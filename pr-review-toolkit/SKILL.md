---
name: pr-review-toolkit
description: Comprehensive PR review with 6 specialized agents covering code quality, simplification, comments, tests, error handling, and type design. Use before creating PRs or when you need a thorough multi-angle code review.
---

# PR Review Toolkit

A comprehensive collection of 6 specialized review agents for thorough pull request analysis. Each agent focuses on a specific dimension of code quality.

## Six Review Agents

| Agent | Focus | When to Use |
|-------|-------|------------|
| `code-reviewer` | Code quality & conventions | General review of any code changes |
| `code-simplifier` | Code clarity & refactoring | Simplify recently written/modified code |
| `comment-analyzer` | Comment accuracy & maintainability | Verify documentation comments match code |
| `pr-test-analyzer` | Test coverage quality | Check if tests adequately cover new code |
| `silent-failure-hunter` | Error handling & silent failures | Audit error handling and catch blocks |
| `type-design-analyzer` | Type quality & invariants | Review new types/interfaces/classes |

## How to Use

### Quick - single agent

Ask for a specific review type and the agent auto-triggers:

- "Can you check if the tests cover all edge cases?" --> `pr-test-analyzer`
- "Review the error handling in the API client" --> `silent-failure-hunter`
- "Are the comments accurate in this file?" --> `comment-analyzer`
- "Review the new types I just added" --> `type-design-analyzer`
- "Simplify the code I just wrote" --> `code-simplifier`

### Comprehensive - full PR review

```
"I'm ready to create this PR. Please:
1. Review test coverage
2. Check for silent failures
3. Verify code comments are accurate
4. Review any new types
5. General code review
6. Simplify where possible"
```

### Parallel or sequential

You can run multiple agents in parallel for independent reviews:
```
"Run pr-test-analyzer and comment-analyzer in parallel"
```

Or sequentially when one review should inform the next:
```
"First review test coverage, then check code quality"
```

## Recommended Workflow

1. **Write code**
2. **code-reviewer** - General quality check
3. **silent-failure-hunter** - Fix error handling issues
4. **pr-test-analyzer** - Add missing tests
5. **comment-analyzer** - Fix documentation
6. **code-simplifier** - Polish and refine
7. **Create PR**

## Confidence Scoring

All agents use confidence-based filtering to report only meaningful issues:

- **pr-test-analyzer**: test gaps rated 1-10 (10 = critical)
- **type-design-analyzer**: four dimensions on a 1-10 scale
- **code-reviewer**: issues scored 0-100 (>= 80 only)
- Other agents use severity tiers (Critical/Important/Minor)

## Agent Files

Each agent is defined in a separate markdown file in this directory:
- `code-reviewer.md`
- `code-simplifier.md`
- `comment-analyzer.md`
- `pr-test-analyzer.md`
- `silent-failure-hunter.md`
- `type-design-analyzer.md`
