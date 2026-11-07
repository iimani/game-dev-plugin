---
name: upgrade
description: Bring a game's copies of the plugin's templates up to date after the plugin changed: stale scripts, new template files and new sections in CLAUDE.md or the methods. Use when the plugin was updated, or when asked to upgrade or sync a game's setup.
---

# Upgrade a game's setup

A game holds copies of the plugin's templates, so it falls behind when the plugin changes. The script lists exactly where.
Run it from the repo root:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/upgrade-diff.py"
```

It lists three things and changes nothing. For each, propose the change and wait for the owner's yes before you make it. The
game's own wording always wins over the template's.

- **Scripts that differ.** Copy the plugin's script over the game's, then re-add the game's `PLANNED` entries.
- **Template files the game doesn't have.** Say what each is for and whether this game needs it (a small game skips most).
  Copy only the ones the owner wants, and add them to the routing table or methods index where they belong.
- **Template headings missing from the game's copy.** Read the template's section next to the game's file, and add the
  section only if it fits this game. Keep it short: a section nobody needs costs every session that reads the file.

Then run `scripts/check-team.py` and `scripts/check-design.py`. Put the whole upgrade in one PR on a `feature/` branch, with
what was added and what the owner declined.
