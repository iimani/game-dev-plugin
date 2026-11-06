# Designing the HUD, the camera and feedback

Use when: designing what the player sees about the game itself: the HUD, on-screen controls, the camera, banners, hit and
danger feedback, haptics.
Skip when: never fully. A game with no HUD still needs the feedback rules.

This is where "readable on the real screen" is decided. On a phone, thumbs cover a large part of it.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline (`docs/design/README.md`): <fill: the guideline files on controls, art and audio>. Where
they disagree, the guideline and the owner's newer ruling win.

## 1. What good feedback does

- **Nothing important sits under a thumb or the HUD** where the player stands to use it.
- **Every action has an answer.** A hit shows what touched you, a loss shows in the HUD, and a button that can do nothing
  says so.
- **Every danger has a tell,** long enough to react to, performed by the thing itself.
- **A display ends with its cause.** A preview, a mark or a glow that outlives what made it reads as a bug.
- **Colours mean one thing.** Reserve each signal colour, and keep it off everything else.
- **Cues read by shape at the game's zoom,** on the real screen.
- **The camera follows the player** and holds at the level's edges, clear of the HUD and the safe area.
- **The frame rate holds.** <fill: target>.

## 2. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | What the player must know at this moment, and from what | the task | |
| 2. Layout | Where it sits on the real screen, against the controls and the safe area | <fill: layout code, clearance check, screen mock> | |
| 3. Mock | The real screen at the game's zoom, HUD and controls drawn on | <fill: screen mock tool> | the owner, for a new element |
| 4. Core | The state the view shows is decided in the game's logic | <fill: test runner> | |
| 5. View | A view takes that state and draws it | <fill: where views live> | |
| 6. Device | The owner on the target device: reading, hands, frame rate | a device | the owner |
| 7. Playtest | Text hidden by controls or HUD; unknown symbols | a blind playtest | the verdict |

## 3. Rules

- **The logic decides, the view shows.** A feedback rule, such as what greys out or what a hit names, lives in the game's
  logic, with a test.
- **Geometry is testable.** Keep control layout and text clearance as pure functions, and test them.
- **Haptics follow events.** They don't replace a visible cue.
- **Set one style** for each kind of on-screen text: <fill: banners, status lines>.

## 4. The proof

Tests for layout, text clearance and camera framing, before a person looks. A mock of the real screen at the game's zoom.

## 5. Numbers

- Shortest danger tell: <fill: seconds>.
- Smallest detail and gap in a cue at the game's zoom: <fill: points, pixels>.
- Frame rate: <fill: target>.

## 6. Lessons

- A cue can read in a close-up and fail on the device, when the zoom merges its gaps. Check every cue at the real zoom.
- Anything anchored outside the camera's frame doesn't exist. Check it with the camera where the player's will be.
- Unseen hits feel unfair. Every attack warns.
- An action that fails silently reads as a broken button.
- An effect or mask left active while it shows nothing can break other rendering. Hide effect nodes when they're idle.

## 7. Open for the owner

- Whether left-handed players get a mirrored layout.
- Whether the HUD hides itself in calm moments.
