"""
OSM Data Toolkit - AOI Rectangle Map Tool
=========================================

This module contains the interactive QGIS map tool used by
the "Draw rectangle on map" AOI method.

Responsibilities
----------------
This module ONLY handles interaction with the QGIS map canvas:

    1. Detect mouse press.
    2. Detect mouse movement.
    3. Draw a temporary rectangle.
    4. Detect mouse release.
    5. Return the completed rectangle geometry.

The actual AOI creation, validation and CRS conversion remain
in core/aoi.py.

This separation keeps main_dialog.py focused on the GUI.
"""

from qgis.PyQt.QtCore import Qt, pyqtSignal
from qgis.PyQt.QtGui import QColor

from qgis.core import (
    Qgis,
    QgsGeometry,
    QgsRectangle,
    QgsWkbTypes,
)

from qgis.gui import (
    QgsMapTool,
    QgsRubberBand,
)


# Polygon geometry type: Qgis.GeometryType.Polygon exists on QGIS >= 3.30;
# QgsWkbTypes.PolygonGeometry is the older spelling.
try:
    POLYGON_GEOMETRY = Qgis.GeometryType.Polygon
except AttributeError:
    POLYGON_GEOMETRY = QgsWkbTypes.PolygonGeometry


class RectangleAOIMapTool(QgsMapTool):
    """
    Interactive rectangle drawing tool for the QGIS map canvas.

    The tool emits a signal when the user completes a rectangle.

    Signal
    ------
    rectangle_finished(QgsGeometry)
        Emitted when a valid rectangle has been drawn.
    """

    rectangle_finished = pyqtSignal(object)

    def __init__(self, canvas):
        """
        Initialise the rectangle map tool.

        Parameters
        ----------
        canvas : QgsMapCanvas
            QGIS map canvas on which the rectangle will be drawn.
        """

        super().__init__(canvas)

        self.canvas = canvas

        # Starting point of the rectangle.
        self.start_point = None

        # Temporary rectangle displayed while the user is drawing.
        self.rubber_band = QgsRubberBand(
            self.canvas,
            POLYGON_GEOMETRY,
        )

        # Configure the temporary rectangle appearance.
        self.rubber_band.setColor(
            QColor(20, 153, 214, 180)
        )

        self.rubber_band.setWidth(2)

        self.rubber_band.setFillColor(
            QColor(20, 153, 214, 50)
        )

    # ========================================================================
    # MOUSE PRESS
    # ========================================================================

    def canvasPressEvent(self, event):
        """
        Start drawing when the user presses the left mouse button.
        """

        if event.button() != Qt.MouseButton.LeftButton:
            return

        # Convert screen coordinates to map coordinates.
        self.start_point = self.toMapCoordinates(
            event.pos()
        )

        # Remove any previous temporary rectangle.
        self.rubber_band.reset(
            POLYGON_GEOMETRY
        )

    # ========================================================================
    # MOUSE MOVE
    # ========================================================================

    def canvasMoveEvent(self, event):
        """
        Update the temporary rectangle while the mouse moves.
        """

        if self.start_point is None:
            return

        current_point = self.toMapCoordinates(
            event.pos()
        )

        rectangle = QgsRectangle(
            self.start_point,
            current_point,
        )

        geometry = QgsGeometry.fromRect(
            rectangle
        )

        self.rubber_band.setToGeometry(
            geometry,
            self.canvas.mapSettings().destinationCrs(),
        )

    # ========================================================================
    # MOUSE RELEASE
    # ========================================================================

    def canvasReleaseEvent(self, event):
        """
        Finish the rectangle when the left mouse button is released.
        """

        if event.button() != Qt.MouseButton.LeftButton:
            return

        if self.start_point is None:
            return

        end_point = self.toMapCoordinates(
            event.pos()
        )

        rectangle = QgsRectangle(
            self.start_point,
            end_point,
        )

        # Reset the starting point before emitting the result.
        self.start_point = None

        # Reject zero-area rectangles.
        if rectangle.isEmpty():
            self.rubber_band.reset(
                POLYGON_GEOMETRY
            )
            return

        geometry = QgsGeometry.fromRect(
            rectangle
        )

        # Emit the completed geometry.
        self.rectangle_finished.emit(
            geometry
        )

    # ========================================================================
    # CLEAN-UP
    # ========================================================================

    def clear(self):
        """
        Remove the temporary rectangle from the map canvas.
        """

        self.start_point = None

        self.rubber_band.reset(
            POLYGON_GEOMETRY
        )

    def deactivate(self):
        """
        Clean up when the map tool is deactivated.
        """

        self.clear()

        super().deactivate()