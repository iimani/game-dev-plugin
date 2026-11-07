# Telemetry

Use when: the game has an economy, a difficulty curve or a pacing target that someone will tune from real play.
Skip when: a game with no numbers to tune, such as a short puzzle game checked by solvers.

How a game records what happened in a run, so `game-dev:balance-analyst` measures from data instead of guesses.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline (`docs/design/README.md`): <fill: the guideline files on progression and difficulty>.

## The format

One JSON object per line, in a `.jsonl` file. The game writes it only when asked (<fill: the switch, such as an
environment variable or a debug flag>), to <fill: a folder that's git-ignored, such as `build/telemetry/`>. A player's build
never writes it.

| Field | Meaning |
|---|---|
| `t` | Milliseconds since the run started |
| `run` | An id, the same on every line of one run |
| `event` | One of the events below |
| `place` | Where, using the game's own ids (a room, level or screen) |

| Event | Extra fields | Written when |
|---|---|---|
| `run_start` | `seed`, `build` | A run begins |
| `place_enter`, `place_exit` | | The player enters or leaves a place |
| `death` | `cause` | The player loses health, a life or the run |
| `item_gain`, `item_spend` | `item`, `amount`, `balance` | Anything countable changes: currency, health, ammo |
| `run_end` | `result` | A run ends (`won`, `died` or `quit`) |

Add events the game needs, with the same fields. Keep ids stable, so runs from different builds line up.

## Reading it

`python3 scripts/telemetry-summary.py <folder>` gives, per place: visits, deaths, death rate and time spent (median and
90th percentile); per item: gained, spent and the lowest balance; and how runs ended. Few runs say little: the report
names the count, and the analyst gives the spread, never just the average.

## Where the runs come from

- **Bots and solvers** playing through the game's real logic: many runs, cheap, and the same rules every time.
- **A person playing** a build with the switch on: few runs, but they show what a bot can't.

Label which kind each number came from. A bot's numbers show where the rules are lopsided, and never how it feels.

## Open for the owner

- <fill: the targets the numbers are checked against, such as a death rate per place or a time to finish.>
