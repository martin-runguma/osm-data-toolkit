"""
OSM Data Toolkit - Visual theme
===============================

Central place for the plugin's look and feel.

The design follows the clean "public data portal" style of the NHIS
Portal (https://nhis.org.na): a bright sky-blue brand colour, white
cards on a soft grey-blue canvas, generous rounded corners, quiet
borders, and one strong call-to-action button.

Everything visual lives here (colours, fonts and the Qt style sheet) so
that the dialogs only need to apply ``STYLESHEET`` and set a few object
names / dynamic properties. Nothing in this module touches plugin logic.

Works unchanged on Qt5 (QGIS 3.x) and Qt6 (QGIS 4).
"""

from __future__ import annotations

import os

# ============================================================================
# PALETTE
# ============================================================================

PRIMARY = "#0A97D9"          # NHIS brand blue (site theme colour)
PRIMARY_DARK = "#0877AD"
PRIMARY_DEEPER = "#065B86"
PRIMARY_SOFT = "#E6F5FC"
PRIMARY_BORDER = "#B9E2F5"

INK = "#0F2A3D"              # headings
TEXT = "#33485A"             # body text
MUTED = "#6B8090"            # captions and hints
BORDER = "#DCE6EC"
BORDER_STRONG = "#CBD9E2"
CANVAS = "#F3F7FA"          # dialog background
SURFACE = "#FFFFFF"          # cards

SUCCESS = "#1B8A4B"
WARNING = "#B26A00"
DANGER = "#C62828"

FONT_STACK = (
    '"Inter", "Segoe UI", "SF Pro Text", "Helvetica Neue", '
    "Arial, sans-serif"
)
MONO_STACK = (
    '"Cascadia Mono", "Consolas", "Menlo", "DejaVu Sans Mono", monospace'
)

# Colours used by the processing log (light background).
LOG_COLORS = {
    "info": TEXT,
    "success": SUCCESS,
    "warning": WARNING,
    "error": DANGER,
}


# ============================================================================
# RESOURCES
# ============================================================================

_RESOURCE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "resources"
)


def resource_path(name: str) -> str:
    """Return a forward-slash path usable inside ``url("...")`` in QSS."""
    return os.path.join(_RESOURCE_DIR, name).replace("\\", "/")


# ============================================================================
# STYLE SHEET
# ============================================================================

_QSS_TEMPLATE = """
/* ---------- Base ---------- */
QDialog {
    background-color: @CANVAS@;
}

QWidget {
    font-family: @FONT@;
    font-size: 10pt;
    color: @TEXT@;
}

QLabel {
    background: transparent;
}

QToolTip {
    background-color: @INK@;
    color: #FFFFFF;
    border: none;
    padding: 5px 8px;
}

/* ---------- Header banner ---------- */
QFrame#header {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 @PRIMARY@, stop:1 #0670A3);
    border: none;
}

QFrame#header QLabel {
    background: transparent;
}

QLabel#logoTile {
    background-color: #FFFFFF;
    border-radius: 12px;
}

QLabel#headerTitle {
    color: #FFFFFF;
    font-size: 17pt;
    font-weight: 700;
}

QLabel#headerSubtitle {
    color: #D8F1FC;
    font-size: 10pt;
}

QLabel#headerPill {
    color: #FFFFFF;
    background-color: rgba(255, 255, 255, 46);
    border: 1px solid rgba(255, 255, 255, 90);
    border-radius: 10px;
    padding: 2px 10px;
    font-size: 8pt;
    font-weight: 600;
}

QFrame#header QPushButton {
    background-color: rgba(255, 255, 255, 40);
    color: #FFFFFF;
    border: 1px solid rgba(255, 255, 255, 110);
    border-radius: 8px;
    padding: 7px 18px;
    font-weight: 600;
}

QFrame#header QPushButton:hover {
    background-color: rgba(255, 255, 255, 80);
}

/* ---------- Scroll area ---------- */
QScrollArea {
    background: transparent;
    border: none;
}

QWidget#scrollContent {
    background-color: @CANVAS@;
}

QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: #C3D3DD;
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: #9FB8C8;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: transparent;
}

QScrollBar:horizontal {
    background: transparent;
    height: 10px;
    margin: 2px;
}

QScrollBar::handle:horizontal {
    background: #C3D3DD;
    border-radius: 4px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: #9FB8C8;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: transparent;
}

/* ---------- Cards ---------- */
QFrame#card {
    background-color: @SURFACE@;
    border: 1px solid @BORDER@;
    border-radius: 12px;
}

QLabel#stepBadge {
    background-color: @PRIMARY@;
    color: #FFFFFF;
    border-radius: 14px;
    font-weight: 700;
    font-size: 10pt;
}

QLabel#cardTitle {
    color: @INK@;
    font-size: 12pt;
    font-weight: 700;
}

QLabel#cardHint {
    color: @MUTED@;
    font-size: 9pt;
}

QFrame#divider {
    background-color: @BORDER@;
    border: none;
    min-height: 1px;
    max-height: 1px;
}

QLabel#sectionLabel {
    color: @MUTED@;
    font-size: 8pt;
    font-weight: 700;
}

QLabel#fieldLabel {
    color: @INK@;
    font-weight: 600;
}

QLabel#countPill {
    background-color: @PRIMARY_SOFT@;
    color: @PRIMARY_DEEPER@;
    border: 1px solid @PRIMARY_BORDER@;
    border-radius: 10px;
    padding: 2px 10px;
    font-size: 9pt;
    font-weight: 600;
}

/* ---------- AOI option rows ---------- */
QFrame#optionRow {
    background-color: #F8FBFD;
    border: 1px solid @BORDER@;
    border-radius: 10px;
}

QFrame#optionRow:hover {
    border: 1px solid @PRIMARY_BORDER@;
}

QFrame#optionRow[active="true"] {
    background-color: @PRIMARY_SOFT@;
    border: 1px solid @PRIMARY@;
}

QLabel#infoPanel {
    background-color: #F8FBFD;
    border: 1px solid @BORDER@;
    border-left: 4px solid @PRIMARY@;
    border-radius: 8px;
    padding: 10px 12px;
    font-family: @MONO@;
    font-size: 9pt;
    color: @INK@;
}

/* ---------- Check boxes and radio buttons ---------- */
QCheckBox, QRadioButton {
    spacing: 9px;
    padding: 3px 0px;
    color: @TEXT@;
}

QCheckBox:hover, QRadioButton:hover {
    color: @PRIMARY_DARK@;
}

QCheckBox:disabled, QRadioButton:disabled {
    color: #9AAAB6;
}

QRadioButton:checked {
    color: @PRIMARY_DEEPER@;
    font-weight: 600;
}

QCheckBox::indicator {
    width: 14px;
    height: 14px;
    border: 1px solid #9DB3C1;
    border-radius: 4px;
    background-color: #FFFFFF;
}

QCheckBox::indicator:hover {
    border: 1px solid @PRIMARY@;
}

QCheckBox::indicator:checked {
    background-color: @PRIMARY@;
    border: 1px solid @PRIMARY@;
    image: url("@CHECK@");
}

QCheckBox::indicator:disabled {
    background-color: #EEF3F6;
    border: 1px solid #D5DFE6;
}

QCheckBox::indicator:checked:disabled {
    background-color: #9CCFE8;
    border: 1px solid #9CCFE8;
}

QRadioButton::indicator {
    width: 14px;
    height: 14px;
    border: 1px solid #9DB3C1;
    border-radius: 8px;
    background-color: #FFFFFF;
}

QRadioButton::indicator:hover {
    border: 1px solid @PRIMARY@;
}

QRadioButton::indicator:checked {
    border: 1px solid @PRIMARY@;
    background: qradialgradient(cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,
                                stop:0 @PRIMARY@, stop:0.45 @PRIMARY@,
                                stop:0.55 #FFFFFF, stop:1 #FFFFFF);
}

/* Category "chips" */
QCheckBox[chip="true"] {
    background-color: #FFFFFF;
    border: 1px solid @BORDER_STRONG@;
    border-radius: 9px;
    padding: 8px 12px;
}

QCheckBox[chip="true"]:hover {
    border: 1px solid @PRIMARY@;
    background-color: #F5FBFE;
}

QCheckBox[chip="true"]:checked {
    background-color: @PRIMARY_SOFT@;
    border: 1px solid @PRIMARY@;
    color: @PRIMARY_DEEPER@;
    font-weight: 600;
}

QCheckBox[chip="true"]:disabled {
    background-color: #F3F6F8;
    border: 1px solid #E3EAEF;
}

/* ---------- Buttons ---------- */
QPushButton {
    background-color: #FFFFFF;
    color: @PRIMARY_DARK@;
    border: 1px solid @PRIMARY_BORDER@;
    border-radius: 8px;
    padding: 7px 16px;
    font-weight: 600;
}

QPushButton:hover {
    background-color: @PRIMARY_SOFT@;
    border: 1px solid @PRIMARY@;
}

QPushButton:pressed {
    background-color: #CFEBF8;
}

QPushButton:disabled {
    background-color: #F1F5F8;
    color: #A9B8C3;
    border: 1px solid #E3EAEF;
}

QPushButton[variant="primary"] {
    background-color: @PRIMARY@;
    color: #FFFFFF;
    border: 1px solid @PRIMARY@;
    padding: 9px 24px;
    font-weight: 700;
}

QPushButton[variant="primary"]:hover {
    background-color: @PRIMARY_DARK@;
    border: 1px solid @PRIMARY_DARK@;
}

QPushButton[variant="primary"]:pressed {
    background-color: @PRIMARY_DEEPER@;
    border: 1px solid @PRIMARY_DEEPER@;
}

QPushButton[variant="primary"]:disabled {
    background-color: #A9D9EF;
    color: #F4FAFD;
    border: 1px solid #A9D9EF;
}

QPushButton[variant="ghost"] {
    background-color: transparent;
    color: @TEXT@;
    border: 1px solid transparent;
}

QPushButton[variant="ghost"]:hover {
    background-color: #EAF1F5;
    border: 1px solid transparent;
}

QPushButton[variant="ghost"]:disabled {
    background-color: transparent;
    color: #A9B8C3;
    border: 1px solid transparent;
}

QPushButton[variant="danger"] {
    background-color: #FFFFFF;
    color: @TEXT@;
    border: 1px solid @BORDER_STRONG@;
}

QPushButton[variant="danger"]:enabled:hover {
    background-color: #FDECEC;
    color: @DANGER@;
    border: 1px solid #F0B4B4;
}

QPushButton[variant="link"] {
    background-color: transparent;
    color: @PRIMARY_DARK@;
    border: none;
    padding: 4px 8px;
}

QPushButton[variant="link"]:hover {
    background-color: transparent;
    color: @PRIMARY_DEEPER@;
    text-decoration: underline;
}

QPushButton[variant="link"]:disabled {
    background-color: transparent;
    color: #A9B8C3;
    border: none;
}

/* ---------- Inputs ---------- */
QLineEdit, QComboBox {
    background-color: #FFFFFF;
    color: @INK@;
    border: 1px solid @BORDER_STRONG@;
    border-radius: 8px;
    padding: 7px 10px;
    selection-background-color: @PRIMARY@;
    selection-color: #FFFFFF;
}

QLineEdit:hover, QComboBox:hover {
    border: 1px solid @PRIMARY_BORDER@;
}

QLineEdit:focus, QComboBox:focus, QComboBox:on {
    border: 1px solid @PRIMARY@;
}

QLineEdit:disabled, QComboBox:disabled {
    background-color: #F3F6F8;
    color: #9AAAB6;
}

QComboBox {
    padding-right: 30px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: center right;
    width: 28px;
    border: none;
}

QComboBox::down-arrow {
    image: url("@CHEVRON@");
    width: 12px;
    height: 12px;
}

QComboBox QAbstractItemView {
    background-color: #FFFFFF;
    color: @INK@;
    border: 1px solid @BORDER_STRONG@;
    selection-background-color: @PRIMARY_SOFT@;
    selection-color: @PRIMARY_DEEPER@;
    outline: 0px;
}

/* ---------- Status and log ---------- */
QLabel#statusText {
    color: @INK@;
    font-weight: 600;
}

QProgressBar {
    background-color: #E3EEF4;
    border: none;
    border-radius: 4px;
    min-height: 8px;
    max-height: 8px;
    text-align: center;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 @PRIMARY@, stop:1 #43B9EE);
    border-radius: 4px;
}

QTextEdit {
    background-color: #FBFDFE;
    color: @TEXT@;
    border: 1px solid @BORDER@;
    border-radius: 8px;
    padding: 8px;
    font-family: @MONO@;
    font-size: 9pt;
    selection-background-color: @PRIMARY@;
    selection-color: #FFFFFF;
}

QTextBrowser {
    background-color: #FFFFFF;
    color: @TEXT@;
    border: 1px solid @BORDER@;
    border-radius: 10px;
    padding: 10px;
}

/* ---------- Footer ---------- */
QFrame#footer {
    background-color: #FFFFFF;
    border: none;
    border-top: 1px solid @BORDER@;
}

QLabel#footerNote {
    color: @MUTED@;
    font-size: 8pt;
}

/* ---------- Group boxes (used by the secondary dialogs) ---------- */
QGroupBox {
    background-color: #FFFFFF;
    border: 1px solid @BORDER@;
    border-radius: 10px;
    margin-top: 14px;
    padding: 18px 12px 12px 12px;
    font-weight: 700;
    color: @INK@;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 14px;
    padding: 0px 6px;
    background-color: @CANVAS@;
    color: @PRIMARY_DARK@;
}

QGroupBox QLabel, QGroupBox QCheckBox, QGroupBox QRadioButton {
    font-weight: 400;
}

QLabel#previewBox {
    background-color: @PRIMARY_SOFT@;
    border: 1px solid @PRIMARY_BORDER@;
    border-radius: 8px;
    padding: 9px 12px;
    color: @PRIMARY_DEEPER@;
    font-family: @MONO@;
    font-size: 9pt;
}

QLabel#errorText {
    color: @DANGER@;
    font-weight: 600;
}
"""


def build_stylesheet() -> str:
    """Return the complete Qt style sheet with the palette filled in."""
    tokens = {
        "@PRIMARY_DARK@": PRIMARY_DARK,
        "@PRIMARY_DEEPER@": PRIMARY_DEEPER,
        "@PRIMARY_SOFT@": PRIMARY_SOFT,
        "@PRIMARY_BORDER@": PRIMARY_BORDER,
        "@PRIMARY@": PRIMARY,
        "@INK@": INK,
        "@TEXT@": TEXT,
        "@MUTED@": MUTED,
        "@BORDER_STRONG@": BORDER_STRONG,
        "@BORDER@": BORDER,
        "@CANVAS@": CANVAS,
        "@SURFACE@": SURFACE,
        "@DANGER@": DANGER,
        "@FONT@": FONT_STACK,
        "@MONO@": MONO_STACK,
        "@CHECK@": resource_path("check.svg"),
        "@CHEVRON@": resource_path("chevron-down.svg"),
    }
    qss = _QSS_TEMPLATE
    for token, value in tokens.items():
        qss = qss.replace(token, value)
    return qss


STYLESHEET = build_stylesheet()


# ============================================================================
# SMALL HELPERS
# ============================================================================

def repolish(widget) -> None:
    """Re-apply the style sheet after a dynamic property changed."""
    style = widget.style()
    style.unpolish(widget)
    style.polish(widget)
    widget.update()
