---
name: decide
description: Record an owner's ruling: log it in decisions.md with their own words, clear the open decision, and relabel the guideline items it settles. Use when the owner has just decided something that was open, or asks to record a ruling.
---

# Record a ruling

Only the owner's words make a ruling. Anything else stays *(builder's call)*.

1. **Get the words.** Quote the owner exactly. If they haven't said it, don't record it: ask.
2. **Log it.** From the repo root:

   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/decide.py" --id <id> --ruling "<what was decided>" --quote "<their words>" --touches "<files>"
   ```

   It adds the row to "Rulings" in `docs/design/decisions.md` and removes the open decision with the same id.
3. **Relabel.** In each file it touches, move the settled items from **[Draft]** to **[Approved]** and quote the owner
   there. If the ruling contradicts an item or another ruling, fix both in this change and say so.
4. **Check.** Run `scripts/check-design.py`, then `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/design-status.py"` to show what
   is still open. Put it all in one commit on a `feature/` branch.
