---
name: setup-codex-project
description: Create the standard Codex project configuration scaffold in the current project directory. Use when the user invokes this skill to initialize a project for Codex, create .codex/agents, .agents/skills, AGENTS.md, and .codex/config.toml, or asks to set up Codex project config files.
---

# Setup Codex Project

## Workflow

Set up the current project directory with the standard Codex scaffold requested by the user.

1. Treat the current working directory as the project root unless the user explicitly names another path.
2. Run `python3 scripts/setup_codex_project.py` from this skill, passing `--project-root <path>` when the target is not the current working directory.
3. Report the created or already-existing paths.

## Required Result

Ensure these directories and files exist:

```text
.codex/agents/
.agents/skills/
AGENTS.md
.codex/config.toml
```

Use idempotent creation only. Do not overwrite existing file contents. If `AGENTS.md` or `.codex/config.toml` already exists, preserve it exactly.

## Direct Command Equivalent

The script is equivalent to running these commands from the project root:

```bash
mkdir -p .codex/agents
mkdir -p .agents/skills
touch AGENTS.md
touch .codex/config.toml
```
