---
name: close
description: Close a game task before its PR is marked ready: check the branch against the design, mark items Built, record decisions, then run the reviewers and a playtest if the player sees the change. Use when a task's work is done, or when asked to close or finish a task.
---

# Close a task

The script does the checking, so you only do the judgment. Run it from the repo root with the task key (`KEY-N` from the
branch or the tracker):

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/close-task.py" KEY-N
```

It prints `OK`, `FIX` and `TODO` lines, and exits 1 on any `FIX`.

1. **Fix each `FIX`.** Mark each item this task built **[Built, KEY-N]** where it lives in `docs/design/`, and update
   `docs/design/status.md` and "Where we are" in `plan.md`. Add anything built without a ruling to `decisions.md`, or mark
   it *(builder's call)*. Run the script again until nothing says `FIX`.
2. **Do each `TODO`.** Update the catalogues the task touched. If the player sees the change, run the playtest skill and add
   its **Worth doing** findings to "Optional" in the plan file.
3. **Run `game-dev:code-reviewer` and `game-dev:design-guardian`** together, in one message. Fix what they find through the
   role that made the work, and re-run only what changed.
4. **Write the PR body** in the form the repo's `CLAUDE.md` gives: the task, what changed and why, Tests and Demo. Say
   plainly what didn't run.

Don't mark the PR ready until step 3 is clean. Never merge: the owner does.
