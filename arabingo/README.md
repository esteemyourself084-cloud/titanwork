# Arabingo

Arabic-learning app (stages → levels → units, lessons, quizzes, conversations, word lists, flashcards and a content studio).

Migrated from the published artifact: https://claude.ai/artifact/T3ehfd5MLocuet6CnFHqYh

- `index.html` — the full single-page app as published.
- Progress is kept in `localStorage` (`arabingo.progress.v2`).
- When hosted as an artifact it uses the runtime capabilities `db`, `downloads`, `sample` and `user`
  (db rules: `units` readable by viewers / writable by admin; `data/users/{self}` writable by each user).
  Opened as a plain file, those calls are unavailable and the app falls back to its built-in seed units.
