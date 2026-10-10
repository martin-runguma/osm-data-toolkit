"""
OSM Data Toolkit - Main Graphical Interface
===========================================

Main QGIS (PyQt5/PyQt6) dialog for the OSM Data Toolkit plugin.

Area of Interest methods:
    1. Current QGIS map extent
    2. Draw rectangle on map
    3. Selected feature(s) in active layer
    4. Active layer extent

Supports:
    - Background Overpass downloading
    - Download cancellation
    - Local query caching
    - GeoPackage and Shapefile exports
    - Optional automatic QGIS layer loading
    - Processing logs and progress reporting
    - Temporary GeoPackage cleanup after successful export

Temporary-file cleanup targets ONLY:
    .osm_toolkit_temp_*.gpkg

Raw OSM response saving is not offered as a separate output option.
"""

from __future__ import annotations

import glob
import html
import os
import re
from datetime import datetime
from typing import Dict, List, Optional

from qgis.core import QgsApplication, QgsVectorLayer
from qgis.PyQt.QtCore import QThread, QUrl
from qgis.PyQt.QtGui import QDesktopServices, QIcon
from qgis.PyQt.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSizePolicy,
    QTextBrowser,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# Core modules
from ..core.aoi import (
    get_current_map_extent,
    create_drawn_rectangle_aoi,
    create_selected_features_aoi,
    create_active_layer_extent_aoi,
    validate_aoi,
)

from ..core.aoi_map_tool import RectangleAOIMapTool
from ..core.overpass import build_overpass_query
from ..core.osm_download_worker import OverpassDownloadWorker
from ..core.osm_exporter import (
    export_overpass_response_to_gpkg,
    export_overpass_response_to_shapefile,
    load_gpkg_layers,
    load_shapefile_layers,
)


# ============================================================================
# CONSTANTS
# ============================================================================

PLUGIN_NAME = "OSM Data Toolkit"

REPOSITORY_URL = "https://github.com/martin-runguma/osm-data-toolkit"
DOCUMENTATION_URL = REPOSITORY_URL + "#readme"
ISSUES_URL = REPOSITORY_URL + "/issues"

LOG_COLORS = {
    "info": "#000000",
    "success": "#2E9E2E",
    "warning": "#D89B00",
    "error": "#D32F2F",
}

FEATURE_LABELS: Dict[str, str] = {
    "buildings": "Buildings",
    "roads": "Roads",
    "railways": "Railways",
    "waterways": "Waterways",
    "landuse": "Landuse",
    "open_public_spaces": "Open public spaces",
    "bus_stops": "Bus stops",
    "rail_stops": "Rail stops",
    "ferry_stops": "Ferry stops",
    "poi": "Points of interest (POI)",
    "boundaries": "Administrative boundaries",
}


# ============================================================================
# QT5 / QT6 COMPATIBILITY HELPERS
# ============================================================================

def _exec_dialog(dialog):
    """Run a modal dialog on both Qt5 (exec_) and Qt6 (exec)."""
    if hasattr(dialog, "exec"):
        return dialog.exec()
    return dialog.exec_()


# ============================================================================
# OUTPUT NAMING DIALOG
# ============================================================================

class OutputNamingDialog(QDialog):
    """Collect optional filename components before exporting OSM data."""

    def __init__(self, output_format: str, parent=None):
        super().__init__(parent)

        self.output_format = output_format
        self.setWindowTitle(f"{PLUGIN_NAME} — Output Naming")
        self.setModal(True)
        self.setMinimumWidth(470)

        self.city_edit = QLineEdit()
        self.city_edit.setPlaceholderText("e.g. Nairobi")

        self.country_edit = QLineEdit()
        self.country_edit.setPlaceholderText("e.g. Kenya")

        self.region_edit = QLineEdit()
        self.region_edit.setPlaceholderText("e.g. NairobiCounty")

        self.aoi_edit = QLineEdit()
        self.aoi_edit.setPlaceholderText("e.g. CBD")

        form = QFormLayout()
        form.addRow("City name:", self.city_edit)
        form.addRow("Country name:", self.country_edit)
        form.addRow("Region name:", self.region_edit)
        form.addRow("AOI name:", self.aoi_edit)

        self.preview_label = QLabel()
        self.preview_label.setWordWrap(True)
        self.preview_label.setStyleSheet(
            "background-color: #EAF4F9; border: 1px solid #C7DDE8; "
            "border-radius: 4px; padding: 8px;"
        )

        self.error_label = QLabel()
        self.error_label.setWordWrap(True)
        self.error_label.setStyleSheet("color: #D32F2F;")

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.button(
            QDialogButtonBox.StandardButton.Ok
        ).setText("Continue to Download")
        buttons.accepted.connect(self._accept_if_valid)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)

        intro = QLabel(
            "Enter one or more name components. Blank fields will be skipped, "
            "and the remaining names will be joined with underscores. "
            "The selected output format will be retained."
        )
        intro.setWordWrap(True)

        layout.addWidget(intro)
        layout.addLayout(form)
        layout.addWidget(QLabel("Filename preview:"))
        layout.addWidget(self.preview_label)

        # Administrative boundary level selection. The default deliberately
        # leaves admin_level unrestricted in the Overpass query.
        self.admin_levels_group = QGroupBox("Administrative boundary levels")
        levels_layout = QVBoxLayout(self.admin_levels_group)
        levels_help = QLabel(
            "Choose all available levels, or select one or more levels "
            "to download (for example, 5–8 or level 5)."
        )
        levels_help.setWordWrap(True)
        levels_layout.addWidget(levels_help)

        self.admin_all_levels_radio = QRadioButton(
            "All levels (0–15; no admin_level filter)"
        )
        self.admin_specific_levels_radio = QRadioButton(
            "Only the selected levels"
        )
        self.admin_all_levels_radio.setChecked(True)
        levels_layout.addWidget(self.admin_all_levels_radio)
        levels_layout.addWidget(self.admin_specific_levels_radio)

        levels_grid = QGridLayout()
        self.admin_level_checks = {}
        for level in range(16):
            check = QCheckBox(str(level))
            check.setEnabled(False)
            self.admin_level_checks[level] = check
            levels_grid.addWidget(check, level // 8, level % 8)
        levels_layout.addLayout(levels_grid)

        level_buttons = QHBoxLayout()
        self.admin_select_all_button = QPushButton("Select all")
        self.admin_clear_all_button = QPushButton("Clear all")
        level_buttons.addWidget(self.admin_select_all_button)
        level_buttons.addWidget(self.admin_clear_all_button)
        level_buttons.addStretch(1)
        levels_layout.addLayout(level_buttons)

        self.admin_level_status = QLabel(
            "All administrative levels will be included."
        )
        self.admin_level_status.setWordWrap(True)
        levels_layout.addWidget(self.admin_level_status)
        layout.addWidget(self.admin_levels_group)

        layout.addWidget(self.error_label)
        layout.addWidget(buttons)

        self.admin_all_levels_radio.toggled.connect(
            self._update_admin_level_controls
        )
        self.admin_specific_levels_radio.toggled.connect(
            self._update_admin_level_controls
        )
        self.admin_select_all_button.clicked.connect(
            self._select_all_admin_levels
        )
        self.admin_clear_all_button.clicked.connect(
            self._clear_admin_levels
        )
        for check in self.admin_level_checks.values():
            check.toggled.connect(self._update_admin_level_status)

        for edit in (
            self.city_edit,
            self.country_edit,
            self.region_edit,
            self.aoi_edit,
        ):
            edit.textChanged.connect(self._update_preview)

        self._update_preview()

    @staticmethod
    def _safe_component(value: str) -> str:
        """Convert a name component into a Windows-safe filename token."""
        value = re.sub(r'[<>:"/\\|?*\x00-\x1f]+', "_", value.strip())
        value = re.sub(r"\s+", "_", value)
        return re.sub(r"_+", "_", value).strip(" ._")

    def output_prefix(self) -> str:
        """Return the combined, sanitized filename prefix."""
        components = [
            self._safe_component(edit.text())
            for edit in (
                self.city_edit,
                self.country_edit,
                self.region_edit,
                self.aoi_edit,
            )
        ]
        return "_".join(component for component in components if component)

    def _update_preview(self, *_args):
        """Update the filename preview as the user edits the components."""
        prefix = self.output_prefix() or "Enter_a_name_to_preview"

        if self.output_format == "GeoPackage":
            preview = f"{prefix}.gpkg"
        else:
            preview = (
                f"{prefix}_roads_line.shp\n"
                f"{prefix}_buildings_polygon.shp"
            )

        self.preview_label.setText(preview)

    def selected_admin_levels(self):
        """Return selected levels, or None when all levels are requested."""
        if self.admin_all_levels_radio.isChecked():
            return None
        return [
            level for level, check in self.admin_level_checks.items()
            if check.isChecked()
        ]

    def _update_admin_level_controls(self, *_args):
        """Enable level checkboxes only when a specific selection is active."""
        specific = self.admin_specific_levels_radio.isChecked()
        for check in self.admin_level_checks.values():
            check.setEnabled(specific)
        self.admin_select_all_button.setEnabled(specific)
        self.admin_clear_all_button.setEnabled(specific)
        self._update_admin_level_status()

    def _select_all_admin_levels(self):
        """Select levels 0–15 and switch to specific-level mode."""
        self.admin_specific_levels_radio.setChecked(True)
        for check in self.admin_level_checks.values():
            check.setChecked(True)
        self._update_admin_level_status()

    def _clear_admin_levels(self):
        """Clear selected levels so the user can make a narrower selection."""
        self.admin_specific_levels_radio.setChecked(True)
        for check in self.admin_level_checks.values():
            check.setChecked(False)
        self._update_admin_level_status()

    def _update_admin_level_status(self, *_args):
        """Show a concise description of the active administrative filter."""
        if self.admin_all_levels_radio.isChecked():
            self.admin_level_status.setText(
                "All administrative levels will be included; no admin_level "
                "filter will be added to the query."
            )
            self.error_label.setText("")
            return

        selected = [
            level for level, check in self.admin_level_checks.items()
            if check.isChecked()
        ]
        if not selected:
            self.admin_level_status.setText(
                "No levels selected. Select at least one level to continue."
            )
        else:
            self.admin_level_status.setText(
                "Selected administrative levels: "
                + ", ".join(map(str, selected))
            )
            self.error_label.setText("")

    def _accept_if_valid(self):
        """Validate filename and any explicitly selected admin levels."""
        prefix = self.output_prefix()

        if not prefix:
            self.error_label.setText(
                "Enter at least one name (City, Country, Region, or AOI)."
            )
            return

        if len(prefix) > 170:
            self.error_label.setText(
                "The combined name is too long. Shorten one or more components."
            )
            return

        if self.admin_specific_levels_radio.isChecked() and not any(
            check.isChecked() for check in self.admin_level_checks.values()
        ):
            self.error_label.setText(
                "Select at least one administrative level, or choose All levels."
            )
            return

        self.accept()


HELP_HTML = """
<h3>Quick start</h3>
<ol>
  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle
      on the map, or use the bounding box of selected features or a
      layer's extent.</li>
  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,
      buildings, boundaries, landuse, ...).</li>
  <li><b>Choose an output format and folder</b>, then click
      <b>Download OSM Data</b>.</li>
</ol>

<h3>Good to know</h3>
<ul>
  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many
      attribute columns, so on large areas some rarely used tag columns
      may be left out (the log tells you when this happens).</li>
  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass
      responses and can be slow or rejected by the public servers.</li>
  <li><b>The cache</b> lets repeat downloads of the same query reuse
      earlier results.</li>
  <li><b>"Unclassified OSM elements"</b> in the log is informational: they
      are mostly untagged vertices of lines and polygons that do not belong
      to any selected category.</li>
</ul>

<p>Data &copy; OpenStreetMap contributors, available under the
<a href="https://www.openstreetmap.org/copyright">Open Database
Licence</a>.</p>
"""


class HelpDialog(QDialog):
    """Short in-plugin help with links to the full online documentation."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{PLUGIN_NAME} — Help")
        self.resize(520, 480)

        layout = QVBoxLayout(self)

        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.setHtml(HELP_HTML)
        layout.addWidget(browser)

        button_row = QHBoxLayout()

        docs_button = QPushButton("Full documentation")
        docs_button.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(DOCUMENTATION_URL))
        )
        button_row.addWidget(docs_button)

        issues_button = QPushButton("Report an issue")
        issues_button.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(ISSUES_URL))
        )
        button_row.addWidget(issues_button)

        button_row.addStretch(1)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        close_button.setDefault(True)
        button_row.addWidget(close_button)

        layout.addLayout(button_row)


# ============================================================================
# MAIN DIALOG
# ============================================================================

class OSMDataToolkitDialog(QDialog):
    """Main OSM Data Toolkit window."""

    def __init__(self, iface=None, parent=None):
        super().__init__(parent)

        self.iface = iface

        # Current Area of Interest.
        self.aoi = None

        # References used by the interactive rectangle map tool.
        self.rectangle_map_tool = None
        self.previous_map_tool = None

        # Background download state.
        self._download_thread = None
        self._download_worker = None
        self._download_cancel_requested = False
        self._pending_output_prefix = ""

        self._configure_window()
        self._create_widgets()
        self._create_layout()
        self._apply_stylesheet()
        self._connect_signals()
        self._set_default_values()

    # ========================================================================
    # INITIALISATION
    # ========================================================================

    def _configure_window(self):
        self.setWindowTitle(PLUGIN_NAME)
        self.setModal(False)
        self.resize(900, 860)
        self.setMinimumSize(820, 760)

        plugin_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        icon_path = os.path.join(plugin_dir, "icon.png")

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    # ========================================================================
    # STYLING
    # ========================================================================

    def _apply_stylesheet(self):
        self.setStyleSheet(
            """
            QDialog {
                background-color: #F5F8FA;
                color: #263238;
            }

            QGroupBox {
                background-color: #FFFFFF;
                border: 1px solid #D5E1E8;
                border-radius: 7px;
                margin-top: 12px;
                padding: 12px;
                color: #0B5E8E;
                font-weight: bold;
                font-size: 10pt;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding-left: 6px;
                padding-right: 6px;
                background-color: #F5F8FA;
                color: #0B5E8E;
            }

            QCheckBox, QRadioButton {
                color: #263238;
                spacing: 7px;
                padding-top: 2px;
                padding-bottom: 2px;
            }

            QCheckBox:hover, QRadioButton:hover {
                color: #1499D6;
            }

            QPushButton {
                background-color: #1499D6;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 7px 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #0B5E8E;
            }

            QPushButton:pressed {
                background-color: #084B70;
            }

            QPushButton:disabled {
                background-color: #B8C7CF;
                color: #E9EEF1;
            }

            QPushButton#help_button {
                background-color: #E7F4FB;
                color: #0B5E8E;
                border: 1px solid #A9D7EC;
            }

            QPushButton#download_button {
                background-color: #6ABF4B;
                color: #FFFFFF;
            }

            QPushButton#download_button:hover {
                background-color: #579F3D;
            }

            QPushButton#cancel_button {
                background-color: #E8ECEF;
                color: #37474F;
                border: 1px solid #CBD5DA;
            }

            QComboBox, QLineEdit, QListWidget {
                background-color: #FFFFFF;
                color: #263238;
                border: 1px solid #C7D5DD;
                border-radius: 5px;
                padding: 6px 9px;
            }

            QComboBox:hover, QLineEdit:hover, QListWidget:hover {
                border: 1px solid #1499D6;
            }

            QComboBox:focus, QLineEdit:focus, QListWidget:focus {
                border: 1px solid #1499D6;
            }

            QTextEdit {
                background-color: #FFFFFF;
                color: #263238;
                border: 1px solid #C7D5DD;
                border-radius: 5px;
                padding: 6px;
            }

            QProgressBar {
                background-color: #E8EFF3;
                color: #263238;
                border: 1px solid #C7D5DD;
                border-radius: 5px;
                text-align: center;
                min-height: 18px;
            }

            QProgressBar::chunk {
                background-color: #1499D6;
                border-radius: 4px;
            }

            QLabel {
                color: #263238;
            }
            """
        )

    # ========================================================================
    # WIDGET CREATION
    # ========================================================================

    def _create_widgets(self):
        # --- Area of Interest: Method 1 ------------------------------------
        self.current_extent_radio = QRadioButton("Current QGIS map extent")
        self.update_current_extent_button = QPushButton(
            "Update Current QGIS Map Extent"
        )
        self.update_current_extent_button.setToolTip(
            "Capture the current QGIS map canvas extent."
        )

        # --- Area of Interest: Method 2 ------------------------------------
        self.draw_rectangle_radio = QRadioButton("Draw rectangle on map")
        self.draw_aoi_button = QPushButton("Draw AOI")
        self.draw_aoi_button.setToolTip(
            "Draw a rectangle on the QGIS map to define the AOI."
        )

        # --- Area of Interest: Method 3 ------------------------------------
        self.selected_feature_radio = QRadioButton(
            "Selected feature(s) in active layer"
        )
        self.selected_features_button = QPushButton("Use Selected Features")
        self.selected_features_button.setToolTip(
            "Use selected features in the active vector layer as the AOI."
        )

        # --- Area of Interest: Method 4 ------------------------------------
        self.layer_extent_radio = QRadioButton("Active layer extent")
        self.layer_extent_button = QPushButton("Use Layer Extent")
        self.layer_extent_button.setToolTip(
            "Use the full extent of the active QGIS layer."
        )

        self.aoi_info_label = QLabel("AOI: not yet resolved")
        self.aoi_info_label.setWordWrap(True)

        # --- OSM feature categories ----------------------------------------
        self.poi_check = QCheckBox(FEATURE_LABELS["poi"])
        self.bus_stops_check = QCheckBox(FEATURE_LABELS["bus_stops"])
        self.rail_stops_check = QCheckBox(FEATURE_LABELS["rail_stops"])
        self.ferry_stops_check = QCheckBox(FEATURE_LABELS["ferry_stops"])

        self.roads_check = QCheckBox(FEATURE_LABELS["roads"])
        self.railways_check = QCheckBox(FEATURE_LABELS["railways"])
        self.waterways_check = QCheckBox(FEATURE_LABELS["waterways"])

        self.buildings_check = QCheckBox(FEATURE_LABELS["buildings"])
        self.boundaries_check = QCheckBox(FEATURE_LABELS["boundaries"])
        self.landuse_check = QCheckBox(FEATURE_LABELS["landuse"])
        self.open_public_spaces_check = QCheckBox(
            FEATURE_LABELS["open_public_spaces"]
        )

        self.select_all_button = QPushButton("Select All")
        self.clear_all_button = QPushButton("Clear All")

        # --- Output settings ------------------------------------------------
        self.output_format_combo = QComboBox()
        self.output_format_combo.addItems(["GeoPackage", "Shapefile"])

        self.output_directory_edit = QLineEdit()
        self.output_directory_edit.setPlaceholderText(
            "Select output directory..."
        )
        self.output_directory_button = QPushButton("Browse...")

        # --- Processing options --------------------------------------------
        self.auto_add_layers_check = QCheckBox(
            "Automatically add downloaded layers to QGIS"
        )
        self.cache_check = QCheckBox("Use local cache where available")

        # NOTE:
        # Raw OSM response saving has deliberately been removed.
        # Local query caching remains available through cache_check.

        # --- Status and log -------------------------------------------------
        self.status_label = QLabel("Ready.")

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setPlaceholderText(
            "Processing messages will appear here..."
        )
        self.log_output.setMinimumHeight(170)
        self.log_output.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        self.clear_log_button = QPushButton("Clear Log")
        self.clear_log_button.setToolTip(
            "Clear the messages currently shown in the Processing Log."
        )

        # --- Main action buttons -------------------------------------------
        self.help_button = QPushButton("Help")
        self.help_button.setObjectName("help_button")

        self.download_button = QPushButton("Download OSM Data")
        self.download_button.setObjectName("download_button")

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setEnabled(False)

        self.close_button = QPushButton("Close")

    # ========================================================================
    # LAYOUT
    # ========================================================================

    def _create_layout(self):
        main_layout = QVBoxLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(8, 8, 8, 8)
        content_layout.setSpacing(10)

        # --- 1. Area of Interest -------------------------------------------
        aoi_group = QGroupBox("1. Area of Interest")
        aoi_layout = QVBoxLayout()

        current_extent_layout = QHBoxLayout()
        current_extent_layout.addWidget(self.current_extent_radio)
        current_extent_layout.addStretch()
        current_extent_layout.addWidget(self.update_current_extent_button)
        aoi_layout.addLayout(current_extent_layout)

        draw_rectangle_layout = QHBoxLayout()
        draw_rectangle_layout.addWidget(self.draw_rectangle_radio)
        draw_rectangle_layout.addStretch()
        draw_rectangle_layout.addWidget(self.draw_aoi_button)
        aoi_layout.addLayout(draw_rectangle_layout)

        selected_feature_layout = QHBoxLayout()
        selected_feature_layout.addWidget(self.selected_feature_radio)
        selected_feature_layout.addStretch()
        selected_feature_layout.addWidget(self.selected_features_button)
        aoi_layout.addLayout(selected_feature_layout)

        layer_extent_layout = QHBoxLayout()
        layer_extent_layout.addWidget(self.layer_extent_radio)
        layer_extent_layout.addStretch()
        layer_extent_layout.addWidget(self.layer_extent_button)
        aoi_layout.addLayout(layer_extent_layout)

        aoi_layout.addWidget(self.aoi_info_label)
        aoi_group.setLayout(aoi_layout)
        content_layout.addWidget(aoi_group)

        # --- 2. OSM Feature Categories -------------------------------------
        feature_group = QGroupBox("2. OSM Feature Categories")
        feature_group.setMinimumHeight(180)
        feature_group.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        feature_columns_layout = QHBoxLayout()

        transport_places_group = QGroupBox("Public Transport & Places")
        transport_places_layout = QVBoxLayout()
        for checkbox in (
            self.poi_check,
            self.bus_stops_check,
            self.rail_stops_check,
            self.ferry_stops_check,
        ):
            transport_places_layout.addWidget(checkbox)
        transport_places_layout.addStretch()
        transport_places_group.setLayout(transport_places_layout)

        linear_group = QGroupBox("Linear Features")
        linear_layout = QVBoxLayout()
        for checkbox in (
            self.roads_check,
            self.railways_check,
            self.waterways_check,
        ):
            linear_layout.addWidget(checkbox)
        linear_layout.addStretch()
        linear_group.setLayout(linear_layout)

        land_built_group = QGroupBox("Land & Built Environment")
        land_built_layout = QVBoxLayout()
        for checkbox in (
            self.buildings_check,
            self.boundaries_check,
            self.landuse_check,
            self.open_public_spaces_check,
        ):
            land_built_layout.addWidget(checkbox)
        land_built_layout.addStretch()
        land_built_group.setLayout(land_built_layout)

        feature_columns_layout.addWidget(transport_places_group)
        feature_columns_layout.addWidget(linear_group)
        feature_columns_layout.addWidget(land_built_group)

        for column in range(3):
            feature_columns_layout.setStretch(column, 1)

        feature_buttons = QHBoxLayout()
        feature_buttons.addWidget(self.select_all_button)
        feature_buttons.addWidget(self.clear_all_button)
        feature_buttons.addStretch()

        feature_layout = QVBoxLayout()
        feature_layout.addLayout(feature_columns_layout)
        feature_layout.addLayout(feature_buttons)
        feature_group.setLayout(feature_layout)
        content_layout.addWidget(feature_group)

        # --- 3. Output Settings --------------------------------------------
        output_group = QGroupBox("3. Output Settings")
        output_layout = QGridLayout()

        output_layout.addWidget(QLabel("Output format:"), 0, 0)
        output_layout.addWidget(self.output_format_combo, 0, 1, 1, 2)

        output_layout.addWidget(QLabel("Output directory:"), 1, 0)
        output_layout.addWidget(self.output_directory_edit, 1, 1)
        output_layout.addWidget(self.output_directory_button, 1, 2)

        output_group.setLayout(output_layout)
        content_layout.addWidget(output_group)

        # --- 4. Processing Options -----------------------------------------
        options_group = QGroupBox("4. Processing Options")
        options_layout = QVBoxLayout()
        options_layout.addWidget(self.auto_add_layers_check)
        options_layout.addWidget(self.cache_check)
        options_group.setLayout(options_layout)
        content_layout.addWidget(options_group)

        content_layout.addStretch()

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area, 1)

        # --- Status and progress -------------------------------------------
        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("Status:"))
        status_layout.addWidget(self.status_label, 1)
        main_layout.addLayout(status_layout)

        main_layout.addWidget(self.progress_bar)

        # --- Processing log ------------------------------------------------
        log_group = QGroupBox("Processing Log")
        log_layout = QVBoxLayout()

        log_header_layout = QHBoxLayout()
        log_header_layout.addStretch()
        log_header_layout.addWidget(self.clear_log_button)

        log_layout.addLayout(log_header_layout)
        log_layout.addWidget(self.log_output)
        log_group.setLayout(log_layout)
        main_layout.addWidget(log_group, 1)

        # --- Main action buttons -------------------------------------------
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.help_button)
        button_layout.addStretch()
        button_layout.addWidget(self.download_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.close_button)
        main_layout.addLayout(button_layout)

    # ========================================================================
    # SIGNALS
    # ========================================================================

    def _connect_signals(self):
        self.select_all_button.clicked.connect(self._select_all_features)
        self.clear_all_button.clicked.connect(self._clear_all_features)

        self.output_directory_button.clicked.connect(
            self._browse_output_directory
        )
        self.help_button.clicked.connect(self._show_help)

        self.update_current_extent_button.clicked.connect(
            self._update_current_map_extent
        )
        self.draw_aoi_button.clicked.connect(
            self._start_rectangle_selection
        )
        self.selected_features_button.clicked.connect(
            self._update_selected_features_aoi
        )
        self.layer_extent_button.clicked.connect(
            self._update_layer_extent_aoi
        )

        self.download_button.clicked.connect(self._start_download)
        self.cancel_button.clicked.connect(self._cancel_download)
        self.close_button.clicked.connect(self.close)
        self.clear_log_button.clicked.connect(self._clear_processing_log)

        for radio in (
            self.current_extent_radio,
            self.draw_rectangle_radio,
            self.selected_feature_radio,
            self.layer_extent_radio,
        ):
            radio.toggled.connect(self._on_aoi_method_changed)

    # ========================================================================
    # DEFAULTS
    # ========================================================================

    def _set_default_values(self):
        self._update_aoi_button_states()

        # Initial AOI method.
        self.current_extent_radio.setChecked(True)

        # Default feature selections.
        for feature_name in ("buildings", "roads"):
            self._set_feature_checked(feature_name, True)

        self.output_format_combo.setCurrentText("GeoPackage")
        self.auto_add_layers_check.setChecked(True)
        self.cache_check.setChecked(True)

        self._log_success("OSM Data Toolkit initialised.")

        if self.iface is None:
            self._log_warning(
                "QGIS interface object was not detected. "
                "Canvas-dependent AOI tools are disabled."
            )

    # ========================================================================
    # FEATURE SELECTION
    # ========================================================================

    def _feature_checkboxes(self) -> Dict[str, QCheckBox]:
        """Return the mapping between feature keys and GUI checkboxes."""
        return {
            "poi": self.poi_check,
            "bus_stops": self.bus_stops_check,
            "rail_stops": self.rail_stops_check,
            "ferry_stops": self.ferry_stops_check,
            "roads": self.roads_check,
            "railways": self.railways_check,
            "waterways": self.waterways_check,
            "buildings": self.buildings_check,
            "boundaries": self.boundaries_check,
            "landuse": self.landuse_check,
            "open_public_spaces": self.open_public_spaces_check,
        }

    def _set_feature_checked(self, feature_name: str, checked: bool):
        checkbox = self._feature_checkboxes().get(feature_name)
        if checkbox is not None:
            checkbox.setChecked(checked)

    def _select_all_features(self):
        for checkbox in self._feature_checkboxes().values():
            checkbox.setChecked(True)
        self._log("All OSM feature categories selected.")

    def _clear_all_features(self):
        for checkbox in self._feature_checkboxes().values():
            checkbox.setChecked(False)
        self._log("All OSM feature categories cleared.")

    def get_selected_features(self) -> List[str]:
        """Return the selected GUI feature keys."""
        return [
            name
            for name, checkbox in self._feature_checkboxes().items()
            if checkbox.isChecked()
        ]

    # ========================================================================
    # AOI - GENERAL
    # ========================================================================

    def get_area_method(self) -> Optional[str]:
        if self.current_extent_radio.isChecked():
            return "current_extent"
        if self.draw_rectangle_radio.isChecked():
            return "draw_rectangle"
        if self.selected_feature_radio.isChecked():
            return "selected_feature"
        if self.layer_extent_radio.isChecked():
            return "layer_extent"
        return None

    def _aoi_action_buttons(self):
        return (
            self.update_current_extent_button,
            self.draw_aoi_button,
            self.selected_features_button,
            self.layer_extent_button,
        )

    def _update_aoi_button_states(self):
        """Enable only the AOI action button for the selected method."""
        has_iface = self.iface is not None
        method = self.get_area_method()

        self.update_current_extent_button.setEnabled(
            has_iface and method == "current_extent"
        )
        self.draw_aoi_button.setEnabled(
            has_iface and method == "draw_rectangle"
        )
        self.selected_features_button.setEnabled(
            has_iface and method == "selected_feature"
        )
        self.layer_extent_button.setEnabled(
            has_iface and method == "layer_extent"
        )

    def _on_aoi_method_changed(self, checked):
        if not checked:
            return

        if (
            self.rectangle_map_tool is not None
            and self.get_area_method() != "draw_rectangle"
        ):
            self._restore_previous_map_tool()

        self._update_aoi_button_states()
        self._update_aoi_info()

    def _show_aoi(self, title: str, aoi):
        """Show AOI coordinates and source CRS in the dialog."""
        extent = aoi.wgs84_extent

        self.aoi_info_label.setText(
            f"AOI: {title}\n"
            f"CRS: {aoi.source_crs.authid()}\n"
            f"West: {extent.xMinimum():.6f}\n"
            f"South: {extent.yMinimum():.6f}\n"
            f"East: {extent.xMaximum():.6f}\n"
            f"North: {extent.yMaximum():.6f}"
        )

    def _update_aoi_info(self):
        """Clear the previous AOI and display guidance for the chosen method."""
        method = self.get_area_method()
        self.aoi = None

        if method == "current_extent":
            self._resolve_current_map_extent()
            return

        if method == "draw_rectangle":
            self.aoi_info_label.setText(
                "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map."
            )
            return

        if method == "selected_feature":
            self.aoi_info_label.setText(
                "AOI: select feature(s) in the active QGIS layer, "
                "then click 'Use Selected Features'."
            )
            return

        if method == "layer_extent":
            self.aoi_info_label.setText(
                "AOI: click 'Use Layer Extent' to use the full extent "
                "of the active QGIS layer."
            )
            return

        self.aoi_info_label.setText("AOI: not yet resolved")

    # ========================================================================
    # AOI - METHOD 1: CURRENT QGIS MAP EXTENT
    # ========================================================================

    def _resolve_current_map_extent(self):
        """Read, validate and store the current QGIS map canvas extent."""
        if self.iface is None:
            self.aoi = None
            self.aoi_info_label.setText(
                "AOI: QGIS interface is not available."
            )
            self._log_warning(
                "Cannot resolve current map extent because QGIS is unavailable."
            )
            return

        try:
            aoi = get_current_map_extent(self.iface)
            is_valid, message = validate_aoi(aoi)

            if not is_valid:
                self.aoi = None
                self.aoi_info_label.setText(f"AOI: invalid\n{message}")
                self._log_error(f"AOI validation failed: {message}")
                return

            self.aoi = aoi
            self._show_aoi("Current QGIS map extent", aoi)
            self._log_success("Current QGIS map extent resolved.")
            self._log(aoi.description())

        except Exception as exc:
            self.aoi = None
            self.aoi_info_label.setText(f"AOI: unable to resolve\n{exc}")
            self._log_error(
                f"Failed to resolve current QGIS map extent: {exc}"
            )

    def _update_current_map_extent(self):
        """Manually capture the map extent after the user pans or zooms."""
        if not self.current_extent_radio.isChecked():
            self.current_extent_radio.setChecked(True)
            return

        self._resolve_current_map_extent()

    # ========================================================================
    # AOI - METHOD 2: DRAW RECTANGLE ON MAP
    # ========================================================================

    def _start_rectangle_selection(self):
        """Activate the interactive rectangle AOI map tool."""
        if self.iface is None:
            self._log_error(
                "Cannot draw AOI because the QGIS interface is unavailable."
            )
            self.status_label.setText("QGIS map canvas is unavailable.")
            return

        if not self.draw_rectangle_radio.isChecked():
            self.draw_rectangle_radio.setChecked(True)

        if self.rectangle_map_tool is not None:
            self._restore_previous_map_tool()

        try:
            canvas = self.iface.mapCanvas()
            if canvas is None:
                raise RuntimeError("QGIS map canvas is unavailable.")

            self.previous_map_tool = canvas.mapTool()
            self.rectangle_map_tool = RectangleAOIMapTool(canvas)

            self.rectangle_map_tool.rectangle_finished.connect(
                self._on_rectangle_drawn
            )
            self.rectangle_map_tool.deactivated.connect(
                self._on_rectangle_tool_deactivated
            )

            canvas.setMapTool(self.rectangle_map_tool)

            self.status_label.setText(
                "Draw the AOI rectangle on the QGIS map."
            )
            self.aoi_info_label.setText(
                "AOI: click and drag on the QGIS map."
            )
            self._log("Rectangle AOI drawing tool activated.")

        except Exception as exc:
            self.rectangle_map_tool = None
            self.previous_map_tool = None
            self._log_error(f"Failed to activate rectangle AOI tool: {exc}")
            self.status_label.setText(f"Unable to start AOI drawing: {exc}")

    def _on_rectangle_drawn(self, geometry):
        """Convert the drawn rectangle into the standard AOI object."""
        try:
            canvas = self.iface.mapCanvas()
            source_crs = canvas.mapSettings().destinationCrs()

            aoi = create_drawn_rectangle_aoi(geometry, source_crs)
            is_valid, message = validate_aoi(aoi)

            if not is_valid:
                self.aoi = None
                self.aoi_info_label.setText(f"AOI: invalid\n{message}")
                self._log_error(f"Drawn AOI validation failed: {message}")
                return

            self.aoi = aoi
            self._show_aoi("Drawn rectangle", aoi)

            self.status_label.setText("AOI rectangle captured successfully.")
            self._log_success("Drawn rectangle AOI captured successfully.")
            self._log(aoi.description())

        except Exception as exc:
            self.aoi = None
            self.aoi_info_label.setText(f"AOI: unable to create\n{exc}")
            self.status_label.setText("Failed to create AOI.")
            self._log_error(f"Failed to process drawn rectangle AOI: {exc}")

        finally:
            self._restore_previous_map_tool()

    def _on_rectangle_tool_deactivated(self):
        """Handle a drawing tool deactivation initiated outside this dialog."""
        tool = self.rectangle_map_tool
        if tool is None:
            return

        self.rectangle_map_tool = None
        self.previous_map_tool = None

        try:
            tool.clear()
        except Exception:
            pass

        self.status_label.setText("AOI drawing cancelled.")

        if self.aoi is None and self.get_area_method() == "draw_rectangle":
            self.aoi_info_label.setText(
                "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map."
            )

        self._log_warning("Rectangle AOI drawing was cancelled.")

    def _restore_previous_map_tool(self):
        """Restore the QGIS map tool active before rectangle drawing."""
        tool = self.rectangle_map_tool
        previous = self.previous_map_tool

        # Clear references first so deactivation does not trigger a second
        # cancellation of the same drawing session.
        self.rectangle_map_tool = None
        self.previous_map_tool = None

        if tool is None:
            return

        try:
            tool.clear()

            if self.iface is None:
                return

            canvas = self.iface.mapCanvas()
            if canvas is None or canvas.mapTool() is not tool:
                return

            if previous is not None and previous is not tool:
                canvas.setMapTool(previous)
            else:
                canvas.unsetMapTool(tool)

        except Exception as exc:
            self._log_warning(
                f"Could not restore previous QGIS map tool: {exc}"
            )

    # ========================================================================
    # AOI - METHOD 3: SELECTED FEATURES IN ACTIVE LAYER
    # ========================================================================

    def _update_selected_features_aoi(self):
        """Use the selected features of the active vector layer as the AOI."""
        if not self.selected_feature_radio.isChecked():
            self.selected_feature_radio.setChecked(True)

        if self.iface is None:
            self.aoi = None
            self.aoi_info_label.setText(
                "AOI: QGIS interface is not available."
            )
            self._log_error(
                "Cannot resolve selected-feature AOI because QGIS is unavailable."
            )
            return

        try:
            layer = self.iface.activeLayer()

            if layer is None:
                self.aoi = None
                self.aoi_info_label.setText("AOI: no active QGIS layer.")
                self._log_warning("No active QGIS layer is available.")
                return

            if not isinstance(layer, QgsVectorLayer):
                self.aoi = None
                self.aoi_info_label.setText(
                    "AOI: the active layer is not a vector layer."
                )
                self.status_label.setText(
                    "Select a vector layer with selected features."
                )
                self._log_warning(
                    "Selected-feature AOI requires a vector layer."
                )
                return

            selected_count = layer.selectedFeatureCount()
            if selected_count == 0:
                self.aoi = None
                self.aoi_info_label.setText(
                    "AOI: no feature(s) selected in the active layer."
                )
                self.status_label.setText(
                    "Select one or more features in the active layer."
                )
                self._log_warning("No selected features found.")
                return

            aoi = create_selected_features_aoi(layer)
            is_valid, message = validate_aoi(aoi)

            if not is_valid:
                self.aoi = None
                self.aoi_info_label.setText(f"AOI: invalid\n{message}")
                self.status_label.setText(
                    "Selected-feature AOI is invalid."
                )
                self._log_error(
                    f"Selected-feature AOI validation failed: {message}"
                )
                return

            self.aoi = aoi
            self._show_aoi(f"Selected features ({selected_count})", aoi)

            self.status_label.setText(
                f"Selected-feature AOI captured successfully "
                f"({selected_count} feature(s))."
            )
            self._log_success("Selected-feature AOI captured successfully.")
            self._log(aoi.description())

        except Exception as exc:
            self.aoi = None
            self.aoi_info_label.setText(
                f"AOI: failed to resolve selected features\n{exc}"
            )
            self.status_label.setText(
                "Failed to resolve selected-feature AOI."
            )
            self._log_error(
                f"Failed to resolve selected-feature AOI: {exc}"
            )

    # ========================================================================
    # AOI - METHOD 4: ACTIVE LAYER EXTENT
    # ========================================================================

    def _update_layer_extent_aoi(self):
        """Use the full extent of the active QGIS layer as the AOI."""
        if not self.layer_extent_radio.isChecked():
            self.layer_extent_radio.setChecked(True)

        if self.iface is None:
            self.aoi = None
            self.aoi_info_label.setText(
                "AOI: QGIS interface is not available."
            )
            self._log_error(
                "Cannot resolve active-layer extent because QGIS is unavailable."
            )
            return

        try:
            layer = self.iface.activeLayer()

            if layer is None:
                self.aoi = None
                self.aoi_info_label.setText("AOI: no active QGIS layer.")
                self.status_label.setText("Select an active QGIS layer.")
                self._log_warning("No active QGIS layer is available.")
                return

            aoi = create_active_layer_extent_aoi(layer)
            is_valid, message = validate_aoi(aoi)

            if not is_valid:
                self.aoi = None
                self.aoi_info_label.setText(f"AOI: invalid\n{message}")
                self.status_label.setText(
                    "Active-layer extent AOI is invalid."
                )
                self._log_error(
                    f"Active-layer extent validation failed: {message}"
                )
                return

            self.aoi = aoi
            self._show_aoi("Active layer extent", aoi)

            self.status_label.setText(
                "Active-layer extent captured successfully."
            )
            self._log_success("Active-layer extent captured successfully.")
            self._log(aoi.description())

        except Exception as exc:
            self.aoi = None
            self.aoi_info_label.setText(
                f"AOI: failed to resolve active layer extent\n{exc}"
            )
            self.status_label.setText(
                "Failed to resolve active-layer extent."
            )
            self._log_error(
                f"Failed to resolve active-layer extent: {exc}"
            )

    # ========================================================================
    # OUTPUT DIRECTORY
    # ========================================================================

    def _browse_output_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory",
        )

        if directory:
            self.output_directory_edit.setText(directory)
            self._log_success(f"Output directory selected: {directory}")

    # ========================================================================
    # DOWNLOAD - FEATURE ID MAPPING
    # ========================================================================

    def _selected_overpass_feature_ids(self) -> List[str]:
        """
        Translate GUI feature keys into IDs used by the core query builder.

        The Waterways checkbox requests both water_lines and water_polygons.
        """
        gui_to_core_ids = {
            "poi": ["poi"],
            "bus_stops": ["bus_stops"],
            "rail_stops": ["rail_stops"],
            "ferry_stops": ["ferry_stops"],
            "roads": ["roads"],
            "railways": ["railways"],
            "waterways": ["water_lines", "water_polygons"],
            "buildings": ["buildings"],
            "boundaries": ["administrative_boundaries"],
            "landuse": ["landuse"],
            "open_public_spaces": ["open_public_spaces"],
        }

        selected_ids = []
        for gui_key in self.get_selected_features():
            selected_ids.extend(gui_to_core_ids.get(gui_key, []))

        return list(dict.fromkeys(selected_ids))

    # ========================================================================
    # DOWNLOAD - VALIDATION, QUERY AND BACKGROUND WORKER
    # ========================================================================

    def _start_download(self):
        """Validate inputs and start the background Overpass download."""
        if self._download_thread is not None:
            self._log_warning("A download is already running.")
            return

        if self.aoi is None:
            self._show_error(
                "No valid Area of Interest is available. Select an AOI "
                "method and resolve the AOI before downloading."
            )
            return

        is_valid, message = validate_aoi(self.aoi)
        if not is_valid:
            self._show_error(f"The current AOI is invalid: {message}")
            return

        selected_feature_ids = self._selected_overpass_feature_ids()
        if not selected_feature_ids:
            self._show_error(
                "Select at least one OSM feature category before downloading."
            )
            return

        output_directory = self.output_directory_edit.text().strip()
        if not output_directory:
            self._show_error(
                "Choose an output directory before downloading."
            )
            return

        if not os.path.isdir(output_directory):
            self._show_error(
                "The selected output directory does not exist. "
                "Choose an existing folder."
            )
            return

        # Get and validate the filename before making the network request.
        output_format = self.output_format_combo.currentText()
        naming_dialog = OutputNamingDialog(output_format, self)

        if _exec_dialog(naming_dialog) != QDialog.DialogCode.Accepted:
            self.status_label.setText("Download cancelled before it started.")
            self._log_warning(
                "Download cancelled in the output-naming dialog."
            )
            return

        output_prefix = naming_dialog.output_prefix()
        if not output_prefix:
            self._show_error(
                "The output name is empty after filename validation."
            )
            return

        # Check only the expected final output files for conflicts.
        if output_format == "GeoPackage":
            expected_path = os.path.join(
                output_directory,
                f"{output_prefix}.gpkg",
            )
            existing_outputs = (
                [expected_path] if os.path.exists(expected_path) else []
            )
        else:
            existing_outputs = glob.glob(
                os.path.join(output_directory, f"{output_prefix}_*.shp")
            )

        # There is deliberately no raw JSON output or raw JSON overwrite check.

        if existing_outputs:
            answer = QMessageBox.question(
                self,
                f"{PLUGIN_NAME} — Confirm Overwrite",
                "One or more output files with this name already exist. "
                "Do you want to overwrite the matching output files?\n\n"
                + "\n".join(
                    os.path.basename(path)
                    for path in existing_outputs[:8]
                )
                + ("\n…" if len(existing_outputs) > 8 else ""),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if answer != QMessageBox.StandardButton.Yes:
                self.status_label.setText(
                    "Download cancelled; existing files preserved."
                )
                self._log_warning(
                    "Download cancelled because existing output files "
                    "were not approved for overwrite."
                )
                return

        self._pending_output_prefix = output_prefix

        # Overpass expects the bounding box in south, west, north, east order.
        try:
            extent = self.aoi.wgs84_extent
            south = float(extent.yMinimum())
            west = float(extent.xMinimum())
            north = float(extent.yMaximum())
            east = float(extent.xMaximum())

            admin_levels = naming_dialog.selected_admin_levels()
            self._pending_admin_levels = admin_levels
            query = build_overpass_query(
                feature_ids=selected_feature_ids,
                south=south,
                west=west,
                north=north,
                east=east,
                admin_levels=admin_levels,
            )

        except Exception as exc:
            self._show_error(f"Could not prepare the Overpass query: {exc}")
            return

        self._download_cancel_requested = False
        self.progress_bar.setRange(0, 0)
        self.status_label.setText("Preparing Overpass download...")

        self._log("Preparing Overpass query.")
        self._log(
            f"Selected feature IDs: {', '.join(selected_feature_ids)}"
        )
        if "administrative_boundaries" in selected_feature_ids:
            if admin_levels is None:
                self._log("Administrative boundary filter: all levels (no admin_level filter).")
            else:
                self._log(
                    "Administrative boundary levels: "
                    + ", ".join(map(str, admin_levels))
                )
        self._log(
            "WGS84 AOI bbox: "
            f"south={south:.6f}, west={west:.6f}, "
            f"north={north:.6f}, east={east:.6f}"
        )
        self._log(f"Generated Overpass query ({len(query)} characters).")

        # The worker handles the network request and optional local cache.
        thread = QThread(self)

        cache_directory = os.path.join(
            QgsApplication.qgisSettingsDirPath(),
            "osm_data_toolkit",
            "cache",
        )

        worker = OverpassDownloadWorker(
            query,
            use_cache=self.cache_check.isChecked(),
            cache_dir=cache_directory,
        )
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.started.connect(self._on_download_started)
        worker.status.connect(self._on_download_status)
        worker.finished.connect(self._on_download_success)
        worker.error.connect(self._on_download_error)
        worker.cancelled.connect(self._on_download_cancelled)

        worker.completed.connect(thread.quit)
        worker.completed.connect(worker.deleteLater)
        thread.finished.connect(self._on_download_thread_finished)

        self._download_thread = thread
        self._download_worker = worker

        self._set_busy(True)
        self.status_label.setText("Downloading OSM data from Overpass...")
        self._log("Background Overpass download started.")

        thread.start()

    def _on_download_started(self):
        self.status_label.setText("Overpass download running...")

    def _on_download_status(self, message: str):
        self._log(message)
        self.status_label.setText(message)

    # ========================================================================
    # DOWNLOAD - SUCCESS AND EXPORT
    # ========================================================================

    def _on_download_success(self, response: dict):
        """Export the downloaded response and optionally load its layers."""
        elements = (
            response.get("elements", [])
            if isinstance(response, dict)
            else []
        )

        counts = {"node": 0, "way": 0, "relation": 0}
        for element in elements:
            if isinstance(element, dict):
                element_type = element.get("type")
                if element_type in counts:
                    counts[element_type] += 1

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(25)

        self._log_success(
            "Overpass response received successfully: "
            f"{len(elements):,} elements "
            f"({counts['node']:,} nodes, {counts['way']:,} ways, "
            f"{counts['relation']:,} relations)."
        )

        output_directory = self.output_directory_edit.text().strip()
        output_format = self.output_format_combo.currentText()
        output_prefix = getattr(self, "_pending_output_prefix", "")

        if not output_prefix:
            self.progress_bar.setValue(0)
            self.status_label.setText(
                "Export cancelled: output name is missing."
            )
            self._log_error(
                "The download completed, but no confirmed output name "
                "was available."
            )
            return

        # No separate raw-response JSON file is written here.
        # The cache remains managed by OverpassDownloadWorker.

        try:
            selected_ids = self._selected_overpass_feature_ids()
            self.progress_bar.setValue(40)

            if output_format == "GeoPackage":
                output_path = os.path.join(
                    output_directory,
                    f"{output_prefix}.gpkg",
                )

                self.status_label.setText(
                    "Converting OSM response to GeoPackage..."
                )
                self._log(
                    "Classifying OSM elements and preparing GeoPackage layers."
                )

                export_result = export_overpass_response_to_gpkg(
                    response=response,
                    selected_feature_ids=selected_ids,
                    output_path=output_path,
                    progress_callback=lambda message: self._log(message),
                )

                self._log_success(
                    f"GeoPackage saved: {export_result['path']} "
                    f"({export_result['total_features']:,} feature records)."
                )

                if self.auto_add_layers_check.isChecked():
                    loaded_layers = load_gpkg_layers(
                        export_result["path"],
                        export_result["layers"],
                    )
                    self._log_success(
                        f"Added {len(loaded_layers)} GeoPackage layer(s) to QGIS."
                    )

            elif output_format == "Shapefile":
                self.status_label.setText(
                    "Converting OSM response to Shapefiles..."
                )
                self._log(
                    "Classifying OSM elements and preparing Shapefile outputs."
                )

                export_result = export_overpass_response_to_shapefile(
                    response=response,
                    selected_feature_ids=selected_ids,
                    output_directory=output_directory,
                    output_prefix=output_prefix,
                    progress_callback=lambda message: self._log(message),
                    admin_levels=getattr(self, "_pending_admin_levels", None),
                )

                self._log_success(
                    f"Shapefile export completed in: {export_result['path']} "
                    f"({export_result['total_features']:,} feature records)."
                )

                for shapefile_path in export_result["paths"]:
                    self._log(f"  • {os.path.basename(shapefile_path)}")

                if self.auto_add_layers_check.isChecked():
                    loaded_layers = load_shapefile_layers(
                        export_result["paths"]
                    )
                    self._log_success(
                        f"Added {len(loaded_layers)} Shapefile layer(s) to QGIS."
                    )

            else:
                raise ValueError(
                    f"Unsupported output format: {output_format}"
                )

            # Report exported feature counts.
            for layer_name, feature_count in export_result["counts"].items():
                self._log_feature_count(
                    f"• {layer_name}: {feature_count:,} features"
                )

            # Report shortened Shapefile field names, if any.
            for layer_name, mapping in export_result.get(
                "field_name_maps", {}
            ).items():
                self._log_warning(
                    f"Shapefile field names shortened for {layer_name}: "
                    + ", ".join(
                        f"{old} → {new}"
                        for old, new in mapping.items()
                    )
                )

            skipped = export_result.get("skipped", {})

            if skipped.get("unsupported_relation", 0):
                self._log_warning(
                    f"Skipped {skipped['unsupported_relation']:,} "
                    "relation geometry assignment(s); relation-member "
                    "geometry assembly is not implemented yet."
                )

            if skipped.get("unclassified", 0):
                self._log(
                    "Unclassified OSM elements not written to feature layers: "
                    f"{skipped['unclassified']:,}."
                )

            # Mark the export as successful before attempting cleanup.
            self.progress_bar.setValue(100)
            self.status_label.setText(
                f"Export complete: "
                f"{export_result['total_features']:,} features written."
            )

            self._log_success("OSM export completed successfully.")

            # Cleanup is deliberately called only after export succeeds.
            # A cleanup failure must not turn a successful export into failure.
            self._delete_temporary_gpkg_files(output_directory)

        except Exception as exc:
            self.progress_bar.setValue(0)
            self.status_label.setText(
                "Download succeeded, but export failed."
            )
            self._log_error(f"{output_format} export failed: {exc}")

            QMessageBox.critical(
                self,
                f"{PLUGIN_NAME} — Export Error",
                "The OSM download succeeded, but the output could not be created."
                f"\n\nDetails: {exc}",
            )

    # ========================================================================
    # TEMPORARY WORKSPACE CLEANUP
    # ========================================================================

    def _delete_temporary_gpkg_files(self, workspace_directory: str):
        """
        Delete only temporary GeoPackages matching the required filename pattern.

        Target pattern:
            <workspace_directory>/.osm_toolkit_temp_*.gpkg

        This method does not create temporary files and does not inspect or
        delete other GeoPackages, final outputs, or cache files.

        Cleanup is called after a successful export. Deletion errors are
        logged as warnings and do not raise an exception to the export handler.
        """
        if not workspace_directory or not os.path.isdir(workspace_directory):
            self._log_warning(
                "Temporary-file cleanup skipped: workspace directory is invalid."
            )
            return

        pattern = os.path.join(
            workspace_directory,
            ".osm_toolkit_temp_*.gpkg",
        )

        try:
            temporary_files = glob.glob(pattern)
        except OSError as exc:
            self._log_warning(
                f"Could not search for temporary GeoPackages: {exc}"
            )
            return

        deleted_count = 0
        failed_count = 0

        for file_path in temporary_files:
            try:
                # Do not target directories, and do not expand the search
                # beyond the selected workspace directory.
                if not os.path.isfile(file_path):
                    continue

                os.remove(file_path)
                deleted_count += 1

                self._log(
                    "Deleted temporary workspace file: "
                    f"{os.path.basename(file_path)}",
                    "info",
                )

            except OSError as exc:
                failed_count += 1
                self._log_warning(
                    f"Could not delete temporary file "
                    f"{os.path.basename(file_path)}: {exc}"
                )

        if deleted_count:
            self._log_success(
                "Temporary workspace cleanup complete: "
                f"{deleted_count} file(s) deleted."
            )
        elif not temporary_files:
            self._log(
                "Temporary workspace cleanup complete: "
                "no matching files found."
            )

        if failed_count:
            self._log_warning(
                f"{failed_count} temporary file(s) could not be deleted. "
                "They may still be in use by QGIS or another process."
            )

    # ========================================================================
    # DOWNLOAD - ERROR, CANCELLATION AND THREAD CLEANUP
    # ========================================================================

    def _on_download_error(self, message: str):
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.status_label.setText("Overpass download failed.")
        self._log_error(f"Overpass download failed: {message}")

    def _on_download_cancelled(self):
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.status_label.setText("Download cancelled.")
        self._log_warning("Overpass download cancelled.")

    def _cancel_download(self):
        """Request cooperative cancellation of the background worker."""
        worker = self._download_worker

        if worker is None:
            self._log_warning("There is no active download to cancel.")
            return

        if self._download_cancel_requested:
            self._log_warning("Cancellation has already been requested.")
            return

        self._download_cancel_requested = True
        worker.request_cancel()
        self.cancel_button.setEnabled(False)

        self.status_label.setText(
            "Cancellation requested; waiting for the current request to finish..."
        )
        self._log_warning(
            "Cancellation requested. If an HTTP request is already active, "
            "the downloader will stop when that request returns or times out."
        )

    def _on_download_thread_finished(self):
        """Restore the GUI once the background thread has stopped."""
        thread = self._download_thread

        self._download_thread = None
        self._download_worker = None
        self._download_cancel_requested = False

        self._set_busy(False)

        if (
            self.progress_bar.minimum() == 0
            and self.progress_bar.maximum() == 0
        ):
            self.progress_bar.setRange(0, 100)
            self.progress_bar.setValue(0)

        if self.status_label.text().startswith("Cancellation requested"):
            self.status_label.setText("Download stopped.")

        if thread is not None:
            thread.deleteLater()

    # ========================================================================
    # GUI BUSY STATE
    # ========================================================================

    def _set_busy(self, busy: bool):
        """Enable or disable controls while a download is running."""
        self.download_button.setEnabled(not busy)
        self.cancel_button.setEnabled(busy)
        self.close_button.setEnabled(not busy)
        self.select_all_button.setEnabled(not busy)
        self.clear_all_button.setEnabled(not busy)

        controls = (
            self.output_format_combo,
            self.output_directory_edit,
            self.output_directory_button,
            *self._feature_checkboxes().values(),
            self.current_extent_radio,
            self.draw_rectangle_radio,
            self.selected_feature_radio,
            self.layer_extent_radio,
            self.auto_add_layers_check,
            self.cache_check,
        )

        for widget in controls:
            widget.setEnabled(not busy)

        if busy:
            for button in self._aoi_action_buttons():
                button.setEnabled(False)
        else:
            self._update_aoi_button_states()

    # ========================================================================
    # HELP
    # ========================================================================

    def _show_help(self):
        """Open the in-plugin help with links to the online documentation."""
        _exec_dialog(HelpDialog(self))

    # ========================================================================
    # LOGGING AND MESSAGES
    # ========================================================================

    def _clear_processing_log(self):
        """Clear only the visible log, without changing processing settings."""
        self.log_output.clear()

    def _log(self, message: str, level: str = "info"):
        """Append a timestamped message using the requested log colour."""
        color = LOG_COLORS.get(level, LOG_COLORS["info"])
        timestamp = datetime.now().strftime("%H:%M:%S")
        safe_text = html.escape(f"[{timestamp}] {message}")

        self.log_output.append(
            f'<span style="color:{color};">{safe_text}</span>'
        )

    def _log_feature_count(self, message: str):
        """Append an exported feature count in bold green text."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        safe_text = html.escape(f"[{timestamp}] {message}")

        self.log_output.append(
            '<span style="color:#2E9E2E; font-weight:600;">'
            f"{safe_text}</span>"
        )

    def _log_success(self, message: str):
        self._log(message, "success")

    def _log_warning(self, message: str):
        self._log(message, "warning")

    def _log_error(self, message: str):
        self._log(message, "error")

    def _show_error(self, message: str):
        self._log_error("ERROR: " + str(message))
        QMessageBox.warning(self, PLUGIN_NAME, str(message))

    # ========================================================================
    # WINDOW EVENTS AND RESET
    # ========================================================================

    def _reset_dialog_to_initial_state(self):
        """Restore default GUI settings when the dialog closes."""
        self.output_directory_edit.clear()
        self.output_format_combo.setCurrentText("GeoPackage")

        self.auto_add_layers_check.setChecked(True)
        self.cache_check.setChecked(True)

        # Restore Buildings and Roads as the only selected categories.
        for feature_name, checkbox in self._feature_checkboxes().items():
            checkbox.setChecked(
                feature_name in ("buildings", "roads")
            )

        # Return to the first AOI method and recapture the current map extent.
        self.aoi = None
        self.current_extent_radio.setChecked(True)

        if self.iface is not None:
            self._update_current_map_extent()
        else:
            self.aoi_info_label.setText("AOI: not yet resolved")

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.status_label.setText("Ready.")

        self._pending_output_prefix = ""
        self.log_output.clear()
        self._log_success("OSM Data Toolkit initialised.")

    def closeEvent(self, event):
        """Restore the map tool and reset state before hiding the dialog."""
        if (
            self._download_thread is not None
            and self._download_thread.isRunning()
        ):
            event.ignore()
            self._log_warning(
                "The dialog cannot close while a download thread is running. "
                "Cancellation has been requested; close the dialog after it stops."
            )
            self._cancel_download()
            return

        if self.rectangle_map_tool is not None:
            self._restore_previous_map_tool()

        self._reset_dialog_to_initial_state()
        super().closeEvent(event)


# ============================================================================
# END OF MODULE
# ============================================================================