"""
OSM Data Toolkit - Main Plugin Controller
==========================================

This module is the main controller for the OSM Data Toolkit
QGIS plugin.

Responsibilities
----------------
This file handles the communication between QGIS and the
OSM Data Toolkit graphical user interface.

It is responsible for:

    1. Initialising the plugin.
    2. Adding the plugin to the QGIS Plugins menu.
    3. Adding the plugin to the QGIS toolbar.
    4. Opening the main OSM Data Toolkit window.
    5. Cleaning up the plugin when it is disabled.

The actual graphical interface is stored separately in:

    gui/main_dialog.py

Keeping the GUI separate from the main plugin controller makes
the plugin easier to maintain and expand.

Future modules will handle:

    - Area-of-interest processing
    - Overpass API requests
    - OSM query construction
    - OSM data parsing
    - GeoPackage creation
    - Shapefile export
    - Caching
    - Download retries
    - Large-area processing
"""


# ============================================================================
# IMPORTS
# ============================================================================
import os

from qgis.PyQt.QtGui import QIcon

# QAction creates the menu item / toolbar action used by QGIS.
try:
    # Qt6: QAction lives in QtGui.
    from qgis.PyQt.QtGui import QAction
except ImportError:
    # Qt5: QAction lives in QtWidgets.
    from qgis.PyQt.QtWidgets import QAction


# Import our main graphical interface.
#
# The "." means that Python should look inside this plugin's
# own directory.
#
# The GUI itself is located at:
#
#     OSM_Data_Toolkit
#     └── gui
#         └── main_dialog.py
#
from .gui.main_dialog import OSMDataToolkitDialog


# ============================================================================
# MAIN PLUGIN CLASS
# ============================================================================

class OSMDataToolkit:
    """
    Main controller class for the OSM Data Toolkit plugin.

    QGIS creates an instance of this class when the plugin is
    loaded.

    Parameters
    ----------
    iface : QgisInterface
        QGIS interface object supplied automatically by QGIS.

        This object allows the plugin to interact with the
        QGIS application, including:

            - Menus
            - Toolbars
            - Map canvas
            - Layers
            - Main application window
    """

    # ------------------------------------------------------------------------
    # INITIALISATION
    # ------------------------------------------------------------------------

    def __init__(self, iface):
        """
        Initialise the OSM Data Toolkit plugin.

        At this stage we store the QGIS interface and create
        placeholders for the QAction and main dialog.
        """

        # Store the QGIS interface.
        #
        # We will use this later for accessing things such as
        # the current map extent, selected features and layers.
        self.iface = iface

        # QAction represents the plugin entry in the QGIS menu
        # and toolbar.
        #
        # It is initially None because it has not yet been
        # created.
        self.action = None

        # The main plugin dialog.
        #
        # We create this only when the user activates the plugin.
        self.dialog = None

    # ========================================================================
    # QGIS GUI INITIALISATION
    # ========================================================================

    def initGui(self):
        """
        Initialise the OSM Data Toolkit GUI.

        This method creates the menu and toolbar action that
        QGIS uses to launch the plugin.
        """

        # ================================================================
        # PLUGIN ICON
        # ================================================================

        # Get the directory containing this plugin.
        plugin_dir = os.path.dirname(
            os.path.abspath(__file__)
        )

        # Build the complete path to the plugin icon.
        icon_path = os.path.join(
            plugin_dir,
            "icon.png"
        )

        # Create the QGIS action using our custom icon.
        self.action = QAction(
            QIcon(icon_path),
            "OSM Data Toolkit",
            self.iface.mainWindow()
        )

        # Connect the action to the plugin's run method.
        self.action.triggered.connect(
            self.run
        )

        # Add the action to the Plugins menu.
        self.iface.addPluginToMenu(
            "&OSM Data Toolkit",
            self.action
        )

        # Add the action to the QGIS toolbar.
        self.iface.addToolBarIcon(
            self.action
        )

    # ========================================================================
    # PLUGIN UNLOAD
    # ========================================================================

    def unload(self):
        """
        Remove the plugin interface from QGIS.

        QGIS automatically calls this method when the plugin
        is disabled or unloaded.
        """

        # --------------------------------------------------------------------
        # CLOSE THE MAIN DIALOG
        # --------------------------------------------------------------------

        if self.dialog is not None:

            self.dialog.close()

            self.dialog = None

        # --------------------------------------------------------------------
        # REMOVE MENU AND TOOLBAR ACTION
        # --------------------------------------------------------------------

        if self.action is not None:

            # Remove the menu entry.
            self.iface.removePluginMenu(
                "&OSM Data Toolkit",
                self.action
            )

            # Remove the toolbar button.
            self.iface.removeToolBarIcon(
                self.action
            )

            # Clear the reference.
            self.action = None

    # ========================================================================
    # OPEN MAIN DIALOG
    # ========================================================================

    def run(self):
        """
        Open the OSM Data Toolkit main window.

        This method is executed when the user clicks:

            Plugins → OSM Data Toolkit

        or the corresponding toolbar button.
        """

        # Create the dialog once and reuse it.
        #
        # iface is passed explicitly so the dialog can access the map
        # canvas and layers; the QGIS main window is the Qt parent.
        if self.dialog is None:
            self.dialog = OSMDataToolkitDialog(
                self.iface,
                self.iface.mainWindow()
            )

        # show() keeps the dialog non-modal, so the map canvas stays
        # usable (needed for the "Draw AOI" tool).
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()
