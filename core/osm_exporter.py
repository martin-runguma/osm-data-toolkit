"""OSM Data Toolkit - Overpass response parsing and vector-data export.

This module runs inside QGIS and keeps file export separate from GUI code. It
converts Overpass JSON elements to QGIS layers, writes GeoPackage or Shapefile
outputs, and provides helpers to load the exported layers into QGIS.

Administrative boundary relations are assembled from their outer and inner
member ways. Incomplete or invalid relation geometries are skipped rather
than being incorrectly exported as lines or partial polygons.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from collections import defaultdict
from typing import Any, Dict, Iterable, List, Optional, Tuple

from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsFeature,
    QgsField,
    QgsGeometry,
    QgsPointXY,
    QgsProject,
    QgsVectorFileWriter,
    QgsVectorLayer,
)
from qgis.PyQt.QtCore import QVariant

try:
    from qgis.PyQt.QtCore import QMetaType
except ImportError:
    QMetaType = None

from qgis.core import NULL, Qgis

# Field type for text fields.
#   * QGIS >= 3.38 (required on Qt6/PyQt6): QMetaType.Type.QString
#   * older QGIS (Qt5 only): QVariant.String
try:
    _qgis_int = Qgis.versionInt()
except Exception:
    _qgis_int = 0

if QMetaType is not None and _qgis_int >= 33800:
    STRING_FIELD_TYPE = QMetaType.Type.QString
else:
    STRING_FIELD_TYPE = QVariant.String

def _writer_enum(enum_name, member):
    """
    Resolve a QgsVectorFileWriter enum member on any QGIS/Qt build.

    Newer QGIS (and all PyQt6 builds) expose scoped names such as
    QgsVectorFileWriter.WriterError.NoError; older PyQt5 builds only
    expose QgsVectorFileWriter.NoError. Try the scoped form first.
    """
    scoped = getattr(QgsVectorFileWriter, enum_name, None)
    if scoped is not None and hasattr(scoped, member):
        return getattr(scoped, member)
    return getattr(QgsVectorFileWriter, member)


WRITER_NO_ERROR = _writer_enum("WriterError", "NoError")
WRITE_CREATE_OVERWRITE_FILE = _writer_enum(
    "ActionOnExistingFile", "CreateOrOverwriteFile"
)
WRITE_CREATE_OVERWRITE_LAYER = _writer_enum(
    "ActionOnExistingFile", "CreateOrOverwriteLayer"
)



OUTPUT_CRS = QgsCoordinateReferenceSystem("EPSG:4326")
CORE_ATTRIBUTE_FIELDS = [
    "osm_id",
    "osm_type",
    "osm_version",
    "osm_timestamp",
    "osm_changeset",
    "osm_uid",
    "osm_user",
]

# Layer names under which bus-stop points can appear in the intermediate
# GeoPackage (layers are named "<feature_id>_<geometry_family>", so the real
# name is the singular form). Whatever the source name, the Shapefile output
# is always written under BUS_POINT_OUTPUT_NAME.
BUS_POINT_LAYER_NAMES = ("bus_stops_point", "bus_stops_points")
BUS_POINT_OUTPUT_NAME = "bus_stops_points"


# -----------------------------------------------------------------------------
# Feature-specification helpers
# -----------------------------------------------------------------------------

def _safe_layer_name(value: str) -> str:
    """Return a stable, GeoPackage-safe layer/table name."""
    value = re.sub(r"[^A-Za-z0-9_]+", "_", value.strip()).strip("_")
    if not value:
        value = "osm_features"
    if value[0].isdigit():
        value = f"osm_{value}"
    return value[:60]


def _get_feature_spec(feature_id: str):
    """Fetch one existing core feature specification without duplicating it."""
    from .osm_features import get_feature

    return get_feature(feature_id)


def _spec_tags(spec: Any) -> Dict[str, Any]:
    """Read the tag-filter mapping from the project's feature-spec object."""
    for attr in ("tags", "tag_filters", "filters", "tag_filter"):
        value = getattr(spec, attr, None)
        if isinstance(value, dict):
            return value
    raise AttributeError(
        f"Feature specification {spec!r} does not expose a tag-filter mapping."
    )


def _spec_match_mode(spec: Any) -> str:
    """Read a feature's match mode, defaulting to OR for older specs."""
    value = getattr(spec, "match_mode", getattr(spec, "match", "OR"))
    value = getattr(value, "value", value)
    return "AND" if str(value).upper().endswith("AND") else "OR"


def _spec_geometry(spec: Any) -> str:
    """Read the declared geometry family from a feature specification."""
    for attr in ("geometry", "geometry_type", "geometry_family"):
        value = getattr(spec, attr, None)
        if value is not None:
            value = getattr(value, "value", value)
            return str(value).lower()
    return "mixed"


def _tag_value_matches(actual: Any, expected: Any) -> bool:
    """Apply the same True/string/list semantics used by the Overpass builder."""
    if expected is True:
        return actual is not None
    if isinstance(expected, str):
        return str(actual) == expected
    if isinstance(expected, (list, tuple, set)):
        return str(actual) in {str(item) for item in expected}
    return False


def _element_matches_spec(element: dict, spec: Any) -> bool:
    """Check whether an OSM element's tags satisfy a feature's tag rules."""
    tags = element.get("tags") or {}
    filters = _spec_tags(spec)
    if not filters:
        return False

    checks = [
        key in tags and _tag_value_matches(tags.get(key), expected)
        for key, expected in filters.items()
    ]
    return all(checks) if _spec_match_mode(spec) == "AND" else any(checks)


# -----------------------------------------------------------------------------
# OSM coordinate and relation-geometry helpers
# -----------------------------------------------------------------------------

def _coordinates_from_way(way: dict) -> List[QgsPointXY]:
    """Convert an OSM way's embedded ``geometry`` coordinates to QGIS points."""
    coordinates = way.get("geometry") or []
    points: List[QgsPointXY] = []

    for coordinate in coordinates:
        if not isinstance(coordinate, dict):
            return []
        if coordinate.get("lat") is None or coordinate.get("lon") is None:
            return []
        try:
            points.append(
                QgsPointXY(float(coordinate["lon"]), float(coordinate["lat"]))
            )
        except (TypeError, ValueError):
            return []

    return points


def _same_point(a: QgsPointXY, b: QgsPointXY) -> bool:
    """Compare geographic coordinates using a small tolerance."""
    tolerance = 1e-9
    return (
        abs(a.x() - b.x()) <= tolerance
        and abs(a.y() - b.y()) <= tolerance
    )


def _stitch_relation_rings(
    segments: List[List[QgsPointXY]],
) -> Tuple[List[List[QgsPointXY]], int]:
    """Join relation member-way segments into closed rings.

    Segments may need to be reversed or attached at either end. The returned
    failure count is the number of segment groups that could not be closed.
    """
    remaining = [list(segment) for segment in segments if len(segment) >= 2]
    rings: List[List[QgsPointXY]] = []
    failed_segments = 0

    while remaining:
        ring = remaining.pop(0)

        # An individual member way can already be a complete closed ring.
        while not _same_point(ring[0], ring[-1]):
            joined = False

            for index, segment in enumerate(remaining):
                if _same_point(ring[-1], segment[0]):
                    ring.extend(segment[1:])
                elif _same_point(ring[-1], segment[-1]):
                    ring.extend(reversed(segment[:-1]))
                elif _same_point(ring[0], segment[-1]):
                    ring = segment[:-1] + ring
                elif _same_point(ring[0], segment[0]):
                    ring = list(reversed(segment[1:])) + ring
                else:
                    continue

                remaining.pop(index)
                joined = True
                break

            if not joined:
                break

        if len(ring) >= 4 and _same_point(ring[0], ring[-1]):
            rings.append(ring)
        else:
            failed_segments += 1

    return rings, failed_segments


def _relation_geometry(
    relation: dict,
    element_lookup: Dict[Tuple[str, int], dict],
) -> Tuple[Optional[QgsGeometry], Optional[str]]:
    """Build a polygon geometry from a relation's outer and inner member ways.

    Inner rings are assigned to the smallest containing outer ring. A relation
    is rejected if an outer or inner ring is incomplete, invalid, or cannot be
    assigned to an outer polygon; this avoids silently losing boundary detail.
    """
    outer_segments: List[List[QgsPointXY]] = []
    inner_segments: List[List[QgsPointXY]] = []

    for member in relation.get("members") or []:
        if not isinstance(member, dict) or member.get("type") != "way":
            continue

        role = member.get("role", "")
        if role not in ("outer", "inner"):
            continue

        # Prefer geometry embedded in the relation response. If unavailable,
        # resolve the member way through the response's OSM type/ID index.
        points = _coordinates_from_way(member)
        if not points:
            try:
                member_id = int(member.get("ref", -1))
            except (TypeError, ValueError):
                member_id = -1
            way = element_lookup.get(("way", member_id))
            if way:
                points = _coordinates_from_way(way)

        if len(points) < 2:
            # Do not allow missing member geometry to produce a partial ring.
            return None, None

        if role == "outer":
            outer_segments.append(points)
        else:
            inner_segments.append(points)

    if not outer_segments:
        return None, None

    outer_rings, failed_outer = _stitch_relation_rings(outer_segments)
    inner_rings, failed_inner = _stitch_relation_rings(inner_segments)

    if not outer_rings or failed_outer or failed_inner:
        return None, None

    outer_polygons = []
    for ring in outer_rings:
        polygon = QgsGeometry.fromPolygonXY([ring])
        if polygon.isNull() or polygon.isEmpty() or not polygon.isGeosValid():
            return None, None
        outer_polygons.append({"ring": ring, "geometry": polygon, "holes": []})

    # Assign each inner ring to the smallest containing outer polygon.
    for inner_ring in inner_rings:
        inner_polygon = QgsGeometry.fromPolygonXY([inner_ring])
        if (
            inner_polygon.isNull()
            or inner_polygon.isEmpty()
            or not inner_polygon.isGeosValid()
        ):
            return None, None

        representative_point = inner_polygon.pointOnSurface()
        if representative_point.isNull() or representative_point.isEmpty():
            return None, None

        containing = [
            outer for outer in outer_polygons
            if outer["geometry"].contains(representative_point)
        ]
        if not containing:
            # An unassigned inner ring may indicate incomplete or inconsistent
            # relation data. Reject it rather than silently dropping the hole.
            return None, None

        smallest_outer = min(
            containing,
            key=lambda item: item["geometry"].area(),
        )
        smallest_outer["holes"].append(inner_ring)

    # QGIS expects: multipolygon -> polygons -> rings -> points.
    multi_polygon = [
        [outer["ring"], *outer["holes"]]
        for outer in outer_polygons
    ]
    geometry = QgsGeometry.fromMultiPolygonXY(multi_polygon)

    if geometry.isNull() or geometry.isEmpty() or not geometry.isGeosValid():
        return None, None

    return geometry, "polygon"


def _element_geometry(
    element: dict,
    declared_geometry: str,
    element_lookup: Optional[Dict[Tuple[str, int], dict]] = None,
) -> Tuple[Optional[QgsGeometry], Optional[str]]:
    """Convert an OSM node, way, or supported polygon relation to QGIS geometry."""
    element_type = element.get("type")

    if element_type == "node":
        lat, lon = element.get("lat"), element.get("lon")
        if lat is None or lon is None:
            return None, None
        try:
            point = QgsPointXY(float(lon), float(lat))
        except (TypeError, ValueError):
            return None, None
        return QgsGeometry.fromPointXY(point), "point"

    if element_type == "relation":
        if declared_geometry not in ("polygon", "multipolygon", "mixed"):
            return None, None
        return _relation_geometry(element, element_lookup or {})

    if element_type != "way":
        return None, None

    points = _coordinates_from_way(element)
    if len(points) < 2:
        return None, None

    is_closed = len(points) >= 4 and _same_point(points[0], points[-1])
    if is_closed and declared_geometry in ("polygon", "multipolygon", "mixed"):
        # Store every polygon feature as MultiPolygon so closed ways and
        # relation geometries can share the same output layer safely.
        polygon = QgsGeometry.fromMultiPolygonXY([[points]])
        if polygon.isNull() or polygon.isEmpty() or not polygon.isGeosValid():
            return None, None
        return polygon, "polygon"

    # Explicit polygon features must never fall back to a line for an open way.
    if declared_geometry in ("polygon", "multipolygon"):
        return None, None

    return QgsGeometry.fromPolylineXY(points), "line"


# -----------------------------------------------------------------------------
# Attribute and temporary-layer creation
# -----------------------------------------------------------------------------

def _osm_attributes(element: dict) -> Dict[str, Optional[str]]:
    """Build stable text attributes for OSM metadata and all available tags."""
    attrs: Dict[str, Optional[str]] = {
        "osm_id": str(element.get("id", "")),
        "osm_type": str(element.get("type", "")),
        "osm_version": str(element.get("version", "")),
        "osm_timestamp": str(element.get("timestamp", "")),
        "osm_changeset": str(element.get("changeset", "")),
        "osm_uid": str(element.get("uid", "")),
        "osm_user": str(element.get("user", "")),
    }

    for key, value in (element.get("tags") or {}).items():
        attrs[str(key)] = (
            json.dumps(value, ensure_ascii=False)
            if isinstance(value, (dict, list))
            else str(value)
        )
    return attrs


def _unique_field_names(names, max_length=250):
    """
    Return output field names that are unique ignoring case.

    OSM tag keys are case-sensitive ("fixme" and "FIXME" are different
    tags), but GeoPackage/SQLite/Shapefile field names are not, so
    duplicates that differ only by case make OGR fail. The first
    occurrence keeps its name; later ones get a numeric suffix.
    """
    used = set()
    result = []
    for name in names:
        base = name[:max_length]
        candidate = base
        counter = 2
        while candidate.lower() in used:
            suffix = f"_{counter}"
            candidate = base[: max_length - len(suffix)] + suffix
            counter += 1
        used.add(candidate.lower())
        result.append(candidate)
    return result


def _make_memory_layer(
    layer_name: str,
    geometry_family: str,
    records: List[Tuple[dict, QgsGeometry]],
) -> QgsVectorLayer:
    """Create a memory layer with the union of the records' attribute fields."""
    geometry_names = {
        "point": "Point",
        "line": "LineString",
        "polygon": "MultiPolygon",
    }
    geometry_name = geometry_names.get(geometry_family)
    if geometry_name is None:
        raise ValueError(f"Unsupported geometry family: {geometry_family}")

    layer = QgsVectorLayer(
        f"{geometry_name}?crs={OUTPUT_CRS.authid() or 'EPSG:4326'}",
        layer_name,
        "memory",
    )
    if not layer.isValid():
        raise RuntimeError(f"Could not create temporary QGIS layer '{layer_name}'.")

    all_fields = set()
    prepared = []
    for element, geometry in records:
        attrs = _osm_attributes(element)
        prepared.append((attrs, geometry))
        all_fields.update(attrs.keys())

    ordered_fields = [name for name in CORE_ATTRIBUTE_FIELDS if name in all_fields]
    ordered_fields.extend(sorted(all_fields.difference(ordered_fields)))

    provider = layer.dataProvider()
    provider.addAttributes([
        QgsField(name, STRING_FIELD_TYPE, len=0)
        for name in _unique_field_names(ordered_fields)
    ])
    layer.updateFields()

    features = []
    for attrs, geometry in prepared:
        feature = QgsFeature(layer.fields())
        feature.setGeometry(geometry)
        feature.setAttributes([attrs.get(name) for name in ordered_fields])
        features.append(feature)

    if features:
        ok, _ = provider.addFeatures(features)
        if not ok:
            raise RuntimeError(f"Could not populate temporary layer '{layer_name}'.")

    layer.updateExtents()
    return layer


def _make_layer_field_names_writable(
    layer: QgsVectorLayer, aggressive: bool = False
) -> bool:
    """
    Rename fields in place so no two names collide ignoring case.

    OGR drivers (GeoPackage, Shapefile, ...) treat field names as
    case-insensitive, while OSM tag keys are case-sensitive. With
    aggressive=True, characters other than letters, digits and
    underscore are also replaced. Returns True if anything was renamed.
    """
    current = list(layer.fields().names())
    wanted = [name.strip() for name in current]
    if aggressive:
        wanted = [
            re.sub(r"[^0-9A-Za-z_]", "_", name) or "field" for name in wanted
        ]
    wanted = [name or "field" for name in wanted]
    wanted = _unique_field_names(wanted)

    changes = {i: new for i, (old, new) in enumerate(zip(current, wanted)) if old != new}
    if not changes:
        return False

    provider = layer.dataProvider()
    # Two-phase rename so a new name can never clash with a name that has
    # not been renamed yet.
    provider.renameAttributes({i: f"__tmp_rename_{i}" for i in changes})
    layer.updateFields()
    provider.renameAttributes(changes)
    layer.updateFields()
    return True


def _write_vector_layer(
    layer: QgsVectorLayer,
    output_path: str,
    layer_name: str,
    driver_name: str,
    action_on_existing_file: int,
) -> None:
    """Write one QGIS vector layer and raise a useful error on failure."""
    # Safety net: guarantee unique (case-insensitive) field names no
    # matter how the layer was built.
    _make_layer_field_names_writable(layer)

    try:
        _write_vector_layer_once(
            layer, output_path, layer_name, driver_name, action_on_existing_file
        )
    except RuntimeError as exc:
        if "already exists" not in str(exc):
            raise
        # OGR still found a clash: sanitise names fully and retry once.
        _make_layer_field_names_writable(layer, aggressive=True)
        try:
            _write_vector_layer_once(
                layer, output_path, layer_name, driver_name,
                action_on_existing_file,
            )
        except RuntimeError as retry_exc:
            # Include the field list so the clashing name can be identified.
            names = ", ".join(layer.fields().names())
            raise RuntimeError(
                f"{retry_exc} [Retried after renaming duplicate fields. "
                f"Field names: {names}]"
            ) from retry_exc


def _write_vector_layer_once(
    layer: QgsVectorLayer,
    output_path: str,
    layer_name: str,
    driver_name: str,
    action_on_existing_file: int,
) -> None:
    """Single write attempt; raises RuntimeError on failure."""
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = driver_name
    options.layerName = layer_name
    options.fileEncoding = "UTF-8"
    options.actionOnExistingFile = action_on_existing_file

    result = QgsVectorFileWriter.writeAsVectorFormatV3(
        layer,
        output_path,
        QgsProject.instance().transformContext(),
        options,
    )
    error_code = result[0]
    error_message = result[1] if len(result) > 1 else ""
    if error_code != WRITER_NO_ERROR:
        raise RuntimeError(
            f"Failed to write layer '{layer_name}' to '{output_path}': "
            f"{error_message}"
        )


# -----------------------------------------------------------------------------
# GeoPackage export
# -----------------------------------------------------------------------------

def export_overpass_response_to_gpkg(
    response: dict,
    selected_feature_ids: Iterable[str],
    output_path: str,
    progress_callback=None,
) -> Dict[str, Any]:
    """Classify the Overpass response and write supported features to GPKG.

    Returns the output path, written layer names, feature counts, and skipped
    element counts. Each selected category is separated by geometry family.
    """
    if not isinstance(response, dict) or not isinstance(response.get("elements"), list):
        raise ValueError(
            "The Overpass response must be a JSON object with an 'elements' list."
        )
    if not output_path:
        raise ValueError("An output GeoPackage path is required.")

    output_path = os.path.abspath(output_path)
    if not output_path.lower().endswith(".gpkg"):
        output_path += ".gpkg"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    selected_feature_ids = list(dict.fromkeys(selected_feature_ids))
    specs = {}
    for feature_id in selected_feature_ids:
        try:
            specs[feature_id] = _get_feature_spec(feature_id)
        except Exception as exc:
            raise ValueError(
                f"Could not load feature definition '{feature_id}': {exc}"
            ) from exc

    elements = response["elements"]
    total = len(elements)
    skipped = {
        "no_geometry": 0,
        "unsupported_relation": 0,
        "unclassified": 0,
        "administrative_member_way": 0,
    }
    buckets = defaultdict(list)

    # Build an index so relation members can be resolved by OSM type and ID.
    element_lookup: Dict[Tuple[str, int], dict] = {}
    for element in elements:
        if not isinstance(element, dict):
            continue
        element_type, element_id = element.get("type"), element.get("id")
        if element_type and element_id is not None:
            try:
                element_lookup[(str(element_type), int(element_id))] = element
            except (TypeError, ValueError):
                continue

    # Only ways belonging to explicitly administrative relations are excluded
    # from the standalone administrative-boundary category.
    administrative_member_way_ids = set()
    for element in elements:
        if not isinstance(element, dict) or element.get("type") != "relation":
            continue
        tags = element.get("tags") or {}
        if tags.get("boundary") != "administrative":
            continue
        for member in element.get("members") or []:
            if (
                isinstance(member, dict)
                and member.get("type") == "way"
                and member.get("role") in ("outer", "inner")
                and member.get("ref") is not None
            ):
                try:
                    administrative_member_way_ids.add(int(member["ref"]))
                except (TypeError, ValueError):
                    continue

    for index, element in enumerate(elements, start=1):
        if not isinstance(element, dict):
            skipped["no_geometry"] += 1
            continue

        matched_specs = [
            (feature_id, spec)
            for feature_id, spec in specs.items()
            if _element_matches_spec(element, spec)
        ]
        if not matched_specs:
            skipped["unclassified"] += 1
            continue

        assigned = False
        for feature_id, spec in matched_specs:
            declared = _spec_geometry(spec)

            # Member ways are used to assemble the complete administrative
            # relation. Do not also export them as standalone admin boundaries.
            if (
                feature_id == "administrative_boundaries"
                and element.get("type") == "way"
                and element.get("id") is not None
            ):
                try:
                    is_admin_member = int(element["id"]) in administrative_member_way_ids
                except (TypeError, ValueError):
                    is_admin_member = False
                if is_admin_member:
                    skipped["administrative_member_way"] += 1
                    continue

            geometry, geometry_family = _element_geometry(
                element=element,
                declared_geometry=declared,
                element_lookup=element_lookup,
            )
            if geometry is None or geometry_family is None:
                if element.get("type") == "relation":
                    skipped["unsupported_relation"] += 1
                else:
                    skipped["no_geometry"] += 1
                continue

            # A line feature remains a line even when the source way is closed.
            if declared in ("line", "linestring") and geometry_family == "polygon":
                points = _coordinates_from_way(element)
                if len(points) < 2:
                    skipped["no_geometry"] += 1
                    continue
                geometry = QgsGeometry.fromPolylineXY(points)
                geometry_family = "line"

            layer_name = _safe_layer_name(f"{feature_id}_{geometry_family}")
            buckets[(feature_id, geometry_family, layer_name)].append(
                (element, geometry)
            )
            assigned = True

        if progress_callback and (index == total or index % 500 == 0):
            progress_callback(
                f"Prepared {index:,} of {total:,} OSM elements for export..."
            )

    nonempty = [(key, rows) for key, rows in buckets.items() if rows]
    if not nonempty:
        raise ValueError(
            "No exportable features matched the selected categories. "
            "Try another AOI or select additional OSM feature categories."
        )

    # Existing output is removed only after classification and geometry
    # preparation have succeeded. (A write error can still leave a partial file.)
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except OSError as exc:
            raise OSError(f"Could not overwrite existing output file: {exc}") from exc

    written_layers = []
    counts = {}
    for layer_index, ((feature_id, geometry_family, layer_name), records) in enumerate(
        nonempty, start=1
    ):
        if progress_callback:
            progress_callback(
                f"Writing layer {layer_index}/{len(nonempty)}: "
                f"{layer_name} ({len(records):,} features)..."
            )

        layer = _make_memory_layer(layer_name, geometry_family, records)
        action = (
            WRITE_CREATE_OVERWRITE_LAYER
            if os.path.exists(output_path)
            else WRITE_CREATE_OVERWRITE_FILE
        )
        _write_vector_layer(layer, output_path, layer_name, "GPKG", action)
        written_layers.append(layer_name)
        counts[layer_name] = len(records)

    return {
        "path": output_path,
        "layers": written_layers,
        "counts": counts,
        "total_features": sum(counts.values()),
        "skipped": skipped,
    }


def load_gpkg_layers(
    output_path: str,
    layer_names: Iterable[str],
) -> List[QgsVectorLayer]:
    """Load exported GeoPackage tables into the current QGIS project."""
    loaded = []
    for layer_name in layer_names:
        uri = f"{output_path}|layername={layer_name}"
        layer = QgsVectorLayer(uri, layer_name, "ogr")
        if not layer.isValid():
            raise RuntimeError(
                f"The exported layer '{layer_name}' could not be opened in QGIS."
            )
        QgsProject.instance().addMapLayer(layer)
        loaded.append(layer)
    return loaded


# -----------------------------------------------------------------------------
# Shapefile-specific field handling and export
# -----------------------------------------------------------------------------

SHAPEFILE_MAX_TEXT_LENGTH = 254   # DBF text field limit (bytes)
SHAPEFILE_MAX_RECORD_BYTES = 65000  # DBF record limit is 65,535 bytes
SHAPEFILE_MAX_FIELDS = 2000         # DBF header limit is about 2,046 fields


def _shapefile_text_value(value):
    """
    Convert an attribute value for a Shapefile (DBF) text field.

    * Missing values stay empty instead of becoming the text "NULL".
    * DBF text fields hold at most 254 bytes, so longer text (OSM tags
      such as description, note or opening_hours) is cut to the limit,
      without splitting a multi-byte character.
    """
    if value is None:
        return None
    try:
        if value == NULL:
            return None
    except Exception:
        pass
    text = str(value)
    encoded = text.encode("utf-8")
    if len(encoded) > SHAPEFILE_MAX_TEXT_LENGTH:
        text = encoded[:SHAPEFILE_MAX_TEXT_LENGTH].decode("utf-8", "ignore")
    return text


def _make_shapefile_safe_layer(
    source_layer: QgsVectorLayer,
    layer_name: str,
) -> Tuple[QgsVectorLayer, Dict[str, str]]:
    """Copy a source layer to memory with unique Shapefile-safe field names.

    Shapefile/DBF field names are limited to 10 characters. Names are shortened
    deterministically and made case-insensitively unique; original-to-shortened
    field-name mappings are returned to the caller.
    """
    geometry_names = {0: "Point", 1: "LineString", 2: "MultiPolygon"}
    geometry_name = geometry_names.get(source_layer.geometryType())
    if geometry_name is None:
        raise RuntimeError(
            "Unsupported geometry type for Shapefile export: "
            f"{source_layer.geometryType()}"
        )

    crs_id = source_layer.crs().authid() or "EPSG:4326"
    safe_layer = QgsVectorLayer(
        f"{geometry_name}?crs={crs_id}", layer_name, "memory"
    )
    if not safe_layer.isValid():
        raise RuntimeError(
            f"Could not create Shapefile staging layer '{layer_name}'."
        )

    source_names = list(source_layer.fields().names())

    # Pass 1: convert values and measure how wide each column really needs
    # to be. A Shapefile (DBF) record may not exceed ~65 KB in total, so
    # fixed 254-byte columns cannot hold the hundreds of tag columns that a
    # large area produces; sizing each column to its data keeps the record
    # small.
    widths = [0] * len(source_names)
    filled = [0] * len(source_names)
    rows = []
    for source_feature in source_layer.getFeatures():
        values = [
            _shapefile_text_value(value)
            for value in source_feature.attributes()
        ]
        for i, value in enumerate(values):
            if value is not None:
                filled[i] += 1
                width = len(value.encode("utf-8"))
                if width > widths[i]:
                    widths[i] = width
        rows.append((QgsGeometry(source_feature.geometry()), values))

    # Choose the columns that fit in the DBF record. Core OSM attributes
    # come first, then the most-populated tags; sparse columns are the
    # ones dropped if the budget is exceeded.
    core = set(CORE_ATTRIBUTE_FIELDS)
    priority = sorted(
        range(len(source_names)),
        key=lambda i: (source_names[i] not in core, -filled[i], i),
    )
    kept = set()
    budget = 1  # deletion-flag byte
    for i in priority:
        width = max(1, widths[i])
        if budget + width > SHAPEFILE_MAX_RECORD_BYTES:
            continue
        if len(kept) >= SHAPEFILE_MAX_FIELDS:
            break
        kept.add(i)
        budget += width
    kept_indexes = sorted(kept)
    dropped_names = [
        source_names[i] for i in range(len(source_names)) if i not in kept
    ]

    used_names = set()
    field_names = []
    field_name_map = {}
    for i in kept_indexes:
        field_name = source_names[i]
        base = re.sub(r"[^A-Za-z0-9_]", "_", field_name).strip("_") or "field"
        if base[0].isdigit():
            base = f"f_{base}"

        candidate = base[:10]
        suffix_number = 1
        while candidate.lower() in used_names:
            suffix = str(suffix_number)
            candidate = f"{base[:10 - len(suffix)]}{suffix}"
            suffix_number += 1

        used_names.add(candidate.lower())
        field_names.append(candidate)
        if candidate != field_name:
            field_name_map[field_name] = candidate

    provider = safe_layer.dataProvider()
    provider.addAttributes([
        QgsField(name, STRING_FIELD_TYPE, len=max(1, widths[i]))
        for name, i in zip(field_names, kept_indexes)
    ])
    safe_layer.updateFields()

    copied_features = []
    for geometry, values in rows:
        feature = QgsFeature(safe_layer.fields())
        feature.setGeometry(geometry)
        feature.setAttributes([values[i] for i in kept_indexes])
        copied_features.append(feature)
    rows = None  # free memory

    if copied_features:
        ok, _ = provider.addFeatures(copied_features)
        if not ok:
            safe_layer.updateExtents()
            added = safe_layer.featureCount()
            if added < len(copied_features):
                details = "; ".join(str(e) for e in provider.errors()[:3])
                raise RuntimeError(
                    f"Could not prepare features for Shapefile layer "
                    f"'{layer_name}' ({added:,} of {len(copied_features):,} "
                    f"features accepted). {details}"
                )

    if dropped_names:
        safe_layer.setCustomProperty(
            "osm_dropped_fields", "\n".join(dropped_names)
        )

    safe_layer.updateExtents()
    return safe_layer, field_name_map


def _report_dropped_fields(layer, layer_name, dropped_fields, progress_callback):
    """Record (and log) columns that could not fit into the Shapefile."""
    dropped = layer.customProperty("osm_dropped_fields") or ""
    names = [n for n in str(dropped).split("\n") if n]
    if not names:
        return
    dropped_fields[layer_name] = names
    if progress_callback:
        shown = ", ".join(names[:8]) + (", ..." if len(names) > 8 else "")
        progress_callback(
            f"Note: {layer_name} has too many tag columns for one Shapefile "
            f"(DBF size limit); {len(names)} rarely-used columns were left "
            f"out ({shown}). Use GeoPackage output to keep every tag."
        )


def _merge_bus_station_centroids(
    point_layer: QgsVectorLayer,
    polygon_layer: QgsVectorLayer,
) -> QgsVectorLayer:
    """Append centroids of amenity=bus_station polygons to bus-stop points.

    Attributes from each source feature are retained by field name. A union of
    both schemas is used so differences between point and polygon tag sets do
    not prevent the merge.
    """
    if not point_layer.isValid() or not polygon_layer.isValid():
        return point_layer

    polygon_fields = polygon_layer.fields()
    amenity_index = polygon_fields.indexFromName("amenity")
    if amenity_index < 0:
        return point_layer

    field_names = list(point_layer.fields().names())
    known_lower = {name.lower(): name for name in field_names}
    for field in polygon_fields:
        if field.name().lower() not in known_lower:
            field_names.append(field.name())
            known_lower[field.name().lower()] = field.name()

    crs_id = point_layer.crs().authid() or "EPSG:4326"
    merged = QgsVectorLayer(f"Point?crs={crs_id}", BUS_POINT_OUTPUT_NAME, "memory")
    if not merged.isValid():
        raise RuntimeError("Could not create the merged bus_stops_points layer.")

    merged_provider = merged.dataProvider()
    merged_provider.addAttributes([
        QgsField(name, STRING_FIELD_TYPE, len=0) for name in field_names
    ])
    merged.updateFields()
    field_positions = {name.lower(): i for i, name in enumerate(field_names)}
    merged_features = []

    def append_feature(source_feature, geometry):
        feature = QgsFeature(merged.fields())
        feature.setGeometry(QgsGeometry(geometry))
        values = [None] * len(field_names)
        for index, field in enumerate(source_feature.fields()):
            values[field_positions[field.name().lower()]] = source_feature.attribute(index)
        feature.setAttributes(values)
        merged_features.append(feature)

    # Keep all existing bus-stop points unchanged.
    for feature in point_layer.getFeatures():
        if not feature.geometry().isNull() and not feature.geometry().isEmpty():
            append_feature(feature, feature.geometry())

    # Add only bus-station polygon centroids, not unrelated polygon features.
    centroid_count = 0
    for feature in polygon_layer.getFeatures():
        if str(feature.attribute(amenity_index) or "").strip().lower() != "bus_station":
            continue
        geometry = feature.geometry()
        if geometry.isNull() or geometry.isEmpty():
            continue
        centroid = geometry.centroid()
        if centroid.isNull() or centroid.isEmpty():
            continue
        append_feature(feature, centroid)
        centroid_count += 1

    if merged_features:
        ok, _ = merged_provider.addFeatures(merged_features)
        if not ok:
            raise RuntimeError("Could not merge bus-station centroids into bus-stop points.")
    merged.updateExtents()
    return merged


def export_overpass_response_to_shapefile(
    response: dict,
    selected_feature_ids: Iterable[str],
    output_directory: str,
    output_prefix: str,
    progress_callback=None,
    admin_levels=None,
) -> Dict[str, Any]:
    """Export selected OSM features to one Shapefile per output layer.

    GeoPackage export performs matching and geometry preparation first, so both
    formats use the same classification and administrative-relation handling.

    Bus-stop points are written as a single ``bus_stops_points`` Shapefile that
    combines the original OSM bus-stop points with the centroids of
    ``amenity=bus_station`` polygons, keeping the attributes of both.
    """
    if not output_directory or not os.path.isdir(output_directory):
        raise ValueError(
            "An existing output directory is required for Shapefile export."
        )
    if not output_prefix or not str(output_prefix).strip():
        raise ValueError("An output name is required for Shapefile export.")

    output_directory = os.path.abspath(output_directory)
    output_prefix = re.sub(
        r"[^A-Za-z0-9_-]+", "_", str(output_prefix).strip()
    ).strip("._-")
    if not output_prefix:
        raise ValueError(
            "The output name does not contain any valid filename characters."
        )

    # Create and then remove the empty temporary file so GDAL can create a new
    # GeoPackage at that path.
    fd, temporary_gpkg = tempfile.mkstemp(
        prefix=".osm_toolkit_temp_", suffix=".gpkg", dir=output_directory
    )
    os.close(fd)
    os.remove(temporary_gpkg)

    written_paths = []
    written_layers = []
    counts = {}
    field_name_maps = {}
    dropped_fields = {}
    skipped = {}

    try:
        intermediate = export_overpass_response_to_gpkg(
            response=response,
            selected_feature_ids=selected_feature_ids,
            output_path=temporary_gpkg,
            progress_callback=progress_callback,
        )
        skipped = intermediate.get("skipped", {})

        for layer_index, layer_name in enumerate(intermediate["layers"], start=1):
            if progress_callback:
                progress_callback(
                    f"Writing Shapefile {layer_index}/"
                    f"{len(intermediate['layers'])}: {layer_name}..."
                )

            source_uri = f"{temporary_gpkg}|layername={layer_name}"
            source_layer = QgsVectorLayer(source_uri, layer_name, "ogr")
            if not source_layer.isValid():
                raise RuntimeError(
                    f"Could not reopen intermediate GeoPackage layer '{layer_name}'."
                )

            # Whatever the source layer is called, bus-stop points are always
            # written under one stable name, merged with station centroids.
            # The original bus_stops_polygon output is retained separately.
            output_name = layer_name
            if layer_name in BUS_POINT_LAYER_NAMES:
                output_name = BUS_POINT_OUTPUT_NAME
                if "bus_stops_polygon" in intermediate["layers"]:
                    polygon_layer = QgsVectorLayer(
                        f"{temporary_gpkg}|layername=bus_stops_polygon",
                        "bus_stops_polygon",
                        "ogr",
                    )
                    if polygon_layer.isValid():
                        source_layer = _merge_bus_station_centroids(
                            source_layer, polygon_layer
                        )
                        if progress_callback:
                            progress_callback(
                                "Merged bus-station polygon centroids into "
                                "bus_stops_points."
                            )

            safe_layer, field_map = _make_shapefile_safe_layer(
                source_layer, output_name
            )
            if field_map:
                field_name_maps[output_name] = field_map
            _report_dropped_fields(
                safe_layer, output_name, dropped_fields, progress_callback
            )

            shapefile_path = os.path.join(
                output_directory,
                f"{output_prefix}_{output_name}.shp",
            )
            _write_vector_layer(
                safe_layer,
                shapefile_path,
                output_name,
                "ESRI Shapefile",
                WRITE_CREATE_OVERWRITE_FILE,
            )

            written_paths.append(shapefile_path)
            written_layers.append(output_name)
            counts[output_name] = safe_layer.featureCount()

            # Keep the combined administrative-boundary Shapefile above, and
            # additionally write one Shapefile for each admin_level present.
            # The split is based on the source attributes before DBF field-name
            # shortening, so the full `admin_level` field remains available.
            if (
                "administrative_boundaries" in layer_name
                and "polygon" in layer_name.lower()
                and "admin_level" in source_layer.fields().names()
            ):
                admin_index = source_layer.fields().indexFromName("admin_level")
                available_levels = set()
                for source_feature in source_layer.getFeatures():
                    raw_level = source_feature.attribute(admin_index)
                    try:
                        available_levels.add(int(raw_level))
                    except (TypeError, ValueError):
                        continue

                if admin_levels is not None:
                    try:
                        requested_levels = {int(level) for level in admin_levels}
                    except (TypeError, ValueError):
                        requested_levels = set()
                    available_levels.intersection_update(requested_levels)

                for level in sorted(available_levels):
                    split_layer = QgsVectorLayer(
                        f"MultiPolygon?crs={source_layer.crs().authid() or 'EPSG:4326'}",
                        f"{layer_name}_Lvl{level}",
                        "memory",
                    )
                    if not split_layer.isValid():
                        raise RuntimeError(
                            f"Could not create temporary layer for admin_level {level}."
                        )
                    split_provider = split_layer.dataProvider()
                    split_provider.addAttributes(list(source_layer.fields()))
                    split_layer.updateFields()
                    split_features = []
                    for source_feature in source_layer.getFeatures():
                        try:
                            feature_level = int(source_feature.attribute(admin_index))
                        except (TypeError, ValueError):
                            continue
                        if feature_level != level:
                            continue
                        split_feature = QgsFeature(split_layer.fields())
                        split_feature.setGeometry(QgsGeometry(source_feature.geometry()))
                        split_feature.setAttributes(source_feature.attributes())
                        split_features.append(split_feature)
                    if not split_features:
                        continue
                    ok, _ = split_provider.addFeatures(split_features)
                    if not ok:
                        raise RuntimeError(
                            f"Could not populate Shapefile for admin_level {level}."
                        )
                    split_layer.updateExtents()
                    split_safe_layer, split_field_map = _make_shapefile_safe_layer(
                        split_layer, f"{layer_name}_Lvl{level}"
                    )
                    split_path = os.path.join(
                        output_directory,
                        f"{output_prefix}_{layer_name}_Lvl{level}.shp",
                    )
                    _write_vector_layer(
                        split_safe_layer,
                        split_path,
                        f"{layer_name}_Lvl{level}",
                        "ESRI Shapefile",
                        WRITE_CREATE_OVERWRITE_FILE,
                    )
                    written_paths.append(split_path)
                    split_name = f"{layer_name}_Lvl{level}"
                    written_layers.append(split_name)
                    counts[split_name] = split_safe_layer.featureCount()
                    if split_field_map:
                        field_name_maps[split_name] = split_field_map

        # If the AOI contains bus-station polygons but no bus-stop point
        # features at all, still create bus_stops_points from their centroids.
        # This only runs when no original point layer exists, so the merged
        # file above is never duplicated.
        if (
            not any(name in BUS_POINT_LAYER_NAMES for name in intermediate["layers"])
            and "bus_stops_polygon" in intermediate["layers"]
        ):
            polygon_layer = QgsVectorLayer(
                f"{temporary_gpkg}|layername=bus_stops_polygon",
                "bus_stops_polygon",
                "ogr",
            )
            if polygon_layer.isValid():
                empty_points = QgsVectorLayer(
                    f"Point?crs={polygon_layer.crs().authid() or 'EPSG:4326'}",
                    BUS_POINT_OUTPUT_NAME,
                    "memory",
                )
                if not empty_points.isValid():
                    raise RuntimeError("Could not create an empty bus_stops_points layer.")
                merged_points = _merge_bus_station_centroids(
                    empty_points, polygon_layer
                )
                if merged_points.featureCount() > 0:
                    safe_points, point_field_map = _make_shapefile_safe_layer(
                        merged_points, BUS_POINT_OUTPUT_NAME
                    )
                    point_path = os.path.join(
                        output_directory,
                        f"{output_prefix}_{BUS_POINT_OUTPUT_NAME}.shp",
                    )
                    _write_vector_layer(
                        safe_points,
                        point_path,
                        BUS_POINT_OUTPUT_NAME,
                        "ESRI Shapefile",
                        WRITE_CREATE_OVERWRITE_FILE,
                    )
                    written_paths.append(point_path)
                    written_layers.append(BUS_POINT_OUTPUT_NAME)
                    counts[BUS_POINT_OUTPUT_NAME] = safe_points.featureCount()
                    if point_field_map:
                        field_name_maps[BUS_POINT_OUTPUT_NAME] = point_field_map
                    _report_dropped_fields(
                        safe_points, BUS_POINT_OUTPUT_NAME, dropped_fields,
                        progress_callback,
                    )
                    if progress_callback:
                        progress_callback(
                            "Created bus_stops_points from bus-station polygon centroids."
                        )

        return {
            "path": output_directory,
            "paths": written_paths,
            "layers": written_layers,
            "counts": counts,
            "total_features": sum(counts.values()),
            "skipped": skipped,
            "field_name_maps": field_name_maps,
            "dropped_fields": dropped_fields,
        }
    finally:
        # Remove the temporary GeoPackage and possible SQLite sidecar files.
        for candidate in (
            temporary_gpkg,
            temporary_gpkg + "-wal",
            temporary_gpkg + "-shm",
        ):
            try:
                if os.path.exists(candidate):
                    os.remove(candidate)
            except OSError:
                pass


def load_shapefile_layers(
    shapefile_paths: Iterable[str],
) -> List[QgsVectorLayer]:
    """Load exported Shapefiles into the current QGIS project."""
    loaded = []
    for shapefile_path in shapefile_paths:
        layer_name = os.path.splitext(os.path.basename(shapefile_path))[0]
        layer = QgsVectorLayer(shapefile_path, layer_name, "ogr")
        if not layer.isValid():
            raise RuntimeError(
                f"The exported Shapefile '{shapefile_path}' could not be opened in QGIS."
            )
        QgsProject.instance().addMapLayer(layer)
        loaded.append(layer)
    return loaded