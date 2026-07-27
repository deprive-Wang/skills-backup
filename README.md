# Skills Backup — Codex / Claude 双平台通用

本仓库备份全部自定义 Skill 资产，兼容 **OpenAI Codex** 与 **Anthropic Claude Code** 双平台。每个目录即一个独立 Skill，可在任一平台加载使用。

> Claude Code 的内置命令（`update-config`、`keybindings-help`、`fewer-permission-prompts`、`loop`、`claude-api`、`run`、`verify`、`review`、`security-review`、`code-review` 等）以及 Anthropic 官方插件 skill（`anthropic-skills:*`）不在此仓库中，无需备份。

## 双目录同步

`~/.cc-switch/skills/` 是唯一维护的 Git 仓库；`~/.claude/skills/` 和 `~/.codex/skills/` 都是指向它的 Junction（同一份文件，非独立 clone）。自定义 Skill 修改后，在 CCS 目录 commit + push；Codex 系统层 `.system/` 由官方维护，不纳入本仓库追踪。

**Remote:** `https://github.com/deprive-Wang/skills-backup.git`

## 快速恢复

```bash
# CCS 统一目录
git clone https://github.com/deprive-Wang/skills-backup.git ~/.cc-switch/skills

# 然后将 Claude / Codex skills 目录链接到 CCS 统一目录
```

---

## Skill 分类索引

### 开发工作流

| Skill | 描述 |
|-------|------|
| `feature-dev` | Guided feature development with codebase understanding and architecture focus. Use when building new features, implementing complex changes, or anytime you need a structured 7-phase workflow from discovery to quality review. |

### 代码质量

| Skill | 描述 |
|-------|------|
| `code-simplifier` | Simplify existing code without changing intended behavior. Use when the user asks to simplify code, reduce complexity, clean up logic, remove duplication, shrink a function, make implementation more direct, or review recent changes for unnecessary abstractions. |
| `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria. |
| `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always |

### 调试与测试

| Skill | 描述 | 备注 |
|-------|------|------|
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |  |
| `tdd` | Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development. | 保留版本；强调行为测试和垂直切片 |
| `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. |  |

### 文档生成

| Skill | 描述 | 备注 |
|-------|------|------|
| `doc` | Use when the task involves reading, creating, or editing `.docx` documents, especially when formatting or layout fidelity matters; prefer `python-docx` plus the bundled `scripts/render_docx.py` for visual checks. |  |
| `pdf` | Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction. |  |
| `ppt-master` | AI-driven multi-format SVG content generation system. Converts source documents (PDF/DOCX/URL/Markdown) into high-quality SVG pages and exports to PPTX through multi-role collaboration. Use when user asks to "create PPT", "make presentation", "生成PPT", "做PPT", "制作演示文稿", or mentions "ppt-master". |  |
| `Visiomaster` | Windows-first Visio diagram reconstruction workflow for flowcharts, architecture diagrams, and paper-style module figures. Reuses ppt-master style analysis and composition discipline on the front half, but outputs editable Visio .vsdx plus exported .svg and .png through a scene.json to Visio pipeline. Use when the user wants a diagram recreated as editable Visio shapes instead of a pasted screenshot or PPT-only result. |  |
| `skills/common/markitdown` | Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPubs and more. | 通用转换工具 |

### 学术与论文

| Skill | 描述 |
|-------|------|
| `academic-paper-polisher` | Academic paper writing assistant for Chinese and English manuscripts. Use when the user asks to polish, translate, rewrite, de-AI, reduce AIGC feel, expand, shorten, check logic, review a paper, analyze experiment results, draft figure/table captions, recommend academic plots, or design paper architecture figures for computer-science research text, LaTeX, Word-friendly Chinese prose, PDFs, or experiment data. |
| `nature-reader` | Build full-paper Chinese-English side-by-side, figure/table-aware, source-grounded Markdown readers for journal or conference papers from PDF, DOI, arXiv, publisher HTML, or pasted text. Use whenever the user asks to translate or read a paper, make 中英文对照/原文对照/全文翻译解读, extract figures or tables into the right positions, preserve figure/table placement near relevant prose, or keep exact source anchors for every block. This skill must not degrade into a summary-only output unless the user explicitly asks for a summary. |
| `paper-review` | Reviews thesis, manuscript, defense, and submission documents from a final-reviewer perspective by rendering native files to PDF and auditing layout, language, logic, figure-text consistency, data consistency, and citation support. Use when the user asks to check whether a paper can be printed/submitted, review a thesis or manuscript, inspect PDF/DOCX/PPT layout, compare text with figures/tables, or judge reviewer-facing risks. |

### 会议与沟通

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-meeting-insights` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills. | 保留版本 |
| `codex-meeting-notes` | Turn meeting transcripts or rough notes into crisp summaries with decisions, risks, and owner-tagged action items; use for Zoom/Meet/Teams transcripts, call notes, or long meeting chats to generate share-ready outputs. | 保留版本 |

### 知识管理

| Skill | 描述 |
|-------|------|
| `notion-research-documentation` | Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations. |
| `storage-analyzer` | macOS / Windows 只读存储分析助手（自动识别系统）。扫描整机磁盘占用，找出 占空间大户，把每一项分成 🟢可自动清理 / 🟡需人工判断 / 🔴谨慎清理 三级并给出 可执行处置方案，生成排版精美、可折叠、命令可一键复制的交互式 HTML 报告，并可 起本地服务在网页上一键删除（移废纸篓/直接删）。扫描全程只读。务必在以下场景 使用：用户说"存储分析""磁盘满了""C盘/硬盘满了""空间不够""清理空间" "清理磁盘""占空间""哪些东西占地方""帮我看看存储""看一下电脑存储/空间" "存储空间""电脑空间不够""内存满了/不够/不足""看下内存/存储"（中文口语里 "内存"常指存储空间）"storage analysis""disk cleanup""清缓存""磁盘清理"； 或用户抱怨电脑没空间、想知道什么东西吃硬盘、想要清理建议时。注意：若用户明确 指运行内存/RAM（如"哪个进程吃内存""内存占用高"想看活动监视器），那是 RAM 不是存储，不属于本 skill。 |

### 项目初始化

| Skill | 描述 | 备注 |
|-------|------|------|
| `codex-project-onboarding` | 首次打开项目时读取并创建或刷新根目录 `codex.md` 摘要。当用户希望 Codex 理解新代码库、生成项目简报、总结架构、记录启动命令或为后续会话创建入门笔记时使用。 | Codex 专用 |

### 辅助工具

| Skill | 描述 | 备注 |
|-------|------|------|
| `caveman` | Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", or invokes /caveman. | 超压缩通信模式 (省 75% Token) |

---

## 精简说明

同一类能力只保留一个主要入口，官方系统 skill 位于 `.system/`，不列入自定义索引：

| 功能 | 可选 Skill | 说明 |
|------|-----------|------|
| 调试与 TDD | `systematic-debugging` / `tdd` | 分别负责根因调试与测试驱动开发 |
| 科研展示 | `ppt-master` / `Visiomaster` | 分别负责 PPT 与可编辑 Visio 图 |
| 文档处理 | `doc` / `pdf` | 分别负责 DOCX 与 PDF |

---

## 命名约定

- `codex-` 前缀: Codex 特定版本
- `nature-` 前缀: Nature 学术写作系列
- 无前缀: 双平台通用或 Claude 原生
- 大写开头 (`Visiomaster`): 特殊命名约定

---

## 日常同步

### 修改 Skill 后推送

```bash
cd ~/.cc-switch/skills
git add <明确的 Skill 路径> README.md generate_readme.py
git commit -m "更新: <skill名> -- <简述>"
git push
```

### 新电脑恢复

```bash
git clone https://github.com/deprive-Wang/skills-backup.git ~/.cc-switch/skills
# 再把 ~/.claude/skills 和 ~/.codex/skills 链接到 ~/.cc-switch/skills
```

---

> README.md 由 `generate_readme.py` 自动生成，共收录 21 个 Skill。
