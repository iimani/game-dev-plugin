#!/usr/bin/env python3
"""Counts a game's design items by status label, from docs/design/. Run from the game's repo root.

Reports each file's Built, Approved, Draft and Proposal counts, the Draft items the owner hasn't reviewed, the open
decisions, and the "Optional" findings in the newest plan file. Reads files, spends no model tokens.
"""
import pathlib
import re
import sys

root = pathlib.Path.cwd()
design = root / "docs/design"
if not design.is_dir():
    sys.exit("design-status: no docs/design/ here. Run it from a game's repo root.")

LABEL = re.compile(r"\*\*\[?(Built|Approved|Draft|Proposal)\b[^\]*]*\]?\*\*")
LEGEND = re.compile(r"^\|\s*\*\*(Built|Approved|Draft|Proposal)\*\*\s*\|")
NAMES = ("Built", "Approved", "Draft", "Proposal")

counts, drafts = {}, []
for path in sorted(design.glob("*.md")):
    row = dict.fromkeys(NAMES, 0)
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if LEGEND.match(line) or re.match(r"^\|\s*<", line):
            continue
        for match in LABEL.finditer(line):
            row[match.group(1)] += 1
            if match.group(1) == "Draft":
                drafts.append(f"{path.name}:{number}  {re.sub(r'[|*]', ' ', line).strip()[:90]}")
    if any(row.values()):
        counts[path.name] = row

total = {n: sum(r[n] for r in counts.values()) for n in NAMES}
print("design status: " + ", ".join(f"{total[n]} {n}" for n in NAMES))
print(f"\n{'file':<18}" + "".join(f"{n:>10}" for n in NAMES))
for name, row in counts.items():
    print(f"{name:<18}" + "".join(f"{row[n]:>10}" for n in NAMES))
if drafts:
    print(f"\nDraft, not yet reviewed by the owner ({len(drafts)}):")
    print("\n".join("  " + d for d in drafts[:15]) + (f"\n  ... and {len(drafts) - 15} more" if len(drafts) > 15 else ""))


def table_rows(text, heading):
    """First cells of the data rows in the first table under `heading`."""
    if heading not in text:
        return []
    block = text.split(heading, 1)[1].split("\n## ", 1)[0]
    rows = [l for l in block.splitlines() if l.startswith("|")][2:]
    return [r.split("|")[1].strip() for r in rows if r.split("|")[1].strip() and not r.split("|")[1].strip().startswith("<")]


decisions = design / "decisions.md"
if decisions.exists():
    ids = table_rows(decisions.read_text(), "## Open decisions")
    print(f"\nOpen decisions: {len(ids)}" + (f" ({', '.join(ids)})" if ids else ""))

plans = sorted((root / "docs/plans").glob("*.md")) if (root / "docs/plans").is_dir() else []
if plans:
    optional = [i for i in table_rows(plans[-1].read_text(), "## Optional") if i.isdigit()]
    print(f"Optional in {plans[-1].relative_to(root)}: {len(optional)}")
