#!/usr/bin/env python3
"""Static translation completeness audit for OSM Data Toolkit (no QGIS required)."""
from __future__ import annotations
import ast
import re
from pathlib import Path
from string import Formatter

ROOT = Path(__file__).resolve().parents[1]

def read_pack(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    assignment = next(n for n in tree.body if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == "TEXT" for t in n.targets))
    return ast.literal_eval(assignment.value)

def fields(value):
    try:
        return sorted(name for _, name, _, _ in Formatter().parse(value) if name is not None)
    except ValueError:
        return ["<invalid-format-string>"]

en = read_pack(ROOT / "translations" / "en.py")
fr = read_pack(ROOT / "translations" / "fr.py")
missing = sorted(set(en) - set(fr))
untranslated = sorted(k for k in en if fr.get(k, k) == k)
placeholder_mismatches = sorted(
    k for k in en if k in fr and fields(k) != fields(fr[k])
)

# Audit literal text supplied directly to common GUI constructors/setters.
gui_tree = ast.parse((ROOT / "gui" / "main_dialog.py").read_text(encoding="utf-8"))
gui_call_names = {
    "QLabel", "QPushButton", "QCheckBox", "QRadioButton", "QGroupBox",
    "QLineEdit", "setText", "setTitle", "setWindowTitle", "setToolTip",
    "setPlaceholderText", "addRow", "addItem", "getExistingDirectory",
}
gui_literals = []
for node in ast.walk(gui_tree):
    if not isinstance(node, ast.Call):
        continue
    func = node.func
    name = func.id if isinstance(func, ast.Name) else (
        func.attr if isinstance(func, ast.Attribute) else ""
    )
    if (name in gui_call_names and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)):
        gui_literals.append(node.args[0].value)
unkeyed_gui = sorted(set(value for value in gui_literals
                         if value not in en and value not in fr
                         and value not in {"", "0%"}))
intentional = {
    "OSM Data Toolkit": "Nom officiel du plugin (nom de produit conservé).",
    "relations).": "Terme technique identique en français dans ce fragment de journal.",
}
unintended = [k for k in untranslated if k not in intentional]

print("OSM Data Toolkit — audit des traductions")
print(f"Clés source anglaises : {len(en)}")
print(f"Clés présentes dans le pack français : {sum(k in fr for k in en)}")
print(f"Traductions françaises différentes de la source : {sum(fr.get(k, k) != k for k in en)}")
print(f"Clés manquantes : {len(missing)}")
print(f"Valeurs identiques à la source : {len(untranslated)}")
print(f"Chaînes volontairement conservées : {len(intentional)}")
print(f"Chaînes utilisateur non traduites restantes : {len(unintended)}")
print(f"Incohérences d’espaces réservés : {len(placeholder_mismatches)}")
print(f"Littéraux de texte GUI analysés : {len(gui_literals)}")
print(f"Littéraux GUI sans clé de traduction : {len(unkeyed_gui)}")
if missing:
    print("\nClés manquantes:\n" + "\n".join(missing))
if unintended:
    print("\nChaînes non traduites à examiner:\n" + "\n".join(unintended))
if placeholder_mismatches:
    print("\nEspaces réservés incohérents:\n" + "\n".join(placeholder_mismatches))
if intentional:
    print("\nConservées volontairement:")
    for key, reason in intentional.items():
        print(f"- {key}: {reason}")
raise SystemExit(1 if missing or unintended or placeholder_mismatches or unkeyed_gui else 0)
