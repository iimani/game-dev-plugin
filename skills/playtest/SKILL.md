---
name: playtest
description: Run one blind playtest of a game change, from build to verdict: prove the game starts, brief the blind playtester with only the controls sheet, sort its findings, fix the critical ones through the role that made the work, retest, and rank the rest as optional work. Use after a change the player sees, before its PR is marked ready, or when asked to playtest.
---

# Playtest

One loop from a changed build to a verdict. It runs the project's own tools: the commands are in `docs/design/tech.md`
(its `### Engine` section) and the controls are in `docs/team/playtester-controls.md`. If either is missing, stop and say
so: don't guess a game's commands.

## 1. Before the tester

1. **Prove it starts.** Run the project's headless or smoke command from `tech.md`, and its tests. A game that doesn't
   start isn't playtested: fix that first.
2. **Size the run to the change.** Pick the mode, a goal that names a place and never a mechanic, and the device. Set the
   move limit well above the shortest route, so a slip doesn't end the run.
3. **Play the sheet once yourself,** using only `playtester-controls.md`. If you stall on it, the sheet is wrong: fix it
   before the tester pays for it.

## 2. The tester

Run `game-dev:playtester` and give it only: `docs/team/playtester-controls.md` word for word, the mode, the goal, the move
limit and the device. Never say what changed or why. If the simulator or browser pane can't run, record the playtest as
**not done**: it's never a pass.

## 3. The verdict

You sort every finding, never the tester. The main result is the gap between what the tester believed and the real rules.

| Level | Means | What happens |
|---|---|---|
| **Critical** | The game can't be finished, something is really broken, or a wrong belief cost the player the level | Fixed in this task by the role that made the work, in one message, then retested |
| **Worth doing** | It works, but the player lost time or misread something | Ranked in "Optional" in the phase's plan file, with its evidence and rough size. Not built unless the owner picks it |
| **Noise** | A tool artifact, or a one-off with nothing behind it | One line in the verdict, then dropped |

- **Critical needs proof.** Reproduce it, or check it against the real rules, first. Running out of moves isn't Critical
  by itself, and neither is a report that a key was lost.
- **Retest only what changed:** the place the fix touched, for at most two rounds. If it's still Critical, it goes to the
  owner.

## 4. Write it down

Put the verdict in the PR: the run's setup (mode, goal, limit, device), what the tester believed against the real rules,
the findings by level, what was fixed and retested, and anything not done. Add each **Worth doing** to "Optional" in the
plan file, best first. When the game records runs (`docs/process/telemetry.md`), run `game-dev:balance-analyst` on the
numbers a finding rests on, instead of arguing from one player.
