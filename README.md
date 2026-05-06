# Skills Backup — Codex / Claude 双平台通用

本仓库备份全部 AI 编程助手的 Skill 资产，兼容 **OpenAI Codex** 与 **Anthropic Claude Code** 双平台。每个目录即一个独立 Skill，可在任一平台加载使用。

## 快速恢复

在新电脑上 clone 后，将整个目录复制到对应平台的 skills 路径：

- **Claude Code**: `~/.claude/skills/`
- **OpenAI Codex**: `~/.codex/skills/`

或使用 `Skill` 工具逐个加载。

---

## Skill 分类索引

### 🔧 开发工作流

| Skill | 描述 |
|-------|------|
| `feature-dev` | 7 阶段功能开发工作流 (Discovery→Exploration→Questions→Architecture→Implementation→Review→Summary) |
| `subagent-driven-development` | 多 Agent 并行开发调度 |
| `executing-plans` | 按既定计划逐步执行开发 |
| `dispatching-parallel-agents` | 无依赖任务并行分发 |
| `writing-plans` | 多步骤任务执行前先写实现计划 |
| `workflow-code` | 代码工作流总入口 (实验设计→代码交付) |

### ✅ 代码质量

| Skill | 描述 |
|-------|------|
| `pr-review-toolkit` | 6 Agent 全面 PR 审查 (质量/精简/注释/测试/错误处理/类型设计) |
| `review` | Pull Request 代码审查 |
| `simplify` | 代码精简审查 (复用/质量/效率) |
| `security-review` | 安全漏洞审查 |
| `requesting-code-review` | 主动请求代码审查的工作流 |
| `receiving-code-review` | 处理审查反馈 (验证而非盲从) |
| `verification-before-completion` | 完成前先验证 (证据优于断言) |
| `karpathy-guidelines` | Karpathy 编码指南 (减少 LLM 常见错误) |
| `improve-codebase-architecture` | 代码库架构深化改进 |

### 🐛 调试与测试

| Skill | 描述 |
|-------|------|
| `systematic-debugging` | 系统化调试 (根因→假设→验证→修复) |
| `diagnose` | 严格诊断循环 (复现→缩小→假设→插桩→修复→回归) |
| `test-driven-development` | TDD 红-绿-重构循环 |
| `tdd` | TDD (含 deep-modules/interface-design/mocking) |
| `tdd-mattpocock` | TDD (Matt Pocock 版，含测试反模式) |
| `webapp-testing` | Playwright Web 应用测试 |

### 📦 Git 工具

| Skill | 描述 |
|-------|------|
| `git-guardrails` | 拦截危险 Git 命令 (push/force reset/clean 等) |
| `finishing-a-development-branch` | 开发分支收尾 (合并/PR/清理) |
| `using-git-worktrees` | 隔离 Git Worktree 工作流 |
| `setup-pre-commit` | Husky pre-commit hooks 配置 |

### 📄 文档生成

| Skill | 描述 |
|-------|------|
| `minimax-docx` | 专业 DOCX 文档 (OpenXML SDK .NET) |
| `minimax-pdf` | 专业 PDF 设计排版 |
| `minimax-xlsx` | Excel 电子表格创建与分析 |
| `pptx-generator` | PowerPoint 演示文稿生成 |
| `doc` | DOCX 基础读写 |
| `pdf` | PDF 基础读写 |
| `paperjsx` | JSON→文档 (PPTX/DOCX/XLSX/PDF) |
| `codex-paperjsx` | PaperJSX (Codex 版本) |

### ✍️ 写作与内容

| Skill | 描述 |
|-------|------|
| `content-research-writer` | 内容写作 + 研究 + 引用 |
| `codex-content-research-writer` | 同上 (Codex 版本) |
| `edit-article` | 文章编辑与润色 |
| `codex-changelog` | 从 Git 提交自动生成 Changelog |
| `codex-email-polish` | 邮件起草/改写/压缩 |

### 🎓 学术与论文

| Skill | 描述 |
|-------|------|
| `workflow-thesis` | 论文全流程 (开题→文献综述→写作→答辩) |
| `hv-analysis` | 横纵分析法深度研究 (双轴分析→PDF 报告) |
| `brainstorming` | 创意构思与设计探索 |
| `grill-me` | 方案质询 (追问至全面理解) |
| `grill-with-docs` | 方案质询 + 文档同步更新 |

### 🎙️ 会议与沟通

| Skill | 描述 |
|-------|------|
| `meeting-insights-analyzer` | 会议分析 (行为模式/沟通洞察) |
| `codex-meeting-insights` | 同上 (Codex 版本) |
| `meeting-notes-and-actions` | 会议纪要 + 待办 |
| `codex-meeting-notes` | 同上 (Codex 版本) |

### 🧠 知识管理

| Skill | 描述 |
|-------|------|
| `neat-freak` | 会话后文档与记忆洁癖级同步 |
| `obsidian-vault` | Obsidian 笔记搜索与管理 |
| `notion-research-documentation` | Notion 跨源研究→结构化文档 |
| `notion-spec-to-implementation` | Notion Spec→实现计划+任务 |
| `file-organizer` | 智能文件整理 |
| `codex-file-organizer` | 同上 (Codex 版本) |

### 📋 项目管理

| Skill | 描述 |
|-------|------|
| `to-issues` | 计划/PRD 拆分为独立 Issue |
| `to-prd` | 对话上下文→PRD |
| `triage` | Issue 状态机分类 |
| `qa` | 对话式 QA→GitHub Issue |
| `create-plan` | 快速创建实现计划 |
| `codex-create-plan` | 同上 (Codex 版本) |
| `planing-with-file` | 计划持久化为 plan.md |

### ⚙️ 技能系统

| Skill | 描述 |
|-------|------|
| `using-superpowers` | Skill 系统使用指南 |
| `workflow-reference` | 全部 Skill 速查手册 |
| `workflow-combos` | 场景化 Skill 组合 |
| `writing-skills` | Skill 编写、编辑与验证 |
| `write-a-skill` | Skill 创建向导 |
| `write-a-skill-mattpocock` | Skill 创建向导 (Matt Pocock 版) |
| `codex-skill-creator` | Skill 创建指南 (Codex 版) |
| `codex-template-skill` | Skill 模板 |

### 🔩 工具与配置

| Skill | 描述 |
|-------|------|
| `update-config` | settings.json 配置管理 |
| `keybindings-help` | 键盘快捷键自定义 |
| `fewer-permission-prompts` | 减少权限提示 (allowlist) |
| `loop` | 定时循环执行任务 |
| `claude-api` | Claude API/Anthropic SDK 开发 |
| `init` | 初始化 CLAUDE.md |
| `setup-matt-pocock-skills` | Matt Pocock Skill 套件安装 |
| `anthropic-skills:schedule` | 定时任务调度 |
| `anthropic-skills:setup-cowork` | Cowork 环境搭建 |
| `anthropic-skills:consolidate-memory` | 记忆文件整理合并 |

### 🎲 其他

| Skill | 描述 |
|-------|------|
| `caveman` | 超压缩通信模式 (省 75% Token) |
| `spreadsheet-formula-helper` | 电子表格公式编写与调试 |
| `ubiquitous-language` | 通用语言 (领域术语) |
| `zoom-out` | 代码库宏观视角 |

---

## 日常同步

### 修改 Skill 后推送

```bash
git add -A
git commit -m "更新: <skill名> — <简述>"
git push
```

### 新电脑恢复

```bash
git clone https://github.com/deprive-Wang/codex-skills-backup.git
cp -r codex-skills-backup/* ~/.claude/skills/   # Claude Code
# 或
cp -r codex-skills-backup/* ~/.codex/skills/    # OpenAI Codex
```

---

## 命名约定

- `codex-` 前缀: Codex 特定版本
- 无前缀: 双平台通用或 Claude 原生
- `anthropic-skills:` 前缀: Anthropic 官方 Skill
