---
name: planing-with-file
description: Record confirmed plans into a local Markdown file during Plan mode workflows. Use when the user wants plan confirmation output to be persisted as `plan.md`, especially for requests like "save the plan", "record the plan", "write the plan to a file", or when a custom workflow says that approved Plan mode output should automatically become a document.
---

# Planing With File

Persist the final approved plan from a Plan mode workflow into `plan.md` in the current working directory.

## Workflow

1. Use this skill only when the task is operating in Plan mode or the user explicitly wants plan output saved to a file.
2. Let the normal planning workflow happen first. Do not write `plan.md` before the plan is shown and confirmed as correct.
3. After the user confirms the plan, create or update `plan.md` in the current workspace.
4. Write only the confirmed plan. Do not include internal reasoning, discarded alternatives, or tool-call metadata.
5. Keep the document concise and readable Markdown.

## File Rules

- Default path: `plan.md` in the current working directory.
- If `plan.md` already exists, replace its contents with the latest confirmed plan unless the user explicitly asks to append history.
- Add a title line `# Plan`.
- Add a short confirmation note with the current date if it is known from context.
- Render the plan as a numbered list when the confirmed plan is step-based.
- Preserve user wording where practical, but normalize into clear action-oriented steps.

## Output Template

Use this structure unless the user requests a different format:

```md
# Plan

Confirmed on: YYYY-MM-DD

1. First step
2. Second step
3. Third step
```

## Guardrails

- Do not claim the file was written unless it was actually created or updated.
- If the plan was not confirmed yet, wait and ask for confirmation through the normal Plan mode flow instead of writing the file early.
- If the user names a different file, follow the user's filename instead of `plan.md`.
