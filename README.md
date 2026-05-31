# Skills Backup — Codex / Claude 双平台通用

本仓库备份全部自定义 Skill 资产，兼容 **OpenAI Codex** 与 **Anthropic Claude Code** 双平台。每个目录即一个独立 Skill，可在任一平台加载使用。

> Claude Code 的内置命令（`update-config`、`keybindings-help`、`fewer-permission-prompts`、`loop`、`claude-api`、`run`、`verify`、`review`、`security-review`、`code-review` 等）以及 Anthropic 官方插件 skill（`anthropic-skills:*`）不在此仓库中，无需备份。

## 双目录同步

`~/.claude/skills/` 和 `~/.codex/skills/` 指向同一个 Git 仓库（同一份文件，非独立 clone）。任一处修改后 commit + push 即可。

**Remote:** `https://github.com/deprive-Wang/skills-backup.git`

## 快速恢复

```bash
# Claude Code
git clone https://github.com/deprive-Wang/skills-backup.git ~/.claude/skills

# OpenAI Codex (同一个仓库)
git clone https://github.com/deprive-Wang/skills-backup.git ~/.codex/skills
```

---

## Skill 分类索引

### 开发工作流

| Skill | 描述 |
|-------|------|
| `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| `feature-dev` | Guided feature development with codebase understanding and architecture focus. Use when building new features, implementing complex changes, or anytime you need a structured 7-phase workflow from discovery to quality review. |
| `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| `workflow-code` | 代码工作流 — 从实验设计到代码交付的 engineering pipeline。当用户提到开发、实现、调试、重构、TDD、实验时使用。 |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |

### 代码质量

| Skill | 描述 |
|-------|------|
| `code-simplifier` | Simplify existing code without changing intended behavior. Use when the user asks to simplify code, reduce complexity, clean up logic, remove duplication, shrink a function, make implementation more direct, or review recent changes for unnecessary abstractions. |
| `improve-codebase-architecture` | Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable. |
| `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria. |
| `pr-review-toolkit` | Comprehensive PR review with 6 specialized agents covering code quality, simplification, comments, tests, error handling, and type design. Use before creating PRs or when you need a thorough multi-angle code review. |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation |
| `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |

### 调试与测试

| Skill | 描述 | 备注 |
|-------|------|------|
| `diagnose` | Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression. |  |
| `playwright` | Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script. |  |
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |  |
| `tdd` | Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development. | 与 `test-driven-development` 功能相同 |
| `tdd-mattpocock` | Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development. | 含测试反模式指南 |
| `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code | 与 `tdd` 功能相同 |
| `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. |  |

### Git 工具

| Skill | 描述 |
|-------|------|
| `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup |
| `git-guardrails` | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code. |
| `setup-pre-commit` | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing. |
| `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification |

### 文档生成

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-paperjsx` | Generate PPTX presentations, DOCX documents, XLSX spreadsheets, and PDF reports from structured JSON input using PaperJSX. | Codex 版本 |
| `doc` | Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks. |  |
| `markitdown` | Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more. |  |
| `minimax-docx` | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). Three pipelines: (A) create new documents from scratch, (B) fill/edit content in existing documents, (C) apply template formatting with XSD validation gate-check. MUST use this skill whenever the user wants to produce, modify, or format a Word document — including when they say "write a report", "draft a proposal", "make a contract", "fill in this form", "reformat to match this template", or any task whose final output is a .docx file. Even if the user doesn't mention "docx" explicitly, if the task implies a printable/formal document, use this skill. |  |
| `minimax-pdf` | Use this skill when visual quality and design identity matter for a PDF. CREATE (generate from scratch): "make a PDF", "generate a report", "write a proposal", "create a resume", "beautiful PDF", "professional document", "cover page", "polished PDF", "client-ready document". FILL (complete form fields): "fill in the form", "fill out this PDF", "complete the form fields", "write values into PDF", "what fields does this PDF have". REFORMAT (apply design to an existing doc): "reformat this document", "apply our style", "convert this Markdown/text to PDF", "make this doc look good", "re-style this PDF". This skill uses a token-based design system: color, typography, and spacing are derived from the document type and flow through every page. The output is print-ready. Prefer this skill when appearance matters, not just when any PDF output is needed. |  |
| `minimax-xlsx` | Open, create, read, analyze, edit, or validate Excel/spreadsheet files (.xlsx, .xlsm, .csv, .tsv). Use when the user asks to create, build, modify, analyze, read, validate, or format any Excel spreadsheet, financial model, pivot table, or tabular data file. Covers: creating new xlsx from scratch, reading and analyzing existing files, editing existing xlsx with zero format loss, formula recalculation and validation, and applying professional financial formatting standards. Triggers on 'spreadsheet', 'Excel', '.xlsx', '.csv', 'pivot table', 'financial model', 'formula', or any request to produce tabular data in Excel format. |  |
| `paperjsx` | Generate PPTX presentations, DOCX documents, XLSX spreadsheets, and PDF reports from structured JSON input using PaperJSX. | 与 `codex-paperjsx` 功能相同 |
| `pdf` | Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction. |  |
| `ppt-master` | AI-driven multi-format SVG content generation system. Converts source documents (PDF/DOCX/URL/Markdown) into high-quality SVG pages and exports to PPTX through multi-role collaboration. Use when user asks to "create PPT", "make presentation", "生成PPT", "做PPT", "制作演示文稿", or mentions "ppt-master". |  |
| `pptx-generator` | Generate, edit, and read PowerPoint presentations. Create from scratch with PptxGenJS (cover, TOC, content, section divider, summary slides), edit existing PPTX via XML workflows, or extract text with markitdown. Triggers: PPT, PPTX, PowerPoint, presentation, slide, deck, slides. |  |
| `Visiomaster` | Windows-first Visio diagram reconstruction workflow for flowcharts, architecture diagrams, and paper-style module figures. Reuses ppt-master style analysis and composition discipline on the front half, but outputs editable Visio .vsdx plus exported .svg and .png through a scene.json to Visio pipeline. Use when the user wants a diagram recreated as editable Visio shapes instead of a pasted screenshot or PPT-only result. |  |

### 写作与内容

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-changelog` | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation. |  |
| `codex-content-research-writer` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership. | Codex 版本 |
| `codex-email-polish` | Draft, rewrite, or condense emails with target tone, length, and audience; use for cold outreach, replies, status updates, or escalations where clarity and brevity matter. |  |
| `content-research-writer` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership. | 与 `codex-content-research-writer` 功能相同 |
| `edit-article` | Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft. |  |

### 学术与论文

| Skill | 描述 |
|-------|------|
| `academic-paper-polisher` | Academic paper writing assistant for Chinese and English manuscripts. Use when the user asks to polish, translate, rewrite, de-AI, reduce AIGC feel, expand, shorten, check logic, review a paper, analyze experiment results, draft figure/table captions, recommend academic plots, or design paper architecture figures for computer-science research text, LaTeX, Word-friendly Chinese prose, PDFs, or experiment data. |
| `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation. |
| `grill-me` | Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me". |
| `grill-with-docs` | Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions. |
| `hv-analysis` | 横纵分析法（Horizontal-Vertical Analysis）深度研究Skill。由数字生命卡兹克提出，融合了索绪尔的历时-共时分析、社会科学的纵向-横截面研究设计、商学院案例研究法与竞争战略分析的核心思想。 当用户想要系统性研究一个产品、公司、概念、技术或人物时使用。核心是双轴分析：纵轴追踪从诞生到当下的完整生命历程（以叙事故事呈现），横轴在当下时间截面上与竞品/同类进行系统性横向对比，最后交叉两条轴产出独到洞察。最终产出一份排版精美的PDF研究报告。 触发词包括但不限于：横纵分析、研究一下、帮我分析、深度研究、做个研究、调研一下、竞品分析、帮我看看这个东西怎么样、这个产品/公司/概念是怎么回事、帮我摸清楚、帮我搞懂、帮我做个deep research。 即使用户只是说"帮我了解一下XX"或"XX是什么来头"，只要上下文暗示需要系统性的深度研究（而非简单的概念解释），都应该触发。也适用于用户丢来一个产品名、公司名、技术名词说"帮我研究一下这个"的场景。 不要用于简单的名词解释（用户只是问"XX是什么"）、不要用于公众号写作（那个用khazix-writer）、不要用于纯标题摘要生成（用wechat-title）。 |
| `nature-paper2ppt` | Build a complete but efficient Nature-style Chinese PPTX presentation from a scientific paper, preprint, PDF, article text, abstract, figure legends, or reading notes. Use this skill whenever the user asks to make slides/PPT/PPTX for journal club, group meeting, paper sharing, thesis seminar, lab meeting, department report, or academic presentation from a research paper, not only medical papers. It identifies the paper type and argument, selects only the figures needed for the story, writes Chinese slide content and speaker notes, creates the actual .pptx deck, and performs lightweight verification with cross-platform Python tooling by default. |
| `nature-polishing` | Polish, restructure, or translate academic prose into Nature-leaning English using writing-strategy principles, curated Nature/Nature Communications article patterns, and phrase-level support from Academic Phrasebank. Use whenever the user asks to polish a manuscript paragraph, abstract, introduction, results, discussion, conclusion, title, methods section, or Chinese academic draft for publication-quality English. |
| `nature-reader` | Build full-paper Chinese-English side-by-side, figure/table-aware, source-grounded Markdown readers for journal or conference papers from PDF, DOI, arXiv, publisher HTML, or pasted text. Use whenever the user asks to translate or read a paper, make 中英文对照/原文对照/全文翻译解读, extract figures or tables into the right positions, preserve figure/table placement near relevant prose, or keep exact source anchors for every block. This skill must not degrade into a summary-only output unless the user explicitly asks for a summary. |
| `nature-response` | Draft, audit, or revise point-by-point reviewer response letters for Nature-family manuscript revisions. Use when the user provides reviewer comments, editor decision letters, revision notes, response drafts, or asks how to respond to major/minor revision requests, rebuttal letters, response to reviewers, peer-review reports, 审稿意见回复, 逐点回复, 修回信, 大修回复, 小修回复, or 如何回复 reviewer. |
| `nature-writing` | Draft, restructure, or plan Nature-style manuscript sections from author-provided claims, results, figures, notes, or Chinese drafts. Use when the user wants to write or rebuild an abstract, introduction, results narrative, discussion, conclusion, title, or full manuscript argument rather than only polish finished prose. |
| `workflow-thesis` | 论文工作流 — 从开题方案到论文终稿的完整 pipeline。当用户提到论文、开题、答辩、文献综述、润色、写作时使用。 |

### PaperSpine 论文工作流

| Skill | 描述 |
|-------|------|
| `paper-spine` | Internal orchestrator — users should use /paperspine to start a full workflow. |
| `paper-spine-audit` | Audits PaperSpine outputs for missing artifacts, shallow revisions, logic transfer, unsupported claims, and translation coverage. |
| `paper-spine-build` | Builds a paper or report from materials using the shared PaperSpine research, motivation, and rationale workflow. |
| `paper-spine-citation` | Builds a citation support bank for Introduction, Discussion, and background claims. |
| `paper-spine-humanize` | Reduces AI detection rates via tiered stylistic constraints mapped to real AIGC detection dimensions. Produces a teaching humanize_matrix.md. |
| `paper-spine-intake` | Collects PaperSpine workflow options and writes config for flash/pro, scene, language, and inputs. |
| `paper-spine-latex` | Handles LaTeX project assembly, figure placement, citations, labels, and compile-safe cleanup. |
| `paper-spine-research` | Researches target requirements, downloads reference materials, learns strong examples, and prepares motivation options. |
| `paper-spine-rewrite` | Rewrites an existing manuscript from confirmed motivation, research, paragraph-level rationale, and evidence. |
| `paper-spine-translate` | Produces the complete translation_zh/ package with row-by-row translation of all required artifacts and full-paper translation. |
| `paper-spine-ui` | Launches the PaperSpine external terminal configuration UI for Codex and Claude Code. |
| `paper-spine-update` | Checks and updates PaperSpine from GitHub while preserving global config; use for upgrades, latest-version checks, or local reinstall. |

### 会议与沟通

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-meeting-insights` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills. | Codex 版本 |
| `codex-meeting-notes` | Turn meeting transcripts or rough notes into crisp summaries with decisions, risks, and owner-tagged action items; use for Zoom/Meet/Teams transcripts, call notes, or long meeting chats to generate share-ready outputs. | Codex 版本 |
| `meeting-insights-analyzer` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills. | 与 `codex-meeting-insights` 功能相同 |
| `meeting-notes-and-actions` | Turn meeting transcripts or rough notes into crisp summaries with decisions, risks, and owner-tagged action items; use for Zoom/Meet/Teams transcripts, call notes, or long meeting chats to generate share-ready outputs. | 与 `codex-meeting-notes` 功能相同 |

### 知识管理

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-file-organizer` | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort. | Codex 版本 |
| `file-organizer` | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort. | 与 `codex-file-organizer` 功能相同 |
| `neat-freak` | End-of-session knowledge cleanup with OCD-level rigor — reconciles project docs (CLAUDE.md, README.md, docs/) and agent memory against the code so nothing rots. 会话结束后对项目文档和记忆进行洁癖级审查与同步。MUST trigger when the user says: "sync up", "tidy up docs", "update memory", "clean up docs", "/sync", "/neat", "同步一下", "整理文档", "整理一下", "更新记忆", "梳理一下", "收尾", "这个阶段做完了", "新人能直接上手", or any phrase suggesting a dev milestone where knowledge needs reconciliation. Also trigger when the user reports stale docs, conflicting memories, or wants a clean handoff to teammates or other agents. Bare "整理" / "tidy" with prior dev context counts — do not under-trigger. Cross-platform: works on Claude Code, OpenAI Codex, OpenCode, and OpenClaw. |  |
| `notion-research-documentation` | Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations. |  |
| `notion-spec-to-implementation` | Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them. |  |
| `obsidian-vault` | Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian. |  |

### 项目管理

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-create-plan` | Create a concise plan. Use when a user explicitly asks for a plan related to a coding task. | Codex 版本 |
| `create-plan` | Create a concise plan. Use when a user explicitly asks for a plan related to a coding task. | 与 `codex-create-plan` 功能相同 |
| `planning-with-file` | Record confirmed plans into a local Markdown file during Plan mode workflows. Use when the user wants plan confirmation output to be persisted as `plan.md`, especially for requests like "save the plan", "record the plan", "write the plan to a file", or when a custom workflow says that approved Plan mode output should automatically become a document. | 原名 `planing-with-file`，已修正拼写 |
| `qa` | Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session". |  |
| `to-issues` | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues. |  |
| `to-prd` | Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context. |  |
| `triage` | Triage issues through a state machine driven by triage roles. Use when user wants to create an issue, triage issues, review incoming bugs or feature requests, prepare issues for an AFK agent, or manage issue workflow. |  |

### 技能系统

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-skill-creator` | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations. |  |
| `codex-template-skill` | Skill 模板骨架。复制此目录并替换 frontmatter 和正文来创建新 skill。不要直接使用。 | 创建新 skill 的起始模板 |
| `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions |  |
| `workflow-combos` | 常用小组合 — 按场景打包的技能组合。当用户提到开会、见导师、整理、润色、周报时使用。 |  |
| `workflow-reference` | 全部技能速查手册。列出所有已安装技能及其一句话用途，按类别分组。当用户想知道"有哪些技能"、"这个能干嘛"时使用。 |  |
| `write-a-skill` | Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill. | 与 `write-a-skill-mattpocock` 功能相似 |
| `write-a-skill-mattpocock` | Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill. | Matt Pocock 版 |
| `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |  |

### 项目初始化

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-project-onboarding` | 首次打开项目时读取并创建或刷新根目录 `codex.md` 摘要。当用户希望 Codex 理解新代码库、生成项目简报、总结架构、记录启动命令或为后续会话创建入门笔记时使用。 | Codex 专用 |
| `init` | Codex-only project initialization workflow. Use when the user enters /init, asks to initialize a project, scan a project, generate codex.md, update codex.md, or create a project onboarding summary for Codex. Produces or updates a project-root codex.md, preferably in Chinese, covering goals, overview, structure, commands, constraints, special requirements, and maintenance notes. Claude does not need this skill. | Codex 专用 |

### 辅助工具

| Skill | 描述 | 备注 |
|-------|------|------|
| `caveman` | Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", or invokes /caveman. | 超压缩通信模式 (省 75% Token) |
| `spreadsheet-formula-helper` | Write and debug spreadsheet formulas (Excel/Google Sheets), pivot tables, and array formulas; translate between dialects; use when users need working formulas with examples and edge-case checks. |  |

### 未分类

| Skill | 描述 |
|-------|------|
| `git-auto` | 自动提交当前 git 项目变更：检测变更 → 更新 README（如有生成器） → git add → commit → pull --rebase → push |
| `paper-review` | Reviews thesis, manuscript, defense, and submission documents from a final-reviewer perspective by rendering native files to PDF and auditing layout, language, logic, figure-text consistency, data consistency, and citation support. Use when the user asks to check whether a paper can be printed/submitted, review a thesis or manuscript, inspect PDF/DOCX/PPT layout, compare text with figures/tables, or judge reviewer-facing risks. |
| `setup-matt-pocock-skills` | Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Run before first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs. |
| `ubiquitous-language` | Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms. Saves to UBIQUITOUS_LANGUAGE.md. Use when user wants to define domain terms, build a glossary, harden terminology, create a ubiquitous language, or mentions "domain model" or "DDD". |
| `zoom-out` | Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar with a section of code or need to understand how it fits into the bigger picture. |

---

## 重复/变体 Skill 说明

以下 skill 存在功能重复或变体关系，可根据偏好选择使用：

| 功能 | 可选 Skill | 说明 |
|------|-----------|------|
| TDD | `tdd` / `test-driven-development` | 功能完全相同 |
| TDD (进阶) | `tdd-mattpocock` | 含测试反模式指南 |
| 内容写作 | `content-research-writer` / `codex-content-research-writer` | Codex 版本针对 Codex 环境适配 |
| 文件整理 | `file-organizer` / `codex-file-organizer` | 同上 |
| 创建计划 | `create-plan` / `codex-create-plan` | 同上 |
| 会议洞察 | `meeting-insights-analyzer` / `codex-meeting-insights` | 同上 |
| 会议纪要 | `meeting-notes-and-actions` / `codex-meeting-notes` | 同上 |
| 文档生成 | `paperjsx` / `codex-paperjsx` | 同上 |
| Skill 创建 | `write-a-skill` / `write-a-skill-mattpocock` / `codex-skill-creator` | 三个变体 |

---

## 命名约定

- `codex-` 前缀: Codex 特定版本
- `nature-` 前缀: Nature 学术写作系列
- `paper-spine-` 前缀: PaperSpine 论文工作流系列
- 无前缀: 双平台通用或 Claude 原生
- 大写开头 (`Visiomaster`): 特殊命名约定

---

## 日常同步

### 修改 Skill 后推送

```bash
cd ~/.codex/skills   # 或 ~/.claude/skills
git add -A
git commit -m "更新: <skill名> -- <简述>"
git push
```

### 新电脑恢复

```bash
git clone https://github.com/deprive-Wang/skills-backup.git ~/.claude/skills
# 或
git clone https://github.com/deprive-Wang/skills-backup.git ~/.codex/skills
```

---

> README.md 由 `generate_readme.py` 自动生成，共收录 97 个 Skill。
