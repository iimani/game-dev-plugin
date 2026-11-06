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
5. **One lane at a time through shared files.** Land one PR, merge it into the next branch, and never rebase. Work in
   separate files can run in parallel.
6. **Don't build on what's being replaced.**

## Steps

1. Read `docs/design/README.md`, `plan.md`, `status.md` and `decisions.md`, then the files the routing table lists for
   this work. Read the code it touches. Plan from what's true, and don't assume a section is still current.
2. List what blocks the phase: open decisions, and items still **[Draft]**. Put them to the owner first, each with your
   call and what it costs if wrong.
3. Set the phase's goal and its exit: one sentence a person can check. The first phase of a new game is a vertical
   slice: one short stretch of the real game, with its core loop, proved and playable.
4. Write the plan file from `${CLAUDE_PLUGIN_ROOT}/skills/kickstart/templates/plan-file.md`. Each step is a PR with What,
   Tests, Files and Proof. Name which role carries it out (`docs/team/README.md`).
5. Update `docs/design/plan.md`: the phase, its exit, and "Where we are".
6. Stop for the owner's approval. Then cut the tasks, in the tracker named in CLAUDE.md.

## Keep it honest

- Everything is *(builder's call)* unless it quotes the owner.
- Size a step to one PR that a person can review.
- A step's proof is something a tool or a person can check, and never "works well".
- If you can't name a step's proof, its design isn't finished.
