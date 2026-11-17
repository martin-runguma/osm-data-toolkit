# OSM Data Toolkit — French translation audit

**Audit date:** 11 November 2026  
**Audited package:** `OSM_Data_Toolkit`  
**Method:** Static comparison of `translations/en.py` and `translations/fr.py`, placeholder-parity checks, Python syntax compilation, and manual review of GUI/worker translation paths.

## Translation dictionary results

| Measure | Result |
|---|---:|
| English source keys identified | 373 |
| Keys present in French pack | 373 |
| French values translated or deliberately adapted | 371 |
| Missing French keys | 0 |
| Remaining identical source/target values | 2 |
| Unintended untranslated user-facing keys | **0** |
| Placeholder mismatches | **0** |

The two identical values are intentional:
- `OSM Data Toolkit` — official plugin/product name.
- `relations).` — the technical term *relations* is identical in this French context.

## Implementation changes

- Central loader `i18n.py` retains the existing `tr()` API and adds `tr_format()` for placeholder-safe formatting, `translate_dynamic()` for exact/prefix runtime messages, and `audit_translation_pack()` for programmatic coverage checks.
- `translations/fr.py` now provides French equivalents for all user-facing source keys in the English source pack.
- Main-dialog retranslation now covers widget text, window and group titles, placeholders, tooltips, and combo-box entries.
- Secondary output-naming and help dialogs receive the selected language.
- The in-plugin help has a French version stored in `translations/fr.py`; documentation links and technical product names remain unchanged.
- Runtime status messages, worker messages, cache diagnostics, common Overpass/network errors, AOI validation errors, export errors, log entries, and message-box text are translated at the GUI boundary while retaining dynamic values such as paths, counts, exception details, coordinates, and CRS identifiers.
- Language persistence continues to use QGIS `QSettings`; the existing language selector updates the visible main dialog without restarting QGIS.
- No OSM query construction, download, cache, or export algorithm was intentionally changed.

## Automated checks

- All Python modules passed `py_compile`.
- English and French translation dictionaries parsed successfully.
- All 373 English keys are present in the French pack.
- All format placeholders were checked for parity.
- A static scan of direct GUI widget constructors and text setters found 64 literal UI text arguments; all user-facing strings were present in the translation inventory. The only two non-key literals were an empty string and the numeric progress label `0%`.
- `tools/translation_audit.py` exits successfully with zero unintended untranslated keys.

## Runtime verification limits

This environment does not provide a running QGIS 3.44 or QGIS 4 application, nor its embedded PyQt runtime. Therefore the following could not be truthfully certified here: loading the plugin inside QGIS, exercising live canvas tools, making real Overpass requests, exporting live GeoPackage/Shapefile data, and testing language persistence across an actual QGIS restart. Those checks should be run in both supported QGIS environments before production deployment.

## Remaining limitations

- The static audit validates the maintained translation source dictionary, direct GUI widget text literals, and formatting placeholders. It cannot prove that every third-party Qt-generated string or every exception text from external libraries is translated.
- Some low-level exception details and externally generated Overpass/network diagnostics may contain English text supplied by Python, QGIS, requests, or the remote service. The surrounding plugin-generated message is translated; the raw technical detail is preserved for diagnostics.
- The existing English source pack is maintained as the canonical source-key inventory; other language packs were not rewritten.
