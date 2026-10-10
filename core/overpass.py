"""
OSM Data Toolkit - Overpass Query Generator
============================================

This module builds Overpass QL queries for the OSM Data Toolkit.

Development stage
-----------------
Step 2.2 — Overpass Query Generation

This module is responsible ONLY for generating Overpass QL.

It does NOT:
    - connect to the Overpass API
    - download OSM data
    - process downloaded OSM data
    - create QGIS layers
    - add layers to QGIS

The workflow is:

    AOI
      +
    selected OSM feature definitions
      ↓
    Overpass QL query

The feature definitions are imported from:

    core/osm_features.py

The query generator respects:

    - feature geometry
    - tag values
    - MATCH_ANY
    - MATCH_ALL
    - True tag values
    - single tag values
    - multiple tag values

The actual API downloader will be implemented later.
"""

from typing import List, Sequence

from .osm_features import (
    OSMFeature,
    MATCH_ANY,
    MATCH_ALL,
    get_feature,
)


# ============================================================================
# DEFAULT OVERPASS SETTINGS
# ============================================================================
#
# These settings control the generated Overpass query.
#
# They do NOT make an API request.
#
# The timeout is sent to Overpass when the query is eventually submitted.
# ============================================================================

DEFAULT_TIMEOUT = 180

DEFAULT_OUTPUT_FORMAT = "json"


# ============================================================================
# GEOMETRY MAPPING
# ============================================================================
#
# OSM uses three primary element types relevant to our query:
#
#     node
#     way
#     relation
#
# Our feature definitions use:
#
#     point
#     line
#     polygon
#     mixed
#
# The mapping below translates the feature definition into the
# appropriate Overpass element type.
#
# IMPORTANT:
#
# The geometry requested here refers to the SOURCE OSM ELEMENT TYPE.
#
# For example:
#
#     POI = point
#
# means that only OSM nodes are queried for POI.
#
# We are NOT converting polygons or lines into centroids.
# ============================================================================

GEOMETRY_TO_ELEMENT = {
    "point": ["node"],
    "line": ["way"],
    "polygon": ["way", "relation"],
    "multipolygon": ["relation"],
    "mixed": ["node", "way", "relation"],
}


# ============================================================================
# STRING ESCAPING
# ============================================================================
#
# Overpass QL uses quoted strings for tag values.
#
# This function protects quotation marks and backslashes inside values.
# ============================================================================


def _escape_overpass_string(value: str) -> str:
    """
    Escape a string so it can safely be used as an Overpass
    quoted value.

    Parameters
    ----------
    value : str
        String value to escape.

    Returns
    -------
    str
        Escaped string.
    """

    return (
        str(value)
        .replace("\\", "\\\\")
        .replace('"', '\\"')
    )


def _normalize_admin_levels(admin_levels):
    """
    Validate and normalize selected OSM administrative levels.


    Parameters
    ----------
    admin_levels : int, str, sequence, or None
        Administrative level or levels to retrieve.

        Examples:
            None          -> all administrative levels
            4             -> level 4
            "4"           -> level 4
            [2, 4, 6]     -> levels 2, 4, and 6
            [2, "4", 6]   -> levels 2, 4, and 6

    Returns
    -------
    list[str] or None
        Unique administrative levels sorted numerically, or None
        when no administrative-level restriction is required.

    Raises
    ------
    ValueError
        If a level is outside 0–15, is not an integer or numeric
        string, or if an explicitly supplied selection is empty.

    Notes
    -----
    Administrative-level meanings vary by country. This function
    validates the numeric range only; it does not assign geographic
    meanings to individual levels.
    """

    if admin_levels is None:
        return None

    # Allow a single level as well as a sequence of levels.
    if isinstance(admin_levels, (int, str)) and not isinstance(
        admin_levels, bool
    ):
        levels = [admin_levels]
    else:
        try:
            levels = list(admin_levels)
        except TypeError as exc:
            raise ValueError(
                "Administrative levels must be an integer, a numeric "
                "string, a sequence of levels, or None."
            ) from exc

    if not levels:
        raise ValueError(
            "Select at least one administrative level, "
            "or use None to retrieve all levels."
        )

    normalized = set()
    invalid = []

    for level in levels:

        # Booleans are subclasses of int in Python, so reject them
        # explicitly rather than interpreting True as level 1.
        if isinstance(level, bool):
            invalid.append(repr(level))
            continue

        # Accept integers and strings containing integer digits.
        if isinstance(level, int):
            numeric_level = level

        elif isinstance(level, str):
            value = level.strip()

            if not value.isdigit():
                invalid.append(repr(level))
                continue

            numeric_level = int(value)

        else:
            # Reject floats, including 2.0, and unsupported types.
            invalid.append(repr(level))
            continue

        if not 0 <= numeric_level <= 15:
            invalid.append(repr(level))
            continue

        normalized.add(str(numeric_level))

    if invalid:
        raise ValueError(
            "Invalid administrative level(s): "
            + ", ".join(invalid)
            + ". Supported levels are 0–15."
        )

    return sorted(normalized, key=int)


# ============================================================================
# TAG FILTER BUILDER
# ============================================================================
#
# Converts one tag definition into an Overpass tag filter.
#
# Examples:
#
#     {"highway": True}
#
# becomes:
#
#     ["highway"]
#
#
#     {"boundary": "administrative"}
#
# becomes:
#
#     ["boundary"="administrative"]
#
#
#     {"highway": ["primary", "secondary"]}
#
# becomes:
#
#     ["highway"~"^(primary|secondary)$"]
#
# The generated expression is intended to be combined with an
# Overpass element type and AOI later.
# ============================================================================


def _build_tag_filter(
    key: str,
    value,
) -> str:
    """
    Build an Overpass tag filter for one OSM tag definition.

    Parameters
    ----------
    key : str
        OSM tag key.

    value : bool, str or list[str]
        OSM tag value definition.

    Returns
    -------
    str
        Overpass tag filter.

    Raises
    ------
    ValueError
        If the supplied tag value type is unsupported.
    """

    key = _escape_overpass_string(key)

    # ------------------------------------------------------------------------
    # ANY VALUE
    # ------------------------------------------------------------------------
    #
    # True means:
    #
    #     the OSM key must exist, regardless of its value.
    #
    # Example:
    #
    #     "building": True
    #
    # becomes:
    #
    #     ["building"]
    # ------------------------------------------------------------------------

    if value is True:
        return f'["{key}"]'

    # ------------------------------------------------------------------------
    # SINGLE VALUE
    # ------------------------------------------------------------------------

    if isinstance(value, str):

        escaped_value = _escape_overpass_string(value)

        return (
            f'["{key}"="{escaped_value}"]'
        )

    # ------------------------------------------------------------------------
    # MULTIPLE VALUES
    # ------------------------------------------------------------------------
    #
    # Multiple values represent alternatives for the SAME OSM key.
    #
    # Example:
    #
    #     "railway": [
    #         "station",
    #         "halt",
    #         "tram_stop",
    #     ]
    #
    # becomes a regular-expression filter matching any of those values.
    #
    # Anchors (^ and $) are used so that partial matches are not returned.
    # ------------------------------------------------------------------------

    if isinstance(value, list):

        if not value:
            raise ValueError(
                f"Tag '{key}' contains an empty value list."
            )

        escaped_values = [
            _escape_overpass_string(item)
            for item in value
        ]

        regex = "|".join(escaped_values)

        return (
            f'["{key}"~"^({regex})$"]'
        )

    # ------------------------------------------------------------------------
    # UNSUPPORTED TYPE
    # ------------------------------------------------------------------------

    raise ValueError(
        f"Unsupported tag value type for '{key}': "
        f"{type(value).__name__}"
    )


# ============================================================================
# FEATURE TAG FILTERS
# ============================================================================
#
# Builds the tag portion of an Overpass query for a complete feature.
#
# MATCH_ANY
# ---------
#
# Each tag condition is an alternative.
#
# Example:
#
#     building
#     OR slum=yes
#     OR informal=yes
#
# requires separate Overpass selectors.
#
#
# MATCH_ALL
# ---------
#
# All tag filters can be placed on the same selector.
#
# Example:
#
#     ["building"]["slum"="yes"]
#
# This is reserved for future feature definitions.
# ============================================================================


def _build_feature_selectors(
    feature: OSMFeature,
    aoi_filter: str,
    admin_levels=None,
) -> List[str]:
    """
    Build Overpass selectors for one OSM feature.

    Parameters
    ----------
    feature : OSMFeature
        Feature definition from osm_features.py.

    aoi_filter : str
        Overpass AOI filter.

    Returns
    -------
    list[str]
        One or more complete Overpass selectors.
    """

    # Apply admin_level only to the administrative-boundary feature.
    # This combines boundary=administrative with the selected levels,
    # rather than treating admin_level as an alternative tag.
    admin_level_filter = ""

    if feature.feature_id == "administrative_boundaries":
        normalized_levels = _normalize_admin_levels(admin_levels)

        if normalized_levels is not None:
            levels_regex = "|".join(normalized_levels)
            admin_level_filter = (
                f'["admin_level"~"^({levels_regex})$"]'
            )

    element_types = GEOMETRY_TO_ELEMENT.get(
        feature.geometry
    )

    if element_types is None:
        raise ValueError(
            f"Unsupported geometry type '{feature.geometry}' "
            f"for feature '{feature.feature_id}'."
        )

    # Build the individual tag filters.
    tag_filters = [
        _build_tag_filter(key, value)
        for key, value in feature.tags.items()
    ]

    if not tag_filters:
        raise ValueError(
            f"Feature '{feature.feature_id}' has no tag definitions."
        )

    selectors = []

    # ========================================================================
    # MATCH_ANY
    # ========================================================================
    #
    # Each tag condition becomes its own selector.
    #
    # Example:
    #
    # way["building"](AOI);
    # way["slum"="yes"](AOI);
    # way["informal"="yes"](AOI);
    #
    # This correctly represents:
    #
    # building OR slum=yes OR informal=yes
    # ========================================================================

    if feature.match_mode == MATCH_ANY:

        for element_type in element_types:

            for tag_filter in tag_filters:

                selectors.append(
                    f"{element_type}"
                    f"{tag_filter}"
                    f"{admin_level_filter}"
                    f"{aoi_filter}"
                    ";"
                )

        return selectors

    # ========================================================================
    # MATCH_ALL
    # ========================================================================
    #
    # All tag conditions are applied to the same selector.
    #
    # Example:
    #
    # way["building"]["slum"="yes"](AOI);
    # ========================================================================

    if feature.match_mode == MATCH_ALL:

        combined_filters = "".join(tag_filters)

        for element_type in element_types:

            selectors.append(
                f"{element_type}"
                f"{combined_filters}"
                f"{admin_level_filter}"
                f"{aoi_filter}"
                ";"
            )

        return selectors

    # ========================================================================
    # UNKNOWN MATCH MODE
    # ========================================================================

    raise ValueError(
        f"Unsupported match mode '{feature.match_mode}' "
        f"for feature '{feature.feature_id}'."
    )


# ============================================================================
# AOI FILTER
# ============================================================================
#
# Overpass accepts a bounding-box filter in this form:
#
#     (south,west,north,east)
#
# The AOI values must therefore be supplied in geographic coordinates:
#
#     latitude / longitude
#
# IMPORTANT:
#
# QGIS AOI geometries may be stored in a projected CRS such as EPSG:32737.
# Coordinate conversion will therefore be handled before this function
# is called, or by a later AOI-to-Overpass adapter.
#
# This function intentionally accepts explicit WGS84 coordinates.
# ============================================================================


def build_bbox_filter(
    south: float,
    west: float,
    north: float,
    east: float,
) -> str:
    """
    Build an Overpass bounding-box filter.

    Parameters
    ----------
    south : float
        Southern latitude.

    west : float
        Western longitude.

    north : float
        Northern latitude.

    east : float
        Eastern longitude.

    Returns
    -------
    str
        Overpass bounding-box expression.

    Raises
    ------
    ValueError
        If the bounding box is invalid.
    """

    if south > north:
        raise ValueError(
            "South latitude cannot be greater than north latitude."
        )

    if west > east:
        raise ValueError(
            "West longitude cannot be greater than east longitude."
        )

    if not (-90 <= south <= 90):
        raise ValueError(
            f"Invalid south latitude: {south}"
        )

    if not (-90 <= north <= 90):
        raise ValueError(
            f"Invalid north latitude: {north}"
        )

    if not (-180 <= west <= 180):
        raise ValueError(
            f"Invalid west longitude: {west}"
        )

    if not (-180 <= east <= 180):
        raise ValueError(
            f"Invalid east longitude: {east}"
        )

    return (
        f"({south},{west},{north},{east})"
    )


# ============================================================================
# OVERPASS QUERY BUILDER
# ============================================================================
#
# This is the main public function of this module.
#
# It accepts:
#
#     selected feature IDs
#     AOI bounding box
#
# and returns a complete Overpass QL query.
#
# NO INTERNET CONNECTION IS MADE.
# ============================================================================


def build_overpass_query(
    feature_ids: Sequence[str],
    south: float,
    west: float,
    north: float,
    east: float,
    timeout: int = DEFAULT_TIMEOUT,
    admin_levels=None,
) -> str:
    """
    Build a complete Overpass QL query.

    Parameters
    ----------
    feature_ids : sequence[str]
        IDs of the OSM features to download.

    south : float
        Southern latitude of the AOI.

    west : float
        Western longitude of the AOI.

    north : float
        Northern latitude of the AOI.

    east : float
        Eastern longitude of the AOI.

    timeout : int, optional
        Overpass query timeout in seconds.

    Returns
    -------
    str
        Complete Overpass QL query.

    Raises
    ------
    ValueError
        If no features are supplied or the AOI is invalid.
    """

    # ------------------------------------------------------------------------
    # Validate selected features
    # ------------------------------------------------------------------------

    if not feature_ids:
        raise ValueError(
            "At least one OSM feature must be selected."
        )

    # ------------------------------------------------------------------------
    # Validate timeout
    # ------------------------------------------------------------------------

    if timeout <= 0:
        raise ValueError(
            "Overpass timeout must be greater than zero."
        )

    # ------------------------------------------------------------------------
    # Build AOI
    # ------------------------------------------------------------------------

    aoi_filter = build_bbox_filter(
        south=south,
        west=west,
        north=north,
        east=east,
    )

    # ------------------------------------------------------------------------
    # Build all feature selectors
    # ------------------------------------------------------------------------

    selectors = []

    for feature_id in feature_ids:

        feature = get_feature(feature_id)

        feature_selectors = _build_feature_selectors(
            feature=feature,
            aoi_filter=aoi_filter,
            admin_levels=admin_levels,
        )

        selectors.extend(feature_selectors)

    if not selectors:
        raise ValueError(
            "No Overpass selectors were generated."
        )

    # ------------------------------------------------------------------------
    # Build final query
    # ------------------------------------------------------------------------
    #
    # The individual selectors are combined into one Overpass union.
    #
    # `out body geom;` requests:
    #
    #     tags
    #     element metadata
    #     geometry
    #
    # Geometry is needed later when converting the Overpass response
    # into GIS features.
    # ------------------------------------------------------------------------

    query_lines = [
        f"[out:{DEFAULT_OUTPUT_FORMAT}]",
        f"[timeout:{timeout}];",
        "(",
    ]

    query_lines.extend(
        f"  {selector}"
        for selector in selectors
    )

    query_lines.extend([
        ");",

        # Return selected OSM elements with their tags and geometry.
        "out body geom;",

        # Retrieve relation members needed to reconstruct polygon rings.
        ">;",

        # Return member ways with their geometry and attributes.
        "out body geom;",
    ])

    return "\n".join(query_lines)


# ============================================================================
# CONVENIENCE FUNCTION — FEATURE OBJECTS
# ============================================================================
#
# Some parts of the plugin may already have OSMFeature objects instead
# of feature IDs.
#
# This helper avoids forcing those callers to convert objects back into
# IDs first.
# ============================================================================


def build_overpass_query_from_features(
    features: Sequence[OSMFeature],
    south: float,
    west: float,
    north: float,
    east: float,
    timeout: int = DEFAULT_TIMEOUT,
    admin_levels=None,
) -> str:
    """
    Build an Overpass query from OSMFeature objects.

    Parameters
    ----------
    features : sequence[OSMFeature]
        OSM feature definitions.

    south : float
        Southern latitude.

    west : float
        Western longitude.

    north : float
        Northern latitude.

    east : float
        Eastern longitude.

    timeout : int, optional
        Overpass query timeout.

    Returns
    -------
    str
        Complete Overpass QL query.
    """

    if not features:
        raise ValueError(
            "At least one OSM feature must be supplied."
        )

    # Validate the Overpass query timeout.
    if timeout <= 0:
        raise ValueError(
            "Overpass timeout must be greater than zero."
        )

    selectors = []

    aoi_filter = build_bbox_filter(
        south=south,
        west=west,
        north=north,
        east=east,
    )

    for feature in features:

        selectors.extend(
            _build_feature_selectors(
                feature=feature,
                aoi_filter=aoi_filter,
                admin_levels=admin_levels,
            )
        )

    query_lines = [
        f"[out:{DEFAULT_OUTPUT_FORMAT}]",
        f"[timeout:{timeout}];",
        "(",
    ]

    query_lines.extend(
        f"  {selector}"
        for selector in selectors
    )

    query_lines.extend([
        ");",

        # Return selected OSM elements with their tags and geometry.
        "out body geom;",

        # Retrieve relation members needed to reconstruct polygon rings.
        ">;",

        # Return member ways with their geometry and attributes.
        "out body geom;",
    ])

    return "\n".join(query_lines)


# ============================================================================
# MODULE TEST
# ============================================================================
#
# This test runs only when overpass.py is executed directly.
#
# It does NOT contact Overpass.
#
# It simply demonstrates that the query generator works and prints
# several representative queries.
# ============================================================================


if __name__ == "__main__":

    print("=" * 80)
    print("OSM DATA TOOLKIT — OVERPASS QUERY GENERATOR TEST")
    print("=" * 80)

    # ------------------------------------------------------------------------
    # TEST AOI
    # ------------------------------------------------------------------------
    #
    # Example coordinates only.
    #
    # Nairobi approximate test bounding box.
    # These coordinates are NOT used to contact the internet.
    # ------------------------------------------------------------------------

    south = -1.35
    west = 36.70
    north = -1.15
    east = 36.95

    # ------------------------------------------------------------------------
    # TEST 1 — ROADS
    # ------------------------------------------------------------------------

    print()
    print("-" * 80)
    print("TEST 1 — ROADS")
    print("-" * 80)

    roads_query = build_overpass_query(
        feature_ids=["roads"],
        south=south,
        west=west,
        north=north,
        east=east,
    )

    print(roads_query)

    # ------------------------------------------------------------------------
    # TEST 2 — BUILDINGS
    # ------------------------------------------------------------------------

    print()
    print("-" * 80)
    print("TEST 2 — BUILDINGS")
    print("-" * 80)

    buildings_query = build_overpass_query(
        feature_ids=["buildings"],
        south=south,
        west=west,
        north=north,
        east=east,
    )

    print(buildings_query)

    # ------------------------------------------------------------------------
    # TEST 3 — MULTIPLE FEATURES
    # ------------------------------------------------------------------------

    print()
    print("-" * 80)
    print("TEST 3 — ROADS + BUILDINGS + WATER LINES")
    print("-" * 80)

    multi_query = build_overpass_query(
        feature_ids=[
            "roads",
            "buildings",
            "water_lines",
        ],
        south=south,
        west=west,
        north=north,
        east=east,
    )

    print(multi_query)

    # ------------------------------------------------------------------------
    # TEST COMPLETE
    # ------------------------------------------------------------------------

    print()
    print("=" * 80)
    print("OVERPASS QUERY GENERATOR TEST COMPLETE")
    print("=" * 80)