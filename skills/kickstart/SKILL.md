---
name: kickstart
description: Start a new game, or bring an existing one onto the team: walks the owner through vision, platform, core loop, art style and sound, then sets up the design guideline, method docs, team files, CLAUDE.md and the first plan. Use when the user starts a new game project or asks to set up the game-dev structure in a repo.
---

# Kickstart a game

This sets up a game's design, planning and documentation, so every later session and agent works the same way. Templates
are in `${CLAUDE_PLUGIN_ROOT}/skills/kickstart/templates/`. They're copied into the project and become the project's own:
the game changes them freely, and they never update from the plugin.

## The rules while you do this

- **The owner decides.** Go one stage at a time, and stop at each gate. Bring two or three real options with what each
  costs, plus your pick. Use their words, in quotes. Anything they didn't say is *(builder's call)*.
- **Don't fill silence with design.** A section with no decision says what's open. It doesn't get invented content.
- **The repo is the source of truth.** `docs/design/` is plain markdown, edited in the same PR as the change. Nothing is
  generated from anywhere else, so keeping the design current costs no sync step.
- **Existing repo:** read what's there first. Never overwrite a doc: map it onto the structure and say what's missing.

## Stages

| Stage | Settle | Writes to | Gate |
|---|---|---|---|
| 1. Look | New or existing repo, what's already decided | | |
| 2. Vision | One sentence, the feelings, three to five pillars, anti-goals, session length, how it's sold | `docs/design/README.md` | the owner |
| 3. Platform | Platform, engine, language, input, what can be tested without the engine | `docs/design/tech.md` | the owner |
| 4. Core loop | What the player does minute to minute, per session and over the whole game | `docs/design/run.md`, `docs/design/controls.md` | the owner |
| 5. Art style | Run the `choose-art-style` skill | `docs/design/art.md`, `docs/process/art-style.md` | the owner |
| 6. Sound | How much sound matters, its tool (see the art style method's tool table), whether it can carry information alone | `docs/design/audio.md` | the owner |
| 7. Methods | Which design methods this game needs (below) | `docs/process/` | the owner |
| 8. Tracking | Where tasks live, the task key, and how a task moves | `CLAUDE.md` | the owner |
| 9. Scaffold | Everything below | the repo | |
| 10. First plan | Run the `plan-phase` skill for phase 1, a vertical slice | `docs/design/plan.md` | the owner |

## A design document, if the owner wants one

Reading and commenting on a whole design is easier in a document than in a repo. If the owner wants that, and a docs
connector is available, draft stages 2 to 6 in one document and review it there. It's a design step, not a second home:
1. At stage 9, import the approved document into `docs/design/`, once.
2. Mark the document as frozen at its top: it's a record of that design, and the repo holds the current one.
3. Nothing flows back. Later, a session can publish a page from the repo if the owner asks. That page is one-way, and
   nobody edits it.

Do the same for a big design phase later on. Images go in the repo, so `docs/design/` can link them.

## Stage 7: choosing methods

`templates/process/README.md` lists them all, and each template's first lines say when to use it and which genres can
skip it. Always copy the index, `art-style.md`, `teaching-and-text.md` and `sound-design.md`. Offer the rest by what the
core loop needs: a puzzle game needs `puzzle-design.md`, a run-based game needs `procgen-design.md`, and so on. Fill each
`<fill: ...>` you can, and leave the others as open questions in the method.

## Stage 9: the scaffold

1. **Design guideline.** Copy `templates/design/` to `docs/design/`. Fill it from stages 2 to 6, or import the design
   document. Every item carries a
   label: **[Built]**, **[Approved]**, **[Draft]** or **[Proposal]**. What the owner ruled at a gate is **[Approved]**.
2. **Methods.** Copy the chosen files from `templates/process/` to `docs/process/`.
3. **Team.** Copy `templates/team/README.md` to `docs/team/README.md`. For each role in use, write `docs/team/<role>.md`
   from `templates/team/role-template.md`. A role file points to docs, and never copies them.
4. **CLAUDE.md.** Write it from `templates/CLAUDE.md`, and fill it from the design. Keep it to what every session needs.
5. **Plans.** Create `docs/plans/`. `templates/plan-file.md` is the pattern.
6. **Checks.** Copy `${CLAUDE_PLUGIN_ROOT}/scripts/check-team.py` and `check-design.py` to the project's `scripts/`, and
   run them from its test script.
7. **Plugin.** Add the plugin to the repo's `.claude/settings.json`, if the owner wants it declared there.

Then run both checks. Leave the commit to the owner's git flow: use a branch and a PR, never the main branch.

## What to report

What was set up, what the owner ruled, what's still open, and the first task in the plan.
