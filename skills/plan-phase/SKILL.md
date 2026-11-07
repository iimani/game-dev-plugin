---
name: plan-phase
description: Plan the next phase of a game the game-dev way: read the design, update the master plan, write a phase plan file with one section per PR, and cut tasks from it. Use when the user asks what to build next, wants a phase or feature planned, or asks to cut tasks.
---

# Plan a phase

The design guideline is the tracker. A plan comes from it, and goes back into it as work lands.

## How work moves

1. **The method first, then code.** A thing gets designed through its method in `docs/process/`, with the owner's gates,
   before it's planned for building.
2. **A plan file per phase,** in `docs/plans/`. The master plan in `docs/design/plan.md` stays the summary.
3. **Tasks are cut from the plan,** one per PR, test-first.
4. **Every PR updates the design:** it marks its items **[Built, KEY-N]** and updates `docs/design/status.md`.
5. **Few handoffs.** A step that's mostly one side, with a little of the other, gets one owner. A step with real work on
   both sides keeps two roles, with the shared format settled first. Review fixes go back to the role that made the work.
   See "Handing work between roles" in `docs/team/README.md`.
6. **One lane at a time through shared files.** Land one PR, merge it into the next branch, and never rebase. Work in
   separate files can run in parallel.
7. **Don't build on what's being replaced.**

## Steps

1. Read `docs/design/README.md`, `plan.md`, `status.md` and `decisions.md`, then the files the routing table lists for
   this work. Read the code it touches. Plan from what's true, and don't assume a section is still current.
2. List what blocks the phase: open decisions, and items still **[Draft]**. Put them to the owner first, each with your
   call and what it costs if wrong.
3. Set the phase's goal and its exit: one sentence a person can check. The first phase of a new game is a vertical
   slice: one short stretch of the real game, with its core loop, proved and playable.
4. Pick a role for every step, from "Who does what" in `docs/team/README.md`, design steps included. Then write the plan
   file from `${CLAUDE_PLUGIN_ROOT}/skills/kickstart/templates/plan-file.md`. Each step is a PR with What,
   Read, Tests, Files and Proof. Name which role carries it out (`docs/team/README.md`). **Read** lists the sections and
   files that role needs, so its brief can name them and it reads nothing else.
5. Mark what can run in parallel. A step that waits on another names what it needs from it: a file, a format or a number.
   "The rules step" isn't an answer. If all it needs is a format, make settling that format a short first step, so both
   steps can run side by side. Levels, for example, usually need the tile format, not the finished rules.
   Steps that run side by side start as new agents, in one message. Don't plan on a resumed agent running beside another:
   its message can wait until the running agent finishes.
6. Update `docs/design/plan.md`: the phase, its exit, and "Where we are".
7. Stop for the owner's approval. Then cut the tasks, in the tracker named in CLAUDE.md.

## Close a task

A role reports what it built, and the session updates the design. When a task's work is done, and before its PR is marked
ready, the session:
1. Marks each item **[Built, KEY-N]** where it lives, and updates `docs/design/status.md` and "Where we are" in `plan.md`.
2. Adds anything built without a ruling to `docs/design/decisions.md`, or records it as a *(builder's call)*.
3. Updates the catalogues the task touched.
4. Runs `game-dev:design-guardian`, which checks all of the above.

## Keep it honest

- Everything is *(builder's call)* unless it quotes the owner.
- Size a step to one PR that a person can review.
- Size a step's tests in its plan: one test per rule each way, plus its proof. Writing tests costs more than running them.
  Keep every test that would catch a real break.
- A step's proof is something a tool or a person can check, and never "works well".
- If you can't name a step's proof, its design isn't finished.
