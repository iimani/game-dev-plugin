---
name: choose-models
description: Choose which Claude model each game-dev role runs on: show the recommended model for each role with its reason and cost, let the owner change any of them, and record the choice in docs/team/README.md. Use during a kickstart or a migrate, or when the user wants to see or change the agents' models.
---

# Choose the models

Each role runs on the model in the "Model" column of `docs/team/README.md`. The session passes that value as `model` on
the Agent call, which overrides the role's own setting. So a game sets its models in its own repo, and the plugin needs no
change.

## Steps

1. Read the current "Model" column, if there is one, and which roles the game uses.
2. Show the owner the table below for those roles, with any current choice beside the recommendation, and the cost note.
3. Ask once: take the recommendation, or change some. The owner decides. Budget and how much a role's work matters here
   are theirs to weigh.
4. Write the choice to the "Model" column. A role can be `opus`, `sonnet`, `haiku`, `fable` or `inherit`, which uses the
   session's own model.
5. Check that the "Agents" section of `CLAUDE.md` tells the session to pass the column's value. Add the line if it's
   missing.

## Recommendations

*(Builder's call, except where it says measured.)* These are starting points. Change a role when its work shows it needs to.

| Role | Recommended | Why | Consider instead |
|---|---|---|---|
| `developer` | `opus` | Long tasks, where a mistake costs a rework | `sonnet` for small, well-planned tasks |
| `level-designer` | `opus` | Spatial reasoning, and proofs that have to hold | `sonnet` for variations on a proved level |
| `encounter-designer` | `opus` | Look and rules designed together, with costly stages | `fable` for the hardest designs |
| `narrative-writer` | `opus` | Voice is hard to fix later | `sonnet` for short hints and signs |
| `code-reviewer` | `opus` | A missed bug costs more than the review | `sonnet` for small diffs |
| `game-artist` | `sonnet` | Many assets, each judged against a render | `opus` for key art, or when a look won't come right |
| `sound-designer` | `sonnet` | Short sources, checked by measurement | |
| `balance-analyst` | `sonnet` | Scripts and arithmetic | `opus` for a question with no clear measure |
| `design-guardian` | `sonnet` | Comparing a change with the docs | `opus` for a large change |
| `playtester` | `sonnet` | Measured: a smaller model never left the first room and misread how moves work, and a larger one was stopped twice by a content filter. Don't change it without a test run | |

## The models

| Alias | Use it for | Cost per token, against Sonnet |
|---|---|---|
| `fable` | The hardest reasoning and longest autonomous work. Pick it by choice, never as a default | 5x |
| `opus` | Hard work where quality matters most | 2x |
| `sonnet` | Everyday work | 1x |
| `haiku` | Simple, high-volume work. No role here defaults to it | 0.05x |

Prices are the API's as of October 2026, and aliases follow the current generation, so this table doesn't go stale when a
new version ships. Check prices if they matter. On a subscription, the cost is in usage limits instead. Judge cost per
finished task: a cheaper model that needs two rounds isn't cheaper.
