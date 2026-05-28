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
| `feature-dev` | 7 阶段功能开发工作流 (Discovery -> Exploration -> Questions -> Architecture -> Implementation -> Review -> Summary) |
| `subagent-driven-development` | 多 Agent 并行开发调度 |
| `executing-plans` | 按既定计划逐步执行开发 |
| `dispatching-parallel-agents` | 无依赖任务并行分发 |
| `writing-plans` | 多步骤任务执行前先写实现计划 |
| `workflow-code` | 代码工作流总入口 (实验设计 -> 代码交付) |

### 代码质量

| Skill | 描述 | 备注 |
|-------|------|------|
| `pr-review-toolkit` | 6 Agent 全面 PR 审查 (质量/精简/注释/测试/错误处理/类型设计) | |
| `requesting-code-review` | 主动请求代码审查的工作流 | |
| `receiving-code-review` | 处理审查反馈 (验证而非盲从) | |
| `verification-before-completion` | 完成前先验证 (证据优于断言) | |
| `karpathy-guidelines` | Karpathy 编码指南 (减少 LLM 常见错误) | |
| `improve-codebase-architecture` | 代码库架构深化改进 | |
| `code-simplifier` | 代码精简 (不改变行为的前提下降低复杂度) | |

### 调试与测试

| Skill | 描述 | 备注 |
|-------|------|------|
| `systematic-debugging` | 系统化调试 (根因 -> 假设 -> 验证 -> 修复) | |
| `diagnose` | 严格诊断循环 (复现 -> 缩小 -> 假设 -> 插桩 -> 修复 -> 回归) | |
| `tdd` | TDD 红-绿-重构循环 | 与 `test-driven-development` 功能相同 |
| `tdd-mattpocock` | TDD (Matt Pocock 版，含测试反模式) | |
| `test-driven-development` | TDD 红-绿-重构循环 | 与 `tdd` 功能相同 |
| `webapp-testing` | Playwright Web 应用测试 | |
| `playwright` | Playwright CLI 浏览器自动化 (导航、点击、截图、数据提取、UI 调试) | |

### Git 工具

| Skill | 描述 |
|-------|------|
| `git-guardrails` | 拦截危险 Git 命令 (push/force reset/clean 等) |
| `finishing-a-development-branch` | 开发分支收尾 (合并/PR/清理) |
| `using-git-worktrees` | 隔离 Git Worktree 工作流 |
| `setup-pre-commit` | Husky pre-commit hooks 配置 |

### 文档生成

| Skill | 描述 | 备注 |
|-------|------|------|
| `minimax-docx` | 专业 DOCX 文档 (OpenXML SDK .NET) | |
| `minimax-pdf` | 专业 PDF 设计排版 | |
| `minimax-xlsx` | Excel 电子表格创建与分析 | |
| `markitdown` | 多格式文件与 Office 文档转换为 Markdown | |
| `ppt-master` | 多格式内容转 SVG 页面并导出 PPTX 的演示文稿生成工作流 | |
| `pptx-generator` | PowerPoint 演示文稿生成 | |
| `doc` | DOCX 基础读写 | |
| `pdf` | PDF 基础读写 | |
| `paperjsx` | JSON -> 文档 (PPTX/DOCX/XLSX/PDF) | 与 `codex-paperjsx` 功能相同 |
| `codex-paperjsx` | PaperJSX (Codex 版本) | 与 `paperjsx` 功能相同 |
| `Visiomaster` | Visio 图表重建工作流，将流程图/架构图重绘为可编辑 `.vsdx` 并导出 `.svg/.png` | |

### 写作与内容

| Skill | 描述 | 备注 |
|-------|------|------|
| `content-research-writer` | 内容写作 + 研究 + 引用 | 与 `codex-content-research-writer` 功能相同 |
| `codex-content-research-writer` | 同上 (Codex 版本) | |
| `edit-article` | 文章编辑与润色 | |
| `codex-changelog` | 从 Git 提交自动生成 Changelog | |
| `codex-email-polish` | 邮件起草/改写/压缩 | |

### 学术与论文

| Skill | 描述 |
|-------|------|
| `workflow-thesis` | 论文全流程 (开题 -> 文献综述 -> 写作 -> 答辩) |
| `hv-analysis` | 横纵分析法深度研究 (双轴分析 -> PDF 报告) |
| `academic-paper-polisher` | 中英文学术论文润色、翻译、去 AI 味、实验分析、caption 与逻辑检查 |
| `nature-paper2ppt` | 论文 -> Nature 风格中文 PPT (组会/报告/答辩) |
| `nature-polishing` | 学术散文 Nature 风格英文润色与翻译 |
| `nature-reader` | 中英文对照全文论文阅读器 (PDF/DOI/arXiv) |
| `nature-response` | 审稿意见逐点回复信 (Nature 系) |
| `nature-writing` | Nature 风格论文各章节撰写与重构 |
| `brainstorming` | 创意构思与设计探索 |
| `grill-me` | 方案质询 (追问至全面理解) |
| `grill-with-docs` | 方案质询 + 文档同步更新 |

### PaperSpine 论文工作流

来源: [github.com/WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine)，使用 `install.ps1 -Target claude` 安装。

| Skill | 描述 |
|-------|------|
| `paper-spine` | PaperSpine 编排器 (总入口，`/paperspine` 启动) |
| `paper-spine-intake` | 配置接入 (flash/pro, scene, language) |
| `paper-spine-ui` | 外部终端配置 UI |
| `paper-spine-research` | 研究目标需求、下载参考资料、学习优秀样例 |
| `paper-spine-citation` | 引用支持库构建 |
| `paper-spine-build` | 从材料构建论文 |
| `paper-spine-rewrite` | 从动机/研究/证据重写手稿 |
| `paper-spine-latex` | LaTeX 项目组装与编译 |
| `paper-spine-translate` | 中文翻译包 (逐行翻译 + 全文翻译) |
| `paper-spine-humanize` | 降低 AI 检测率 (分层风格约束) |
| `paper-spine-audit` | 产出物审计 (缺失、浅层修改、逻辑迁移) |
| `paper-spine-update` | 版本更新检查与升级 |

### 会议与沟通

| Skill | 描述 | 备注 |
|-------|------|------|
| `meeting-insights-analyzer` | 会议分析 (行为模式/沟通洞察) | 与 `codex-meeting-insights` 功能相同 |
| `codex-meeting-insights` | 同上 (Codex 版本) | |
| `meeting-notes-and-actions` | 会议纪要 + 待办 | 与 `codex-meeting-notes` 功能相同 |
| `codex-meeting-notes` | 同上 (Codex 版本) | |

### 知识管理

| Skill | 描述 | 备注 |
|-------|------|------|
| `neat-freak` | 会话后文档与记忆洁癖级同步 | |
| `obsidian-vault` | Obsidian 笔记搜索与管理 | |
| `notion-research-documentation` | Notion 跨源研究 -> 结构化文档 | |
| `notion-spec-to-implementation` | Notion Spec -> 实现计划+任务 | |
| `file-organizer` | 智能文件整理 | 与 `codex-file-organizer` 功能相同 |
| `codex-file-organizer` | 同上 (Codex 版本) | |

### 项目管理

| Skill | 描述 | 备注 |
|-------|------|------|
| `to-issues` | 计划/PRD 拆分为独立 Issue | |
| `to-prd` | 对话上下文 -> PRD | |
| `triage` | Issue 状态机分类 | |
| `qa` | 对话式 QA -> GitHub Issue | |
| `create-plan` | 快速创建实现计划 | 与 `codex-create-plan` 功能相同 |
| `codex-create-plan` | 同上 (Codex 版本) | |
| `planning-with-file` | 计划持久化为 plan.md | 原名 `planing-with-file`，已修正拼写 |

### 技能系统

| Skill | 描述 | 备注 |
|-------|------|------|
| `using-superpowers` | Skill 系统使用指南 | |
| `workflow-reference` | 全部 Skill 速查手册 | |
| `workflow-combos` | 场景化 Skill 组合 | |
| `writing-skills` | Skill 编写、编辑与验证 | |
| `write-a-skill` | Skill 创建向导 | 与 `write-a-skill-mattpocock` 功能相似 |
| `write-a-skill-mattpocock` | Skill 创建向导 (Matt Pocock 版) | |
| `codex-skill-creator` | Skill 创建指南 (Codex 版) | |
| `codex-template-skill` | Skill 模板骨架 (创建新 skill 的起始模板) | |

### 项目初始化

| Skill | 描述 | 备注 |
|-------|------|------|
| `init` | 项目初始化 (生成/更新项目级 codex.md) | Codex 专用 |
| `codex-project-onboarding` | 项目首次扫描与 onboarding 总结 | Codex 专用 |

### 辅助工具

| Skill | 描述 |
|-------|------|
| `caveman` | 超压缩通信模式 (省 75% Token) |
| `spreadsheet-formula-helper` | 电子表格公式编写与调试 |
| `ubiquitous-language` | DDD 通用语言术语表提取 |
| `zoom-out` | 代码库宏观视角 (向上一层抽象) |
| `setup-matt-pocock-skills` | Matt Pocock Skill 套件安装 (配置 issue tracker / triage labels / domain docs) |

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
