---
name: workflow-code
description: 代码工作流 — 从实验设计到代码交付的 engineering pipeline。当用户提到开发、实现、调试、重构、TDD、实验时使用。
---

# 代码工作流

按开发生命周期分四个阶段。全程遵循 Karpathy 四原则：**先想再写、简单至上、精准修改、目标驱动**。

## Phase 1: 设计 & 规划

```
/codex-create-plan  → 生成简洁的执行计划（实验步骤 / 功能拆分）
/karpathy-guidelines → 先想再写：陈述假设、给出多解、挑最简单的
/grill-me            → 挑战你的设计方案
/caveman             → 极简模式，剔除冗余，聚焦核心逻辑
```

**适用场景：** 新实验、新功能、算法改进。先做计划再动手。

> Karpathy 原则 #1 **先想再写**：别猜，不确定就问。有多种解读就列出来。能更简单就说出来。
> Karpathy 原则 #4 **目标驱动**：把需求转为可验证的成功标准。"加个功能" → "X 输入应得 Y 输出"。

## Phase 2: 实现

```
/karpathy-guidelines → 简单至上：最少代码解决问题，200 行能改 50 行就改
/tdd-mattpocock      → TDD 红-绿-重构循环（Matt Pocock 风格，偏集成测试）
/test-driven-development → TDD 流程（通用风格）
```

> 二选一：`tdd-mattpocock` 偏集成测试先行，`test-driven-development` 偏单元测试先行。

> Karpathy 原则 #2 **简单至上**：不加多余功能、不抽象单次调用的代码、不添加没被要求的"灵活性"。每行代码都应对应用户请求。

## Phase 3: 调试 & 审查

```
/systematic-debugging → 遇到 bug 时系统排查（不猜测，逐层隔离）
/karpathy-guidelines  → 精准修改：只改必须改的，不动相邻代码
/caveman              → 极简调试 — 最小化复现代码
/qa                   → 对话式 bug 报告，后台探索代码库
```

**步骤：** bug → `/systematic-debugging` 定位 → `/karpathy-guidelines` 约束改动范围 → `/caveman` 最小复现 → `/qa` 记录。

> Karpathy 原则 #3 **精准修改**：不动注释、不动格式、不重构没坏的代码。每个改动行都能追溯到用户请求。你的改动产生的孤儿（未引用 import/变量）必须清理，但不碰已有的 dead code。

## Phase 4: 收尾

```
/verification-before-completion → 完成前验证：跑测试、确认输出、再声明成功
/codex-changelog                → 从 git commit 自动生成变更记录
/requesting-code-review         → 提交前请求代码审查
```

## 完整流水线（一次性）

```
/codex-create-plan → /karpathy-guidelines → /tdd-mattpocock → /verification-before-completion → /codex-changelog
```
