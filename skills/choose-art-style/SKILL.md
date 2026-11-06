---
name: choose-art-style
description: Choose a game's art style and art tool with the owner: shortlist styles, make the same test asset in each, judge them on the game's real screen, and record the ruling. Use during a kickstart, or when a game's art style or art tool is being chosen or changed.
---

# Choose an art style

Follow `${CLAUDE_PLUGIN_ROOT}/skills/kickstart/templates/process/art-style.md`. If the project has its own
`docs/process/art-style.md`, that copy wins.

Stop at each gate for the owner. When the style is ruled:
1. Record the ruling, with the owner's words, in `docs/design/art.md`, marked **[Approved]**.
2. Write `docs/team/game-artist.md`: the tool, the sources, the build, and how to judge the art. Name the same tool in
   `docs/team/encounter-designer.md` if the game uses that role.
3. Start the asset contract at `docs/art/catalogue.md`, with the test asset as its first row.
4. Tell the owner to install the tool if it's missing. Each tool's install is in the method's table.
