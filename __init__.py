"""
OSM Data Toolkit - QGIS Plugin
==============================

This file is the entry point for the OSM Data Toolkit QGIS
plugin.

QGIS requires a function named:

    classFactory()

This function creates and returns the main plugin class.

The main plugin controller is located in:

    osm_data_toolkit.py

The graphical interface is located in:

    gui/main_dialog.py

Keeping this entry point small follows the standard QGIS
Python plugin architecture.
"""


def classFactory(iface):
    """
    Create and return the OSM Data Toolkit plugin instance.

    Parameters
    ----------
    iface : QgisInterface
        QGIS interface object supplied automatically by QGIS.

    Returns
    -------
    OSMDataToolkit
        Main OSM Data Toolkit plugin controller.
    """

    # Import the main plugin controller.
    #
    # The "." means that the module is located inside this
    # plugin package.
    from .osm_data_toolkit import OSMDataToolkit

    # Return the plugin instance to QGIS.
    return OSMDataToolkit(iface)