---
name: codex-project-onboarding
description: Read a project on first open and create or refresh a root `codex.md` summary. Use when the user wants Codex to understand a new codebase, generate a project briefing, summarize architecture, capture setup commands, or create onboarding notes for future sessions.
---

# Codex Project Onboarding

Understand a project on first contact and create a practical `codex.md` in the project root.

## Workflow

1. Inspect the repo before writing:
   - root files like `README`, `package.json`, `pyproject.toml`, `Cargo.toml`, `.env.example`
   - likely entry points
   - test configuration
   - docs and architecture notes
2. Build a concise mental model:
   - what the project does
   - major subsystems
   - how to run or test it
   - key external dependencies
   - conventions or gotchas
3. Create or update `codex.md` at the project root.
4. Keep `codex.md` useful for future coding sessions, not as a generic repo summary.

## Required `codex.md` Sections

Use these sections unless the repo clearly needs a different shape:

```md
# Codex Notes

## Project Summary

## Structure

## Run and Test

## Key Conventions

## Current Risks or Gaps

## Recommended First Actions
```

## Content Rules

- Keep the document short and high signal.
- Prefer repo-specific facts over generic advice.
- Include concrete commands when they can be discovered safely.
- Mention important unknowns instead of pretending certainty.
- Update the file in place if `codex.md` already exists and is stale.

## Guardrails

- Do not invent commands that were not supported by repo evidence.
- Do not dump long file inventories.
- Do not rewrite the whole document if only a small refresh is needed.
- If the repo is large, summarize the main paths and defer deep detail.
