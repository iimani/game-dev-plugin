### Engine: Unity

**Version:** <fill: exact editor version, render pipeline, and the Unity binary path (on macOS inside `/Applications/Unity/Hub/Editor/<version>/`).>

**Run:** open the project in the editor and press Play. For a scripted launch use `-batchmode -projectPath .`.

**Test:** Unity Test Framework. `Unity -batchmode -nographics -projectPath . -runTests -testPlatform EditMode -testResults build/results.xml` (and `PlayMode`). Don't pass `-quit` with `-runTests`. Record the real command and call it from the project's test script.

**Export:** a static `BuildScript.Build` method run with `-executeMethod BuildScript.Build -buildTarget <target> -quit`. Commit the script.

**See it (playtester):** `-nographics` draws nothing. For screenshots run a player build with a window, or capture with `ScreenCapture.CaptureScreenshot` from a debug hook.

**Keep engine-free:** rules, generation and solvers in plain C# in an assembly definition with no `UnityEngine` reference, so EditMode tests run fast and without scenes.

**Pitfalls:** batch mode needs a valid license on the machine. Commit `.meta` files with their assets. Only one Unity process may open a project at a time.
