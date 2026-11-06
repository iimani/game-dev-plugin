---
name: migrate
description: Move a game that's already in development onto the game-dev setup: audit its docs, code and agents, map them onto the design guideline, method and team structure, and turn on delegation, without losing or overwriting anything. Use when the user wants an existing game repo brought onto game-dev.
---

# Migrate an existing game

`kickstart` starts a game from nothing. This brings in a game that already has code, docs and habits. The game's real
state wins: map what's there, and don't redesign it. Templates are in
`${CLAUDE_PLUGIN_ROOT}/skills/kickstart/templates/`.

## The rules while you do this

- **Nothing is lost.** Move and link. Never overwrite or delete a doc until its content is confirmed in its new home.
- **Don't invent design.** A gap is written down as a gap. A decision you can't find a source for is **[Draft]**, marked
  *(builder's call)*.
- **Label by evidence.** **[Built]** needs code you've read or a test that passes. **[Approved]** needs the owner's words.
- **One PR per step,** on a branch. Never commit to the main branch. Stop after the audit for the owner.

## Stages

| Stage | What | Gate |
|---|---|---|
| 1. Audit | What exists, and how it maps (below). Change nothing | the owner approves the map |
| 2. Guideline | `docs/design/`, filled from what's there | the owner reviews labels and open decisions |
| 3. Methods | `docs/process/`, keeping any process the game already has | the owner |
| 4. Team | `docs/team/`, role files, "Who does what", delegation in `CLAUDE.md`, and each role's model | the owner |
| 5. Agents | Project agents move to the plugin's roles | the owner |
| 6. Plan | The current work becomes `docs/design/plan.md` and `status.md` | the owner |
| 7. Check | Run the checks and prove delegation works (below) | |

## Stage 1: the audit

Read the repo before you touch it, and report a table of what exists, where it goes, and what's missing:

- **Design:** design docs, specs, wikis, notes. Which one is the source of truth? Is any of it outside the repo?
- **Process:** how things get designed and reviewed now. A good existing process stays, and only moves.
- **Tracking:** where tasks live, the task key, how a task moves.
- **Code:** engine, language, layout. What decides and what shows. What can be tested without the engine.
- **Proofs:** tests, bots, solvers, and the full and fast check commands.
- **Art and sound:** the style, the tools, any asset list. Don't run `choose-art-style` when a style is already set: record
  it in `docs/design/art.md`.
- **Agents:** anything in `.claude/agents/`, and the project detail each one holds.
- **Instructions:** `CLAUDE.md`, and any line that keeps work in the session.

## Moving the design

- **Design outside the repo** moves in, because `docs/design/` is the source of truth. Export it, import it once, and
  compare the two. Mark the old copy as frozen at its top only after that PR merges.
- **Generated docs** stop being generated: remove the headers and the script, and update whatever described them.
- **A large doc** splits one file per section. The routing table in `docs/design/README.md` names every file.
- Keep specs where they are, and link them from the section they serve.

## Moving agents

For each project agent: match it to a role, then move its project detail to `docs/team/<role>.md`. Keep only what's
specific to this game. Delete the old agent file once the role works. A job no role covers stays a project agent.

- **The playtester** can't read files. Its project detail goes in `docs/team/playtester-controls.md`, pasted word for word
  into its brief.
- **Plans** that name an old agent can stay as history. Note the new name in `CLAUDE.md`.

## Turning on delegation

A session keeps doing the work itself unless the setup says otherwise. Use the "Agents" section of `templates/CLAUDE.md`,
and "Who does what" from `templates/team/README.md`, filled with this game's kinds of work. Remove any line that says the
session keeps the design, or that names only some of the roles.

Then run the `choose-models` skill. If a project agent already had a model for a measured reason, keep it, and say why.

## Stage 7: the check

1. Copy `${CLAUDE_PLUGIN_ROOT}/scripts/check-team.py` and `check-design.py` to `scripts/`, unless the repo has its own, and
   run them from the test script. A path that isn't built yet goes in `PLANNED`.
2. Run the repo's full test script.
3. Check the install: the plugin must be at user scope, because a project-scope install is tied to one folder and is
   missing from every other worktree.
4. Start a fresh session in the repo and give it a piece of design work. It must name a role and delegate. If it doesn't,
   the instructions aren't clear enough yet.

## What to report

What moved and where, what the owner ruled, what's still a gap, anything left frozen outside the repo, and the next task.
