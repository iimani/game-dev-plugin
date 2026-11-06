# <Game>: Design Guideline

The design in one place, split by section.

## How to use this guideline

This is the game's design: what it is, how each system works, and what is built, approved, drafted or only proposed.

**Status labels.** Every rule or feature carries one:

| Label | Means |
| --- | --- |
| **Built** | in the code today, tested |
| **Approved** | the owner ruled it; not built yet |
| **Draft** | written by the builder, marked *(builder's call)*; the owner hasn't reviewed it |
| **Proposal** | an idea the owner hasn't approved; kept, not planned |

**How it's maintained.** This folder is the source of truth. Edit it by hand. A PR that changes a rule, a number or a status updates the matching section in the same change.
When this guideline and another document disagree, the newer owner ruling wins, and both are corrected in the same change.

**Tracking implementation.** This guideline is also the implementation tracker. An item's label moves Draft → Approved →
Built as decisions and code land.

### What to read for a task

Read this file first, always. Then read the files for your task, every one listed on its row.

| Task | Read |
| --- | --- |
| Planning, or picking the next task | `plan.md`, `status.md`, `decisions.md`, then the files for the task |
| Movement, controls, feel, tuning | `controls.md`, `tech.md` |
| A mechanic or a puzzle | `mechanics.md`, `tech.md`, `decisions.md` |
| Levels and generated content | `content.md`, `run.md`, `process.md`, `tech.md` |
| The run: sessions, saves | `run.md`, `progression.md`, `tech.md` |
| Upgrades and rewards | `progression.md`, `run.md` |
| Story and lore | `world.md` |
| Art | `art.md`, then `docs/art/catalogue.md` |
| Sound and haptics | `audio.md` |
| A playtest, a PR | `process.md` |

**Methods.** How to design each part, as stages with gates and proofs, is in `docs/process/README.md`.

## Vision

<One sentence.> **[Approved]**

### The feelings

<What the player should feel, in the owner's words.>

### Pillars

<Three to five. A design choice that serves none of them is cut.>

### Anti-goals

<What this game must never become. Each one is a test a change can fail.>

### House rules

<The rules every change keeps.>

## The files

| File | Section |
|---|---|
| [world.md](world.md) | World, story and lore |
| [run.md](run.md) | The core loop and run structure |
| [controls.md](controls.md) | Controls and movement |
| [mechanics.md](mechanics.md) | Mechanics |
| [content.md](content.md) | Levels and content |
| [progression.md](progression.md) | Progression |
| [art.md](art.md) | Art direction |
| [audio.md](audio.md) | Audio, haptics and feel |
| [tech.md](tech.md) | Tech and architecture |
| [process.md](process.md) | Process |
| [status.md](status.md) | Implementation status |
| [plan.md](plan.md) | Implementation plan |
| [decisions.md](decisions.md) | Open decisions |
