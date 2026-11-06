# Designing sound

Use when: designing anything the player hears: effects, ambience, music.
Skip when: never for a game with sound. A silent game keeps only the rule that nothing depends on sound.

The project's audio tool is chosen at kickstart: <fill: tool>. This method is the same for any tool and any style.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline (`docs/design/README.md`): <fill: the guideline files on audio and scripted moments>.
Where they disagree, the guideline and the owner's newer ruling win.

## 1. What good sound does

- **It's designed, not added at the end.** Decide early whether audio is a pillar of this game.
- **It never carries information alone.** Everything audible is also visible. Sound is a shortcut. This is a default the
  owner can change, for a game built on listening.
- **A sound means one thing everywhere.** A family keeps its pitches and voices wherever it's used.
- **It decides nothing.** Sounds react to game events, as haptics do. Nothing about a sound changes game state.
- **It's checked without ears,** then by the owner's.

## 2. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | The event, the feeling, the visible twin, whether it loops | the catalogue row | |
| 2. Reference | The nearest sound in the family; its pitch, length and loudness | the audio catalogue | |
| 3. Build | The sound, with its variants | <fill: audio tool> | |
| 4. Check | Peak, loudness, brightness, no clipping; pitch over time where it matters | <fill: audio tool's report> | |
| 5. Wire | The game plays it on the event, and a missing file falls back to silence | <fill: audio code> | |
| 6. Listen | The owner on a device, with the mix | a device | the owner |
| 7. Review | Does it still pair with its visible twin; is the mix level | the catalogue | |

A blind playtest agent can't hear. Sound is the owner's call on a device, every time. Say what a still or a log can't
show.

## 3. The catalogue

`<fill: path to the audio catalogue>`: one row per sound.

| Field | Meaning |
|---|---|
| Name | unique, `<family>_<what>` |
| Event | the game event or state that plays it |
| Loudness target | in the mix's units |
| Loop | yes or no, and its length |
| Visible twin | the cue it pairs with |

A change that adds a sound adds its row, and checks it against "everything audible is also visible".

## 4. Families, in order of build

1. The **seam:** one audio director fed by the game's events.
2. **Sounds that carry a rule,** if the game has any.
3. **Movement and feedback:** the player's actions, the world, hazards, UI.
4. **The score:** short loops from stems, with swells at the big moments.

## 5. The proof

The tool's measurements, before anyone listens. A test or review that every row has its visible twin.

## 6. Numbers and technical rules

- Formats per platform: <fill: check what the target plays, and whether its compressed format loops seamlessly>.
- Size budget: <fill: uncompressed audio is large, so keep music beds to short loops built from stems>.
- A missing file falls back, and never crashes.
- Haptics are events like sounds, and they don't replace the visible twin.

## 7. Lessons

- A sound can't carry a cue the screen lacks. Whatever a sound helps with, the visuals must also show.
- Anything timed by sound is also shown, such as a glow that fades.
- A silent tool sees only the visual cue. When a blind run stalls, check what the screen shows before blaming the design.

## 8. Open for the owner

- The sound style.
- How adaptive the score is.
- Whether sound gets an accessibility setting.
