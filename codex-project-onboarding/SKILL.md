---
name: codex-project-onboarding
description: 首次打开项目时读取并创建或刷新根目录 `codex.md` 摘要。当用户希望 Codex 理解新代码库、生成项目简报、总结架构、记录启动命令或为后续会话创建入门笔记时使用。
---

# Codex 项目入门

首次接触项目时理解项目，并在项目根目录创建实用的 `codex.md`。

## 工作流程

1. 写之前先检查仓库：
   - 根目录文件，如 `README`、`package.json`、`pyproject.toml`、`Cargo.toml`、`.env.example`
   - 可能的入口点
   - 测试配置
   - 文档和架构说明
2. 建立简洁的心智模型：
   - 项目做什么
   - 主要子系统
   - 如何运行或测试
   - 关键外部依赖
   - 约定或坑点
3. 在项目根目录创建或更新 `codex.md`。
4. 让 `codex.md` 对后续编码会话有用，而不是通用仓库摘要。

## `codex.md` 必要章节

除非仓库明显需要不同的结构，否则使用以下章节：

```md
# Codex Notes

## Project Summary（项目概述）

## Structure（项目结构）

## Run and Test（运行与测试）

## Key Conventions（关键约定）

## Current Risks or Gaps（当前风险或缺口）

## Recommended First Actions（建议的首步操作）
```

## 内容规则

- 保持文档简短、高信号。
- 优先写仓库特有的事实，而非通用建议。
- 在可以安全发现的前提下，包含具体命令。
- 如实说明重要未知事项，不假装确定。
- 若 `codex.md` 已存在且过时，就地更新。

## 护栏

- 不编造没有仓库证据支持的命令。
- 不堆砌冗长的文件清单。
- 不重写整个文档，除非只需要小幅刷新。
- 若仓库较大，总结主要路径并推迟深入细节。
