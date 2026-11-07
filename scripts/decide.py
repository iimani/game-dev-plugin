#!/usr/bin/env python3
"""Records an owner's ruling in docs/design/decisions.md. Run from the game's repo root.

decide.py --id D3 --ruling "Keys carry between rooms" --quote "keys should carry over" [--touches mechanics.md]

Adds a row to the "## Rulings" table (creating it if missing) and removes the open-decision row with the same id.
The session still relabels the guideline items the ruling touches, and quotes the owner there.
"""
import argparse
import datetime
import pathlib
import sys

ap = argparse.ArgumentParser()
ap.add_argument("--id", required=True)
ap.add_argument("--ruling", required=True)
ap.add_argument("--quote", required=True, help="the owner's own words")
ap.add_argument("--touches", default="")
a = ap.parse_args()

path = pathlib.Path.cwd() / "docs/design/decisions.md"
if not path.exists():
    sys.exit("decide: no docs/design/decisions.md here. Run it from a game's repo root.")

lines = path.read_text().splitlines()
cell = lambda s: s.replace("|", "/").replace("\n", " ").strip()
before = len(lines)
lines = [l for l in lines if not (l.startswith("|") and l.split("|")[1].strip() == a.id)]
removed = before - len(lines)

row = f"| {cell(a.id)} | {datetime.date.today()} | {cell(a.ruling)} | \"{cell(a.quote)}\" | {cell(a.touches)} |"
if "## Rulings" not in lines:
    lines += ["", "## Rulings", "", "What the owner decided, in their words.", "",
              "| Id | Date | Ruling | Owner's words | Touches |", "| --- | --- | --- | --- | --- |"]
end = len(lines)
while end > 0 and not lines[end - 1].startswith("|") and lines[end - 1].strip() == "":
    end -= 1
lines.insert(end, row)
path.write_text("\n".join(lines) + "\n")
print(f"decide: recorded {a.id}" + (", removed it from Open decisions" if removed else ", no open row with that id"))
