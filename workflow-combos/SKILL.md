---
name: workflow-combos
description: 常用小组合 — 按场景打包的技能组合。当用户提到开会、见导师、整理、润色、周报时使用。
---

# 常用小组合

按高频场景打包，一次调用一个场景的完整流程。

## 场景 1: 和导师开会前/后

```
/codex-meeting-notes    → 录音/笔记 → 决议 + 风险 + 待办（带负责人）
/codex-meeting-insights → 深度分析：导师的隐含关注点、沟通模式
/codex-email-polish     → 会后给导师发总结邮件
```

**步骤：** 开会 → 笔记整理 → 深度分析 → 发邮件确认。

## 场景 2: 周报 / 进度汇报

```
/zoom-out               → 跳出细节，盘点本周进度
/codex-changelog        → 从 commit 自动生成技术变更
/codex-email-polish     → 草拟导师的进度邮件
```

## 场景 3: 论文段落打磨

```
/codex-content-research-writer → 写初稿（带引用）
/edit-article                  → 润色结构 + 文字
/ubiquitous-language           → 术语一致性检查
```

> 这是 `workflow-thesis` Phase 2 的快捷版。

## 场景 4: 项目整理

```
/codex-file-organizer   → 整理实验数据、论文草稿、参考文献
/zoom-out               → 审视项目结构是否合理
```

## 场景 5: 设计方案审查

```
/to-prd               → 出需求文档
/karpathy-guidelines  → 先想再写：陈述假设，权衡方案
/grill-me             → 严格挑战
/grill-with-docs      → 结合项目文档审查（如已有 CONTEXT.md）
```

> `grill-me` 是盲审，`grill-with-docs` 会结合领域文档。`karpathy-guidelines` 提醒 AI 先澄清需求再动手。

## 场景 6: 快速 debug

```
/systematic-debugging   → 系统定位
/karpathy-guidelines    → 精准修改：只改 bug，不动相邻代码
/caveman                → 最小复现
```

## 场景 7: 写代码（小需求）

```
/karpathy-guidelines → 简单至上 + 精准修改：最少代码、只改该改的
/caveman             → 极简输出
```

> 小改动直接 `karpathy-guidelines` + `caveman`。大需求切 `workflow-code` 完整流水线。

## 场景 8: 创建自己的技能

```
/codex-skill-creator      → Codex 风格指南
/write-a-skill-mattpocock → Matt Pocock 风格指南
/codex-template-skill     → 模板骨架
```
