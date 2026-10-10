"""
OSM Data Toolkit - GUI Package
==============================

This package contains the graphical user interface components
used by the OSM Data Toolkit QGIS plugin.

The main interface is currently implemented in:

    main_dialog.py

Keeping GUI components inside a separate package makes the
plugin easier to expand.

Future GUI modules may include:

    area_selector.py
        Tools for selecting or drawing areas of interest.

    feature_selector.py
        Tools for selecting OSM feature categories.

    settings_dialog.py
        Plugin configuration and API/download settings.

    progress_dialog.py
        Detailed download and processing progress.

This __init__.py file intentionally contains no executable
plugin logic.
"""