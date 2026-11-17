# OSM Data Toolkit translations

Each language has its own editable Python file in this folder:

- `en.py` — English source strings (reference)
- `fr.py` — French
- `es.py` — Spanish
- `sw.py` — Kiswahili
- `ar.py` — Arabic
- and the remaining language files listed in the plugin language selector.

## How to edit a translation

Every language file exports a dictionary named `TEXT`. The dictionary key
must remain the exact English source string used by the interface. Change only
the value on the right-hand side.

Example:

```python
TEXT = {
    "Download": "Télécharger",
    "Processing log": "Journal de traitement",
}
```

If a key is missing, or its value is still English, the interface safely
falls back to the original English text. This makes it possible to translate
the plugin gradually.

## How language switching works

`i18n.py` loads `translations/<language_code>.py` when the user chooses a
language. The main dialog's language selector saves the choice in QGIS
settings and reapplies translated labels, placeholders, tooltips, and combo
box entries. Arabic, Persian, and Urdu use right-to-left layout direction.

Keep the language code in the filename aligned with the code in
`i18n.LANGUAGES`. No third-party translation package is required.
