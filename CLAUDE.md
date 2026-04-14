# Skills backup repo

This repo is a git-backed backup of Claude skills, pushed to GitHub. The live skills that Claude Code loads live under `~/.claude/skills/` as symlinks pointing back into this repo.

## Layout

Each top-level folder here is a scope/namespace (e.g. `mathacademy/`). Inside it, a skill is any folder containing a `SKILL.md` file.

## Symlinking rules

- Only folders that contain a `SKILL.md` are skills and eligible for symlinking into `~/.claude/skills/`.
- Symlink the skill folder itself (and any assets it needs to function) — do **not** symlink parent/namespace folders or unrelated files.
- Never create symlinks automatically. Always ask the user first and confirm which folder to link and under what name in `~/.claude/skills/`.
- Symlink form: `ln -s /Users/chinmay/code/agency/skills/<path-to-skill-folder> /Users/chinmay/.claude/skills/<skill-name>`

## When creating a new skill

1. Create it inside this repo (under an appropriate namespace folder, or at the top level if it's standalone).
2. Ensure it has a `SKILL.md`.
3. Ask the user whether to symlink it into `~/.claude/skills/` and under what name.

## Upstream skills (`anthropic-skills/`)

The `anthropic-skills/` directory is a git submodule of [anthropics/skills](https://github.com/anthropics/skills), tracking its `main` branch. It is treated as read-only — do not edit files inside it; contribute upstream instead.

- **Layout:** individual skills live at `anthropic-skills/skills/<name>/` (one extra nesting level vs the top-level namespaces).
- **Licensing:** most skills are Apache 2.0; `docx`, `pdf`, `pptx`, `xlsx` are source-available (not OSS). Attribution is preserved automatically via `.gitmodules` and upstream's own `LICENSE`/`README`.
- **Symlinking:** same rule as above — only folders with `SKILL.md` qualify. Example:
  `ln -s /Users/chinmay/code/agency/skills/anthropic-skills/skills/<name> /Users/chinmay/.claude/skills/<name>`
- **Update from upstream:** `git submodule update --remote --merge anthropic-skills` then commit the new pointer.
