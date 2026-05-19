---
name: init
description: Codex-only project initialization workflow. Use when the user enters /init, asks to initialize a project, scan a project, generate codex.md, update codex.md, or create a project onboarding summary for Codex. Produces or updates a project-root codex.md, preferably in Chinese, covering goals, overview, structure, commands, constraints, special requirements, and maintenance notes. Claude does not need this skill.
---

# Project Init

Use this skill to create or refresh the project-level `codex.md` in the current project root.

## Compatibility

- Codex-only: this skill is for Codex project onboarding workflows and Codex session continuity.
- Claude does not need this skill and should not treat `codex.md` as a required Claude memory file.
- Claude can follow its own project-memory, `CLAUDE.md`, or onboarding mechanism instead.

## Output Contract

- Create or update exactly one project-level `codex.md` in the detected project root.
- Prefer Chinese for all prose in `codex.md`; keep code identifiers, commands, API names, package names, file paths, and technical terms in English when clearer.
- Treat `codex.md` as long-term project context for future Codex sessions only.
- If `codex.md` already exists, update it incrementally and preserve user-authored content.
- Do not create README, CHANGELOG, ADR, or extra documentation unless the user explicitly asks.

## Workflow

1. Identify the project root from the current working directory, nearest VCS root, package manifest, build file, or explicit user-provided path.
2. Inspect the project with `rg --files`, relevant manifests, configuration files, entry points, tests, and existing documentation.
3. Codex-only helper: if available and useful, use `codex-project-onboarding` to gather project structure and technical context.
4. Read any existing `codex.md` before editing it.
5. If the user's intent, project goals, special requirements, business rules, or long-term preferences are unclear, ask concise clarification questions before writing those sections.
6. Generate or update `codex.md` with stable facts, confirmed requirements, and actionable development context.
7. For large projects, summarize primary paths and critical modules only; do not dump a complete file inventory.
8. Verify the final Markdown is coherent, non-duplicative, and useful as future session context.

## Clarification Questions

Ask questions when important project context cannot be inferred from files or prior conversation.

- Ask before inventing implementation goals, special requirements, business rules, target users, deployment assumptions, or long-term preferences.
- Prefer 1-3 high-signal questions at a time.
- Do not block on details that can be safely discovered from the repository.
- If the user is unsure, help them decide by offering concrete options or examples.
- Write unresolved items into `codex.md` as pending confirmation instead of guessing.

## Required Content

`codex.md` should include sections appropriate to the project. Use Chinese section titles in the output when possible. Cover these areas when discoverable:

- Implementation goals: project goals, current priorities, and user-confirmed delivery direction.
- Project overview: purpose, core scenarios, target users, and runtime context.
- Tech stack: languages, frameworks, runtime, key dependencies, package manager, and build system.
- Directory structure: core directories and module responsibilities; summarize main paths only.
- Development environment: dependency installation, environment variables, startup flow, and local services.
- Common commands: real dev, build, test, lint, format, typecheck, or equivalent commands.
- Architecture constraints: key decisions, data flow, system boundaries, external services, and integration points.
- Special requirements: business rules, user preferences, coding constraints, platform limits, compliance, or security notes.
- Testing strategy: test framework, test locations, recommended verification paths, and known coverage gaps.
- Known risks: open questions, fragile areas, and future maintenance notes.

## Update Rules

- Preserve manual notes unless they are demonstrably stale; when updating stale content, prefer revising in place over deleting.
- Do not invent commands, dependencies, APIs, environment variables, architecture decisions, or test results.
- Mark unknown items with the Chinese phrase meaning "to be confirmed" instead of guessing.
- Only include commands verified from project files or actually run during the session.
- Keep the document concise enough to be read at session start.

## Final Response

After completing the init task, report:

- The `codex.md` location.
- Whether it was created or updated.
- The major context areas added or refreshed.
- Any commands or checks that could not be verified.
