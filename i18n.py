"""Internationalisation loader for OSM Data Toolkit.

Translation files live in ``translations/<language>.py``. Each file exports
a dictionary named ``TEXT`` mapping the original English UI string to its
translated equivalent. Add or edit values in those files without changing
the UI code.
"""
from __future__ import annotations

import importlib
import re
from string import Formatter
from qgis.PyQt.QtCore import QSettings

LANGUAGES = [('en', 'English'), ('fr', 'Français'), ('es', 'Español'), ('it', 'Italiano'), ('zh', '中文'), ('ar', 'العربية'), ('pt', 'Português'), ('de', 'Deutsch'), ('ru', 'Русский'), ('ja', '日本語'), ('sw', 'Kiswahili'), ('sv', 'Svenska'), ('nb', 'Norsk (bokmål)'), ('da', 'Dansk'), ('hi', 'हिन्दी'), ('bn', 'বাংলা'), ('ur', 'اردو'), ('pa', 'ਪੰਜਾਬੀ'), ('mr', 'मराठी'), ('te', 'తెలుగు'), ('ta', 'தமிழ்'), ('gu', 'ગુજરાતી'), ('id', 'Bahasa Indonesia'), ('tr', 'Türkçe'), ('ko', '한국어'), ('vi', 'Tiếng Việt'), ('fa', 'فارسی'), ('th', 'ไทย'), ('pl', 'Polski'), ('nl', 'Nederlands'), ('uk', 'Українська'), ('am', 'አማርኛ'), ('ha', 'Hausa')]
RTL_LANGUAGES = ("ar", "fa", "ur")

def normalise(code):
    code = str(code or "en").strip().lower().replace("-", "_").split("_")[0]
    aliases = {"no": "nb", "nn": "nb", "in": "id"}
    code = aliases.get(code, code)
    return code if any(item[0] == code for item in LANGUAGES) else "en"

def default_language():
    settings = QSettings()
    return normalise(settings.value("OSMDataToolkit/language", "en", type=str))

def save_language(code):
    QSettings().setValue("OSMDataToolkit/language", normalise(code))

def _load_pack(code):
    try:
        module = importlib.import_module(".translations." + code, package=__package__)
        return getattr(module, "TEXT", {}) or {}
    except Exception:
        return {}

def tr(source_text, lang=None):
    code = normalise(lang or default_language())
    if code == "en":
        return source_text
    pack = _load_pack(code)
    return pack.get(source_text, source_text)

def available_languages():
    return list(LANGUAGES)


def tr_format(source_text, lang=None, **values):
    """Translate a source template, then interpolate its original placeholders."""
    template = tr(source_text, lang)
    try:
        return template.format(**values)
    except (KeyError, IndexError, ValueError):
        # Preserve the untranslated source rather than lose a diagnostic.
        return source_text.format(**values)


def translate_dynamic(message, lang=None):
    """Translate exact and templated runtime messages without altering payloads."""
    text = str(message)
    exact = tr(text, lang)
    if exact != text:
        return exact
    code = normalise(lang or default_language())
    if code == "en":
        return text
    pack = _load_pack(code)

    # Match parameterised source templates (e.g. "Downloaded {count} items").
    for source in sorted((k for k in pack if "{" in k and pack[k] != k),
                         key=len, reverse=True):
        try:
            parts = list(Formatter().parse(source))
        except ValueError:
            continue
        regex_parts = []
        fields_found = []
        for literal, field_name, _format_spec, _conversion in parts:
            regex_parts.append(re.escape(literal))
            if field_name is not None:
                fields_found.append(field_name.split(".", 1)[0].split("[", 1)[0])
                regex_parts.append("(.+?)")
        match = re.fullmatch("".join(regex_parts), text, flags=re.DOTALL)
        if match:
            translated = pack[source]
            for field_name, value in zip(fields_found, match.groups()):
                translated = re.sub(r"\{" + re.escape(field_name) + r"[^}]*\}",
                                    lambda _m, v=value: v, translated)
            return translated

    # Translate the longest known prefix while retaining dynamic details.
    for source in sorted(pack, key=len, reverse=True):
        if source and text.startswith(source) and pack[source] != source:
            text = pack[source] + text[len(source):]
            break

    # Translate known Overpass status fragments embedded in parameterised
    # server/attempt messages; leave URLs and raw exception details untouched.
    fragments = (
        "attempt ", "timeout — ", "connection error — ", "HTTP error — ",
        "request error — ", "invalid response — ", " responded successfully.", "Details:",
        "Retrying in ", " seconds...", "All attempts failed for server ", "Attempt details:",
    )
    for source in fragments:
        target = pack.get(source, source)
        if source != target and source in text:
            text = text.replace(source, target)
    return text


def audit_translation_pack(code="fr"):
    """Return source/target coverage metrics for the selected language pack."""
    source = _load_pack("en")
    target = _load_pack(code)
    missing = sorted(key for key in source if key not in target)
    untranslated = sorted(key for key in source if target.get(key, key) == key)
    return {
        "language": normalise(code),
        "source_keys": len(source),
        "translated_keys": sum(1 for key in source if target.get(key, key) != key),
        "untranslated_keys": untranslated,
        "missing_keys": missing,
    }
