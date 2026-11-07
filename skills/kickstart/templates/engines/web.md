### Engine: Web (Canvas, WebGL or a JS framework)

**Version:** <fill: framework or library, bundler, language (TypeScript or JavaScript), and Node version.>

**Run:** `npm run dev` serves the game on localhost. Open it in the browser pane to play.

**Test:** a unit runner such as Vitest for rules and generation (`npm test`), and Playwright for the running game (`npx playwright test`). Record the real commands here.

**Export:** `npm run build` writes static files to `dist/`. Any static host serves them.

**See it (playtester):** the dev server in a browser needs no extra tool. Playwright's `page.screenshot()` captures a frame for checks that don't need a person.

**Keep engine-free:** rules, generation and solvers in plain modules with no DOM or canvas access, so tests run in Node. The render layer only reads state.

**Pitfalls:** a fixed time step keeps behaviour the same at any frame rate. Browsers block audio until the first user input, so the first screen needs one. Check the build, not just the dev server.
