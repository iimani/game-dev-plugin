# Playtest ledger

Use when: the game is playtested more than once, so one run can be read against the others.
Skip when: a game with a single playtest, whose verdict lives in its PR.

One row per run, added by the session that ran it (`/game-dev:playtest`). Never one row for a set of runs: three runs of
one brief are three rows, and a before-and-after pair is two. A run that couldn't start gets a row too, with **not
done** as its result. Rows are never edited afterwards or removed.

## How to fill a row

- **Build:** the commit that was played.
- **Profile:** blind, practiced or regular, then the temperament if one was given.
- **Brief:** the mode, the goal, the move limit and the device.
- **Result:** the goal reached or not, moves used, deaths, times stuck. Put **(log)** after a figure from the game's own
  run log and **(tester)** after one the tester counted.
- **Findings:** how many at each level (Critical, Worth doing, Noise), as this run alone gave them.
- **For:** the task or PR, and "before" or "after" when the run is half of a pair.

## Runs

| Date | Build | Profile | Brief | Result | Findings | For |
|---|---|---|---|---|---|---|
| <fill: date> | | | | | | |
