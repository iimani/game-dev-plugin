---
name: playtest
description: Run a playtest of a game change, from build to verdict: prove the game starts, pick the tester's profile (blind, practiced, regular), brief it, sort its findings, fix the critical ones through the role that made the work, retest, and rank the rest as optional. Use after a change the player sees, before its PR is marked ready, or when asked to playtest.
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

## 2. Pick the profile

One role, three players. What the brief holds decides which one plays.

| Profile | The tester gets | It answers | Use it when |
|---|---|---|---|
| **Blind** | The controls sheet | Can a first-time player read this, and where do they stall? | The change is something a newcomer meets: a first room, a lesson, a sign, the HUD |
| **Practiced** | The sheet and `docs/team/player-guide.md` | Does it hold up for someone who knows the game: pace, friction, difficulty, is it worth playing? | The change sits past the opening, or alters something a player already knows |
| **Regular** | The sheet, the guide and `docs/team/playtester-journal.md` | Is this session better or worse than the ones before it? | The same player returns over several builds: long-run feel, and what quietly got worse |

- **A game with no player's guide runs blind only.** Don't write a guide to get a run: it's written from play, as its
  own piece of work.
- **The guide is the game as the player knew it.** Never update it for the change under test before the run.
- **A temperament is optional,** one line in the brief, written out because the role doesn't define it. With none, the
  tester plays as it would.
  - *Skipper*, to show what can be skipped and the least a player must understand: "Temperament: you do as little as
    you can. Take the shortest way you can see, and pass by text and anything that looks optional."
  - *Explorer*, to find dead ends and edges: "Temperament: you look in every corner. Try each thing you find, and take
    the side way before the main one."

## 3. The tester

Run `game-dev:playtester` and give it only:
- `docs/team/playtester-controls.md`, word for word;
- for practiced and regular, the guide, word for word from below its line; for regular, the journal the same way;
- the mode, the goal, the move limit and the device, and the temperament line if there is one.

Never say what changed or why, to any profile, and never name the profile or the task. If the simulator or browser
pane can't run, record the playtest as **not done**: it's never a pass.

- **A verdict that gates a merge rests on three runs of the same brief.** Start the three together, in one message.
  One run is enough for a look that gates nothing: say it was one.
- **To ask whether a change helped, run before and after.** The same profile and the same brief play the build before
  the change and the build after it. No tester is told which build it has, and nothing it can see says so. A gating
  answer needs three of each.

## 4. The verdict

You sort every finding, never the tester. The main result is the gap between what the tester believed and the real rules.

| Level | Means | What happens |
|---|---|---|
| **Critical** | The game can't be finished, something is really broken, or a wrong belief cost the player the level | Fixed in this task by the role that made the work, in one message, then retested |
| **Worth doing** | It works, but the player lost time or misread something | Ranked in "Optional" in the phase's plan file, with its evidence and rough size. Not built unless the owner picks it |
| **Noise** | A tool artifact, or a one-off with nothing behind it | One line in the verdict, then dropped |

- **Critical needs proof.** Reproduce it, or check it against the real rules, first. Running out of moves isn't Critical
  by itself, and neither is a report that a key was lost.
- **Write it as a count:** "stuck at the gate in 2 of 3 runs", never "the tester got stuck". Three runs that disagree
  are the finding: don't pick the one you believe.
- **Read each finding against its profile.** Only a blind run says whether something can be learned: a practiced player
  walking through a room doesn't show a newcomer would. A blind player's "too hard" or "too slow" says little about
  balance. Where a practiced player contradicts the guide, check which is wrong, the guide or the build. A skipper
  missing something doesn't make it hidden, and an explorer's move count isn't the pace.
- **Prefer the game's own run log.** Where `docs/process/telemetry.md` exists, record the run and take its figures from
  the log. It outranks the tester's memory wherever they disagree. The tester's "run in numbers" is the fallback, and is
  labelled as the tester's count.
- **Retest only what changed:** the place the fix touched, for at most two rounds. If it's still Critical, it goes to the
  owner.

## 5. Write it down

Put the verdict in the PR: the run's setup (profile, temperament, mode, goal, limit, device, how many runs), what the
testers believed against the real rules, the findings by level as counts, what was fixed and retested, and anything not
done. Add each **Worth doing** to "Optional" in the plan file, best first.

- **The ledger.** Where the game has `docs/process/playtest-ledger.md`, add one row per run, never one for a set.
- **The journal.** After a regular run, replace everything below the line in `docs/team/playtester-journal.md` with the
  tester's rewritten notes, unedited: not corrected, trimmed or added to. From three runs keep the first one's, and from
  a before-and-after set the first after-run's.
- **Numbers.** When the game records runs, run `game-dev:balance-analyst` on the numbers a finding rests on, instead of
  arguing from one player.

## A project's own copy of the role

`game-dev:playtester` plays through the simulator or the browser pane. A game that plays through its own tools keeps a
copy of the role in `.claude/agents/`, named `<something>-playtester`, and this skill runs that copy instead. The copy
changes only the frontmatter: its name, description and tools. Its body is `agents/playtester.md` from the plugin, word
for word, and anything about the game goes in the controls sheet, never in the copy. `/game-dev:upgrade` lists a copy
whose body has fallen behind: copy the plugin's body over it again.
