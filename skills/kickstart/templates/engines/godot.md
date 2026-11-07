### Engine: Godot 4

**Version:** <fill: exact version, and whether the project uses GDScript or C#.>

**Run:** `godot --path . ` opens the game. `godot --headless --path . --quit-after 60` loads it with no window, which proves it starts.

**Test:** a test addon (GUT or GdUnit4) runs under `--headless`. GUT: `godot --headless -s addons/gut/gut_cmdln.gd -gdir=res://test -gexit`. Record the real command here and call it from the project's test script.

**Export:** `godot --headless --export-release "<preset>" build/<name>`. Needs `export_presets.cfg` committed and the export templates installed for this version.

**See it (playtester):** `--headless` uses a dummy renderer and draws nothing. For screenshots run with a window, and either drive it through the simulator or browser pane (web export) or save frames with `--write-movie out.avi --quit-after <frames>`.

**Keep engine-free:** rules, generation and solvers in plain scripts with no node access (`RefCounted`, not `Node`), so tests run without a scene tree.

**Pitfalls:** a missing `.import` or `.godot/` cache fails a fresh headless run, so run `godot --headless --import` once first. Never edit `.tscn` files by hand without re-opening them in the editor to check they load.
