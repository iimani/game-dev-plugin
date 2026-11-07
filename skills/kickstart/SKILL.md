---
name: kickstart
description: Start a new game: walks the owner through vision, platform, core loop, art style and sound, then sets up the design guideline, method docs, team files, CLAUDE.md and the first plan. Use when the user starts a new game project or asks to set up the game-dev structure in a repo.
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
- **Copy, don't retype.** Templates go in with `cp` or a script. Never read a template and write it back, and never spend
  an agent on copying. Then fill each file with small edits.
- **Existing game:** use the `migrate` skill instead. An empty repo, or one with only a rough idea, stays here.

## Stages

| Stage | Settle | Writes to | Gate |
|---|---|---|---|
| 1. Look | New or existing repo, what's already decided, and the game's size (below) | | the owner |
| 2. Scaffold | Copy the structure in first, so every later stage has its file (below) | the repo | |
| 3. Vision | One sentence, the feelings, three to five pillars, anti-goals, session length, how it's sold | `docs/design/README.md` | the owner |
| 4. Platform | Platform, engine, language, input, what can be tested without the engine; the engine's adapter (below) | `docs/design/tech.md` | the owner |
| 5. Core loop | What the player does minute to minute, per session and over the whole game | `docs/design/run.md`, `docs/design/controls.md` | the owner |
| 6. Art style | Run the `choose-art-style` skill | `docs/design/art.md`, `docs/team/game-artist.md` | the owner |
| 7. Sound | How much sound matters, its tool (see the art style method's tool table), whether it can carry information alone | `docs/design/audio.md` | the owner |
| 8. Methods | Which design methods this game needs (below) | `docs/process/` | the owner |
| 9. Tracking | Where tasks live, the task key, and how a task moves | `CLAUDE.md` | the owner |
| 10. Team | Which roles this game uses, who does what, and each role's model (below) | `docs/team/`, `CLAUDE.md` | the owner |
| 11. First plan | Run the `plan-phase` skill for phase 1, a vertical slice | `docs/design/plan.md` | the owner |

## A small game

The full setup costs more than a small game can repay. At stage 1, recommend the small path for a game that fits in one
phase, with one person's decisions and no long life after it ships. The owner decides, and can move to the full setup
later by copying in what's missing.

Small changes these stages. The others run as above.

| Stage | On the small path |
|---|---|
| 2. Scaffold | Copy only `README.md`, `mechanics.md`, `tech.md`, `plan.md`, `status.md` and `decisions.md` from `templates/design/`, and take the other files out of the routing table, deleting any row left empty. Copy `templates/team/README.md`. Skip `docs/art/catalogue.md`, and copy `docs/process/` at stage 8. |
| 3 to 7 | One sheet and one gate. Vision goes in `docs/design/README.md`, the core loop in `mechanics.md`, and platform, art and sound in `tech.md`, a few lines each. Skip `choose-art-style` unless the owner wants a test. |
| 8. Methods | Copy only the methods the kept roles' rows name, and cut the index to match. |
| 10. Team | Write a role file only for a role with two or more tasks in the plan. Every other role's brief carries what its file would: what to read, where the work lives, the tools, how to prove it and what it must not do. Use the recommended models unless the owner objects. |

Check-team and check-design still run. `docs/team/playtester-controls.md` is still written if the plan has a playtest.

## A design document, if the owner wants one

Reading and commenting on a whole design is easier in a document than in a repo. If the owner wants that, and a docs
connector is available, draft stages 3 to 7 in one document and review it there. It's a design step, not a second home:
1. Before stage 8, import the approved document into `docs/design/`, once.
2. Mark the document as frozen at its top: it's a record of that design, and the repo holds the current one.
3. Nothing flows back. Later, a session can publish a page from the repo if the owner asks. That page is one-way, and
   nobody edits it.

Do the same for a big design phase later on. Images go in the repo, so `docs/design/` can link them.

## Stage 2: the scaffold

1. **Design guideline.** Copy `templates/design/` to `docs/design/`. Later stages fill it, or import the design document.
   Every item carries a label: **[Built]**, **[Approved]**, **[Draft]** or **[Proposal]**. What the owner ruled at a gate
   is **[Approved]**.
2. **Methods.** Copy all of `templates/process/` to `docs/process/`. Stage 8 removes what the game doesn't need.
3. **Team.** Copy `templates/team/README.md` and `templates/team/playtester-controls.md` to `docs/team/`.
4. **Art and plans.** Create `docs/art/catalogue.md` with a title, and `docs/plans/`. `templates/plan-file.md` is the
   pattern for a plan.
5. **CLAUDE.md.** Write it from `templates/CLAUDE.md`, now, so roles have it from their first run. Later stages fill it.
   Keep it to what every session needs.
6. **Checks.** Copy `${CLAUDE_PLUGIN_ROOT}/scripts/check-team.py` and `check-design.py` to the project's `scripts/`, and
   run them from its test script. A path that's named but not built yet goes in the script's `PLANNED` set.
7. **Plugin.** Add the plugin to the repo's `.claude/settings.json`, if the owner wants it declared there.

## Stage 4: the engine adapter

`templates/engines/` holds a short adapter per engine: `godot.md`, `unity.md`, `unreal.md`, `web.md` and `bevy.md`. Each
gives the headless run, test and export commands, how the playtester sees the game, and what to keep engine-free. When the
owner picks one of these, paste it under `### Engine` in `docs/design/tech.md` and fill its `<fill: ...>` bits. Commands change
between versions, so run each one with the engine's `--help` or once for real, and record the version and the command that
worked. Then call the test command from the project's test script. For another engine, write the same six labels by hand.

## Stage 8: choosing methods

`templates/process/README.md` lists them all, and each template's first lines say when to use it and which genres can
skip it. Always keep the index, `art-style.md`, `teaching-and-text.md` and `sound-design.md`. Keep the rest by what the
core loop needs: a puzzle game needs `puzzle-design.md`, a run-based game needs `procgen-design.md`, and so on. Delete the
others, with their rows in the index. Fill each `<fill: ...>` you can, and leave the others as open questions.

## Stage 10: the team

**This stage decides if the team gets used.** A session does the work itself unless it's told otherwise, so the setup has
to make delegation the default.

1. Decide which roles this game uses. Delete the other roles' rows from `docs/team/README.md`, in both tables.
2. Write `docs/team/<role>.md` for each role, from `templates/team/role-template.md`. A role file points to docs, and
   never copies them. Write `docs/team/playtester-controls.md` too: it lists every key the game accepts or prompts for,
   including between levels and on menus.
3. Fill the "Who does what" table in `docs/team/README.md` with this game's own kinds of work.
4. Run the `choose-models` skill: it recommends a model for each role, and the owner decides.
5. Keep the "Agents" section of `CLAUDE.md` as the template has it. Add nothing that says the session keeps the design:
   that line is what sends the work back to the session.

Then run both checks. Leave the commit to the owner's git flow: use a branch and a PR, never the main branch.

## What to report

What was set up, what the owner ruled, what's still open, and the first task in the plan.
