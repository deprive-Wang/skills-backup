---
name: feature-dev
description: Guided feature development with codebase understanding and architecture focus. Use when building new features, implementing complex changes, or anytime you need a structured 7-phase workflow from discovery to quality review.
---

# Feature Development

Implement new features following a systematic approach: understand the codebase deeply, identify and ask about all underspecified details, design elegant architectures, then implement.

## Core Principles

- **Ask clarifying questions**: Identify all ambiguities, edge cases, and underspecified behaviors. Wait for user answers before proceeding.
- **Understand before acting**: Read existing code patterns first.
- **Read files identified by agents**: After agents complete, read those files to build detailed context before proceeding.
- **Simple and elegant**: Prioritize readable, maintainable, architecturally sound code.
- **Use TodoWrite**: Track all progress throughout.

---

## Phase 1: Discovery

**Goal**: Understand what needs to be built.

**Actions**:
1. Create todo list with all phases.
2. If unclear, ask the user about the problem, what the feature should do, and constraints/requirements.
3. Summarize understanding and confirm with user.

---

## Phase 2: Codebase Exploration

**Goal**: Understand relevant existing code and patterns.

**Actions**:
1. Launch 2-3 code-explorer agents in parallel. Each agent should trace comprehensively, target a different aspect, and include a list of 5-10 key files to read.

   Example prompts:
   - "Find all features similar to [new feature]. Trace their implementation from entry points through business logic to data layer."
   - "Map the architecture of [relevant module]. Identify patterns, abstractions, naming conventions, and design decisions."
   - "Analyze how [existing feature] handles error cases, validation, and edge conditions."
   - "Identify the UI patterns and component hierarchy used in [related area]."

2. After agents return, **read all files identified by agents** to build deep understanding.
3. Present a comprehensive summary of findings and patterns.

---

## Phase 3: Clarifying Questions

**Goal**: Fill in gaps and resolve all ambiguities before designing.

**CRITICAL - DO NOT SKIP**

**Actions**:
1. Review codebase findings and original request.
2. Identify underspecified aspects:
   - Edge cases and error handling
   - Integration points with existing systems
   - Scope boundaries and constraints
   - Design preferences and conventions
   - Backward compatibility requirements
   - Performance or scalability concerns
3. **Present all questions to the user in a clear, organized list.**
4. **Wait for answers** before proceeding.

If the user says "whatever you think is best," provide a recommendation and get explicit confirmation.

---

## Phase 4: Architecture Design

**Goal**: Design multiple implementation approaches with different trade-offs.

**Actions**:
1. Launch 2-3 code-architect agents with different focuses:
   - **Minimal changes** - smallest possible diff, maximum reuse
   - **Clean architecture** - best long-term design, proper abstractions
   - **Pragmatic balance** - practical middle ground

2. Review all approaches and form an opinion (consider fix size, urgency, complexity, team context).
3. Present to user:
   - Summary of each approach
   - Trade-offs comparison
   - **Recommendation with reasoning**
   - Concrete implementation differences
4. **Ask user which approach they prefer.**

---

## Phase 5: Implementation

**Goal**: Build the feature.

**DO NOT START WITHOUT USER APPROVAL**

**Actions**:
1. Wait for explicit user approval.
2. Read all relevant files identified in previous phases.
3. Implement following chosen architecture.
4. Follow codebase conventions strictly.
5. Write clean, well-documented code.
6. Update todos as progress is made.

---

## Phase 6: Quality Review

**Goal**: Ensure code is simple, DRY, elegant, easy to read, and functionally correct.

**Actions**:
1. Launch 3 code-reviewer agents in parallel with different focuses:
   - **Simplicity / DRY / elegance** - Can the code be simpler without losing functionality?
   - **Bugs / functional correctness** - Are there edge cases, logic errors, or missing validation?
   - **Project conventions / abstractions** - Does the code follow established patterns?

2. Consolidate findings, identify highest severity issues.
3. **Present findings to user and ask what they want to do** (fix now, fix later, or proceed as-is).
4. Address issues based on user decision.

---

## Phase 7: Summary

**Goal**: Document what was accomplished.

**Actions**:
1. Mark all todos complete.
2. Summarize:
   - What was built
   - Key decisions made
   - Files modified
   - Suggested next steps

---

## Agent Reference

This workflow uses three specialized agents:

| Agent | Purpose | File |
|-------|---------|------|
| `code-explorer` | Traces feature implementations, maps architecture | `code-explorer.md` |
| `code-architect` | Designs architecture blueprints | `code-architect.md` |
| `code-reviewer` | Reviews code quality with confidence scoring | `code-reviewer.md` |

Launch these agents as needed during the workflow.
