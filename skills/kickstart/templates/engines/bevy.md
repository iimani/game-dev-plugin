### Engine: Bevy (Rust)

**Version:** <fill: Bevy version (its API changes between releases), and Rust toolchain.>

**Run:** `cargo run` for development, `cargo run --release` to judge performance.

**Test:** `cargo test`. Build a `World` or `App` with `MinimalPlugins` and step it with `app.update()`, so tests need no window or GPU.

**Export:** `cargo build --release`. For the web, add the `wasm32-unknown-unknown` target and build with `trunk`. Record which targets this game ships.

**See it (playtester):** run with a window, or use Bevy's screenshot support (`Screenshot::primary_window()` with `save_to_disk` in recent versions) and read the file.

**Keep engine-free:** rules, generation and solvers in a plain library crate, or modules with no `bevy` types, so tests are ordinary Rust tests.

**Pitfalls:** debug builds are very slow, so enable `opt-level = 1` for the project and `3` for dependencies in `Cargo.toml`. Pin the Bevy version, since upgrades break code.
