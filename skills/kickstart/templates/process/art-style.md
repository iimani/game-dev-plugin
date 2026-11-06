# Choosing an art style

Use when: a new game needs its look, or an existing game is changing its art tool. Every game needs this once.

Status: **[Draft]**. *(Builder's call)* on anything the owner didn't say.

Read with the design guideline: `art.md`, `tech.md` (the engine, the screen), and the vision's feelings and anti-goals.

## 1. What good looks like

- **The style serves the feeling.** It's chosen from the vision's feelings, not from what's easy to make.
- **It reads at game size.** The player, hazards and goals are clear on the real screen, in the game's light, with the
  HUD on.
- **The team can make all of it.** One test asset is easy. A whole game needs hundreds, so judge what the tool does for
  variants, animation and repeat work.
- **The engine can use it.** The tool's output goes into the chosen engine without a manual step.
- **It's one style.** Mixed tools are fine if they share a palette, a light and a level of detail.

## 2. The tools

Each one is art as code: a small source file builds the assets, with previews an agent can look at. All are MIT licensed
and need Node 22.18 or later. Install one as a skill by cloning it to `~/.claude/skills/<name>`, then run `npm install`
where its README asks. Check its README first: it's the source of truth.

| Tool | Makes | Fits | Output | Watch for |
|---|---|---|---|---|
| [pxl](https://github.com/uilianks/pxl) | Pixel art: sprites, tiles, sheets, animated GIFs | 2D, retro, crisp at a fixed scale | PNG, sprite sheets with JSON, GIF | Fix the pixel scale early: everything hangs on it |
| [vex](https://github.com/uilianks/vex) | 2D vector art: characters, UI, scenes, animation strips | Flat, cartoon, clean shapes, smooth scaling | SVG, PNG, sprite atlases with JSON | Flat shapes need strong silhouettes and a tight palette |
| [kiln](https://github.com/uilianks/kiln) | Low-poly and voxel 3D: characters, props, dioramas | 3D games in Godot, Unity, Unreal or Three.js | GLB, previews | Blender is only for beauty renders and videos |
| [loom](https://github.com/uilianks/loom) | Seamless textures and PBR materials | Surfaces for 3D, with kiln or alone; tiling 2D backgrounds | Albedo, normal, height, roughness, AO, ORM, emissive | It makes surfaces, not objects: it pairs with another tool |
| [chirp](https://github.com/uilianks/chirp) | Sound effects and music, not art | Every game's sound | WAV, OGG, looping songs, audio sprites | An agent can't hear: it measures, and the owner listens |

A style with no tool here (hand-painted, photo-based) is allowed. It needs a named source of assets, and the owner
accepts that an agent can't make them.

## 3. The stages

| Stage | What | Tool | Gate |
|---|---|---|---|
| 1. Brief | The feelings, the screen size, the camera, the engine, what must read at a glance | the vision, `tech.md` | |
| 2. References | Three to five looks in words: what each gets right for this game | | the owner picks two or three |
| 3. Fit | For each pick: which tool, what it costs across the whole game, what it can't do | the table above | |
| 4. Test asset | The same scene in each pick: the player, a hazard, a goal, a floor, on the real screen size. `game-artist` makes them, briefed as a style test | the tools | |
| 5. Judge | Each test at game size, in the game's light, with a mock HUD. Say plainly what's weak in each | the renders | the owner rules |
| 6. Rules | The pixel scale or shape language, palette, light, what's reserved for hazards and goals | `art.md` | the owner |
| 7. Contract | The asset contract: names, sizes, anchors, states, layers. A build that checks the rules | `docs/art/catalogue.md` | |

## 4. The proof

The art build fails when an asset breaks a colour or size rule. Test assets are judged in a mock lit like the game, never
as sprites on a blank background.

## 5. Numbers to set

- Screen size and art resolution: `<fill: ...>`
- Pixel scale or tile size, or polygon budget: `<fill: ...>`
- Palette size and the colours reserved for meaning: `<fill: ...>`

## 6. Lessons

- Judge art under the game's light. A dark ambient can make an asset that looks fine as a sprite vanish.
- Anything that must read in the dark goes on an unlit layer.
- A cue that reads in a close-up can fail at game zoom. Check at the real screen size.
- Let art swap in by levels, from a placeholder drawn in code to the final asset, so the game never waits on art.

## 7. Open for the owner

- `<fill: open questions from the brief>`
