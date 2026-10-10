"""
OSM Data Toolkit - Area of Interest (AOI)
==========================================

This module contains all Area of Interest (AOI) functionality for the
OSM Data Toolkit QGIS plugin.

The AOI can be created using four different methods:

    1. Current QGIS map extent
    2. Draw rectangle on map
    3. Selected feature(s) in active layer
    4. Active layer extent

All four methods return the same AOI object so that the rest of the
plugin does not need to know how the AOI was created.

Architecture
------------
The GUI (main_dialog.py) is responsible for:

    - Presenting AOI options to the user
    - Starting the selected AOI method
    - Displaying AOI information

This module is responsible for:

    - Creating AOI geometries
    - Managing CRS
    - Transforming geometries
    - Validating AOIs
    - Providing AOI extents for future OSM queries

The OSM downloader should eventually receive an AOI object and should
not need to know which of the four methods was used.
"""


# =============================================================================
# IMPORTS
# =============================================================================

from dataclasses import dataclass
from typing import Optional

from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsGeometry,
    QgsProject,
    QgsRectangle,
    QgsVectorLayer,
)


# =============================================================================
# CONSTANTS
# =============================================================================

# WGS84 is the geographic CRS used by OSM/Overpass queries.
WGS84_CRS = QgsCoordinateReferenceSystem("EPSG:4326")


# =============================================================================
# AOI DATA CLASS
# =============================================================================

@dataclass
class AOI:
    """
    Standard Area of Interest object.

    Every AOI creation method in this module returns this same object.

    Attributes
    ----------
    geometry : QgsGeometry
        The actual AOI geometry in its original/source CRS.

    source_crs : QgsCoordinateReferenceSystem
        CRS in which the AOI geometry was originally created.

    source : str
        Description of how the AOI was created.

    geometry_wgs84 : QgsGeometry
        AOI geometry transformed to EPSG:4326.

    Notes
    -----
    Keeping both the original geometry and WGS84 geometry is useful
    because QGIS operations may need the original CRS, while OSM/
    Overpass queries require geographic coordinates.
    """

    geometry: QgsGeometry

    source_crs: QgsCoordinateReferenceSystem

    source: str

    geometry_wgs84: Optional[QgsGeometry] = None

    # -------------------------------------------------------------------------
    # Source CRS extent
    # -------------------------------------------------------------------------

    @property
    def extent(self) -> QgsRectangle:
        """
        Return the AOI bounding box in the original/source CRS.
        """

        return self.geometry.boundingBox()

    # -------------------------------------------------------------------------
    # WGS84 extent
    # -------------------------------------------------------------------------

    @property
    def wgs84_extent(self) -> QgsRectangle:
        """
        Return the AOI bounding box in WGS84.

        This will eventually be used for Overpass bounding-box queries.
        """

        if self.geometry_wgs84 is None:
            raise ValueError(
                "WGS84 AOI geometry is not available."
            )

        return self.geometry_wgs84.boundingBox()

    # -------------------------------------------------------------------------
    # WGS84 coordinates
    # -------------------------------------------------------------------------

    @property
    def west(self) -> float:
        """Return western longitude."""

        return self.wgs84_extent.xMinimum()

    @property
    def south(self) -> float:
        """Return southern latitude."""

        return self.wgs84_extent.yMinimum()

    @property
    def east(self) -> float:
        """Return eastern longitude."""

        return self.wgs84_extent.xMaximum()

    @property
    def north(self) -> float:
        """Return northern latitude."""

        return self.wgs84_extent.yMaximum()

    # -------------------------------------------------------------------------
    # Human-readable description
    # -------------------------------------------------------------------------

    def description(self) -> str:
        """
        Return a human-readable description of the AOI.
        """

        source_extent = self.extent

        source_crs = self.source_crs.authid()

        text = (
            f"AOI Source: {self.source}\n"
            f"Source CRS: {source_crs}\n"
            f"Source Extent:\n"
            f"  X Min: {source_extent.xMinimum():.6f}\n"
            f"  Y Min: {source_extent.yMinimum():.6f}\n"
            f"  X Max: {source_extent.xMaximum():.6f}\n"
            f"  Y Max: {source_extent.yMaximum():.6f}"
        )

        if self.geometry_wgs84 is not None:

            wgs84_extent = self.wgs84_extent

            text += (
                "\n\n"
                "WGS84 Extent:\n"
                f"  West:  {wgs84_extent.xMinimum():.6f}\n"
                f"  South: {wgs84_extent.yMinimum():.6f}\n"
                f"  East:  {wgs84_extent.xMaximum():.6f}\n"
                f"  North: {wgs84_extent.yMaximum():.6f}"
            )

        return text


# =============================================================================
# GEOMETRY / CRS UTILITIES
# =============================================================================

def transform_geometry_to_wgs84(
    geometry: QgsGeometry,
    source_crs: QgsCoordinateReferenceSystem,
) -> QgsGeometry:
    """
    Transform a geometry from its source CRS to WGS84.

    Parameters
    ----------
    geometry : QgsGeometry
        Input geometry.

    source_crs : QgsCoordinateReferenceSystem
        CRS of the input geometry.

    Returns
    -------
    QgsGeometry
        A copy of the geometry transformed to EPSG:4326.
    """

    if geometry is None or geometry.isEmpty():
        raise ValueError(
            "Cannot transform an empty geometry."
        )

    if not source_crs.isValid():
        raise ValueError(
            "Source CRS is invalid."
        )

    # -------------------------------------------------------------------------
    # Make a copy so that the original AOI geometry is never modified.
    # -------------------------------------------------------------------------

    transformed_geometry = QgsGeometry(geometry)

    # -------------------------------------------------------------------------
    # No transformation is necessary when the source is already WGS84.
    # -------------------------------------------------------------------------

    if source_crs == WGS84_CRS:
        return transformed_geometry

    # -------------------------------------------------------------------------
    # Create the QGIS coordinate transformation.
    # -------------------------------------------------------------------------

    transform = QgsCoordinateTransform(
        source_crs,
        WGS84_CRS,
        QgsProject.instance(),
    )

    # -------------------------------------------------------------------------
    # Apply the transformation.
    # -------------------------------------------------------------------------

    transformed_geometry.transform(transform)

    return transformed_geometry


def create_aoi(
    geometry: QgsGeometry,
    source_crs: QgsCoordinateReferenceSystem,
    source: str,
) -> AOI:
    """
    Create the standard AOI object.

    This is the common function used by all four AOI creation methods.

    Parameters
    ----------
    geometry : QgsGeometry
        AOI geometry.

    source_crs : QgsCoordinateReferenceSystem
        CRS of the geometry.

    source : str
        Description of the AOI creation method.

    Returns
    -------
    AOI
        Standardized AOI object.
    """

    if geometry is None:
        raise ValueError(
            "AOI geometry is missing."
        )

    if geometry.isEmpty():
        raise ValueError(
            "AOI geometry is empty."
        )

    if not source_crs.isValid():
        raise ValueError(
            "AOI source CRS is invalid."
        )

    # -------------------------------------------------------------------------
    # Create WGS84 copy.
    # -------------------------------------------------------------------------

    geometry_wgs84 = transform_geometry_to_wgs84(
        geometry,
        source_crs,
    )

    # -------------------------------------------------------------------------
    # Create and return standard AOI object.
    # -------------------------------------------------------------------------

    return AOI(
        geometry=QgsGeometry(geometry),
        source_crs=source_crs,
        source=source,
        geometry_wgs84=geometry_wgs84,
    )


# =============================================================================
# AOI VALIDATION
# =============================================================================

def validate_aoi(
    aoi: AOI,
) -> tuple[bool, str]:
    """
    Validate an AOI.

    Parameters
    ----------
    aoi : AOI
        AOI object to validate.

    Returns
    -------
    tuple[bool, str]
        Validation status and explanatory message.
    """

    # -------------------------------------------------------------------------
    # Check AOI object.
    # -------------------------------------------------------------------------

    if aoi is None:
        return False, "No AOI has been defined."

    # -------------------------------------------------------------------------
    # Check source geometry.
    # -------------------------------------------------------------------------

    if aoi.geometry is None:
        return False, "AOI geometry is missing."

    if aoi.geometry.isEmpty():
        return False, "AOI geometry is empty."

    # -------------------------------------------------------------------------
    # Check source CRS.
    # -------------------------------------------------------------------------

    if not aoi.source_crs.isValid():
        return False, "AOI source CRS is invalid."

    # -------------------------------------------------------------------------
    # Check WGS84 geometry.
    # -------------------------------------------------------------------------

    if aoi.geometry_wgs84 is None:
        return False, "WGS84 AOI geometry is missing."

    if aoi.geometry_wgs84.isEmpty():
        return False, "WGS84 AOI geometry is empty."

    # -------------------------------------------------------------------------
    # Check WGS84 coordinate range.
    # -------------------------------------------------------------------------

    extent = aoi.wgs84_extent

    if extent.xMinimum() < -180:
        return False, "AOI extends west of -180° longitude."

    if extent.xMaximum() > 180:
        return False, "AOI extends east of 180° longitude."

    if extent.yMinimum() < -90:
        return False, "AOI extends south of -90° latitude."

    if extent.yMaximum() > 90:
        return False, "AOI extends north of 90° latitude."

    return True, "AOI is valid."

## Method 1: Current QGIS Map Extent
# =============================================================================
# 1. CURRENT QGIS MAP EXTENT
# =============================================================================

def get_current_map_extent(
    iface,
) -> AOI:
    """
    Create an AOI from the current QGIS map canvas extent.

    This method uses the current visible extent of the QGIS map canvas.

    Parameters
    ----------
    iface :
        QGIS interface object.

    Returns
    -------
    AOI
        Standard AOI object.
    """

    # -------------------------------------------------------------------------
    # Get map canvas.
    # -------------------------------------------------------------------------

    canvas = iface.mapCanvas()

    if canvas is None:
        raise RuntimeError(
            "QGIS map canvas could not be accessed."
        )

    # -------------------------------------------------------------------------
    # Get current map extent.
    # -------------------------------------------------------------------------

    extent = canvas.extent()

    if extent.isEmpty():
        raise ValueError(
            "The current QGIS map extent is empty."
        )

    # -------------------------------------------------------------------------
    # Get the map canvas CRS.
    # -------------------------------------------------------------------------

    source_crs = canvas.mapSettings().destinationCrs()

    if not source_crs.isValid():
        raise ValueError(
            "The QGIS map canvas CRS is invalid."
        )

    # -------------------------------------------------------------------------
    # Convert the rectangle to a polygon geometry.
    # -------------------------------------------------------------------------

    geometry = QgsGeometry.fromRect(extent)

    # -------------------------------------------------------------------------
    # Create the standard AOI.
    # -------------------------------------------------------------------------

    return create_aoi(
        geometry=geometry,
        source_crs=source_crs,
        source="Current QGIS map extent",
    )


## Method 2: Draw Rectangle on Map
# =============================================================================
# 2. DRAW RECTANGLE ON MAP
# =============================================================================

def create_drawn_rectangle_aoi(
    geometry: QgsGeometry,
    source_crs: QgsCoordinateReferenceSystem,
) -> AOI:
    """
    Create an AOI from a rectangle drawn by the user on the QGIS map.

    The actual QGIS map-tool interaction will be controlled by
    main_dialog.py or a dedicated map-tool class.

    Once the rectangle has been drawn, its geometry is passed to this
    function.

    Parameters
    ----------
    geometry : QgsGeometry
        Rectangle geometry drawn by the user.

    source_crs : QgsCoordinateReferenceSystem
        CRS of the QGIS map canvas.

    Returns
    -------
    AOI
        Standard AOI object.
    """

    return create_aoi(
        geometry=geometry,
        source_crs=source_crs,
        source="Draw rectangle on map",
    )


# =============================================================================
# 3. SELECTED FEATURE(S) IN ACTIVE LAYER
# =============================================================================

def create_selected_features_aoi(
    layer: QgsVectorLayer,
) -> AOI:
    """
    Create an AOI from the selected feature(s) in the active layer.

    Multiple selected features are combined into one geometry.

    Parameters
    ----------
    layer : QgsVectorLayer
        Active vector layer containing the selected features.

    Returns
    -------
    AOI
        Standard AOI object.
    """

    # -------------------------------------------------------------------------
    # Validate layer.
    # -------------------------------------------------------------------------

    if layer is None:
        raise ValueError(
            "No active layer is available."
        )

    if not isinstance(layer, QgsVectorLayer):
        raise TypeError(
            "The active layer must be a vector layer."
        )

    # -------------------------------------------------------------------------
    # Get selected features.
    # -------------------------------------------------------------------------

    selected_features = layer.selectedFeatures()

    if not selected_features:
        raise ValueError(
            "No features are selected in the active layer."
        )

    # -------------------------------------------------------------------------
    # Collect valid geometries.
    # -------------------------------------------------------------------------

    geometries = []

    for feature in selected_features:

        geometry = feature.geometry()

        if geometry is None:
            continue

        if geometry.isEmpty():
            continue

        geometries.append(
            QgsGeometry(geometry)
        )

    if not geometries:
        raise ValueError(
            "The selected features contain no valid geometry."
        )

    # -------------------------------------------------------------------------
    # Combine the selected geometries.
    # -------------------------------------------------------------------------

    combined_geometry = QgsGeometry.unaryUnion(
        geometries
    )

    if combined_geometry is None:
        raise ValueError(
            "Could not combine the selected feature geometries."
        )

    if combined_geometry.isEmpty():
        raise ValueError(
            "The combined selected-feature geometry is empty."
        )

    # -------------------------------------------------------------------------
    # Get active layer CRS.
    # -------------------------------------------------------------------------

    source_crs = layer.crs()

    if not source_crs.isValid():
        raise ValueError(
            "The active layer CRS is invalid."
        )

    # -------------------------------------------------------------------------
    # Create standard AOI.
    # -------------------------------------------------------------------------

    return create_aoi(
        geometry=combined_geometry,
        source_crs=source_crs,
        source="Selected feature(s) in active layer",
    )


# =============================================================================
# 4. ACTIVE LAYER EXTENT
# =============================================================================

def create_active_layer_extent_aoi(
    layer: QgsVectorLayer,
) -> AOI:
    """
    Create an AOI from the extent of the active vector layer.

    Parameters
    ----------
    layer : QgsVectorLayer
        Active vector layer.

    Returns
    -------
    AOI
        Standard AOI object.
    """

    # -------------------------------------------------------------------------
    # Validate layer.
    # -------------------------------------------------------------------------

    if layer is None:
        raise ValueError(
            "No active layer is available."
        )

    if not isinstance(layer, QgsVectorLayer):
        raise TypeError(
            "The active layer must be a vector layer."
        )

    # -------------------------------------------------------------------------
    # Get layer extent.
    # -------------------------------------------------------------------------

    extent = layer.extent()

    if extent.isEmpty():
        raise ValueError(
            "The active layer extent is empty."
        )

    # -------------------------------------------------------------------------
    # Get layer CRS.
    # -------------------------------------------------------------------------

    source_crs = layer.crs()

    if not source_crs.isValid():
        raise ValueError(
            "The active layer CRS is invalid."
        )

    # -------------------------------------------------------------------------
    # Convert extent to geometry.
    # -------------------------------------------------------------------------

    geometry = QgsGeometry.fromRect(extent)

    # -------------------------------------------------------------------------
    # Create standard AOI.
    # -------------------------------------------------------------------------

    return create_aoi(
        geometry=geometry,
        source_crs=source_crs,
        source="Active layer extent",
    )


# =============================================================================
# END OF MODULE
# =============================================================================

