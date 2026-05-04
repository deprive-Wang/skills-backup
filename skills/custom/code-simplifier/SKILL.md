---
name: code-simplifier
description: Simplify existing code without changing intended behavior. Use when the user asks to simplify code, reduce complexity, clean up logic, remove duplication, shrink a function, make implementation more direct, or review recent changes for unnecessary abstractions.
---

# Code Simplifier

Simplify code while preserving behavior and keeping the change set tight.

## Workflow

1. Read the target files and understand the current behavior before editing.
2. Identify the highest-value simplifications first:
   - duplicated logic
   - unnecessary abstractions
   - over-long functions
   - indirect control flow
   - avoidable temporary state
   - dead code introduced by the change
3. Prefer the smallest safe rewrite that improves readability or maintainability.
4. Preserve public behavior unless the user explicitly asked for behavioral change.
5. Verify with tests when available. If no tests exist, use the smallest practical validation.

## Default Simplification Rules

- Prefer existing helpers over new helpers.
- Prefer fewer branches when readability improves.
- Prefer removing speculative flexibility.
- Prefer inlining single-use abstractions when they obscure intent.
- Do not rename widely used symbols unless the name itself is the problem.
- Do not refactor unrelated code just because it is nearby.

## Review Checklist

Before finishing, check:

- Is the new code shorter or clearer?
- Did the change preserve behavior?
- Did the change avoid touching unrelated files?
- Were any newly unused imports, variables, or helpers removed?
- Were tests run or a validation gap called out?

## Output Expectations

When this skill is active:

- explain the main simplification choices briefly
- keep edits surgical
- call out any behavior assumptions
- mention residual risks if validation is incomplete
