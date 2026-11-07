### Engine: Unreal Engine 5

**Version:** <fill: exact engine version, C++ or Blueprint, and the editor install path.>

**Run:** open the `.uproject` in the editor, or `UnrealEditor <Project>.uproject -game` for a standalone window.

**Test:** the automation system. `UnrealEditor-Cmd <Project>.uproject -ExecCmds="Automation RunTests <Prefix>; Quit" -unattended -nullrhi -nosplash -log`. Record the real command and call it from the project's test script.

**Export:** `RunUAT BuildCookRun -project=<Project>.uproject -platform=<platform> -cook -stage -pak -archive -archivedirectory=build`.

**See it (playtester):** `-nullrhi` renders nothing. For screenshots run with a window, and use the `HighResShot <width>x<height>` console command.

**Keep engine-free:** rules, generation and solvers in a plain C++ module with no `UObject` types, so they can be tested without a world. Blueprint-only games keep rules in data tables.

**Pitfalls:** builds are slow, so run the smallest test prefix that proves the change. Don't commit `Intermediate/`, `Saved/` or `Binaries/`.
