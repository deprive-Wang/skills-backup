---
name: workflow-thesis
description: 论文工作流 — 从开题方案到论文终稿的完整 pipeline。当用户提到论文、开题、答辩、文献综述、润色、写作时使用。
---

# 论文工作流

按学术写作的生命周期分三个阶段，每阶段调用对应技能。

## Phase 1: 方案设计（开题 / 中期报告）

```
/to-prd           → 将导师要求转为结构化需求文档
/grill-me         → 让 AI 扮演答辩评委，逐条挑战你的设计
/zoom-out         → 跳出细节，审视整体目标和进度
```

**步骤：** 先用 `/to-prd` 输出需求文档 → 用 `/grill-me` 逐条审查 → 最后 `/zoom-out` 确认大方向。

## Phase 2: 论文写作

```
/codex-content-research-writer → 文献综述 / 调研段落 / 正文（带引用）
/edit-article                   → 逐段润色，改善结构、清晰度、紧凑度
/ubiquitous-language            → 统一论文中的术语，消除同义词漂移
```

**步骤：** 先写 → 再润 → 最后术语统一。可反复迭代。

## Phase 3: 最终打磨（提交前 / 答辩前）

```
/qa                             → 代码和实验逻辑审查
/edit-article                   → 最后一遍全文通读润色
/codex-paperjsx                 → 生成答辩 PPT / PDF 报告
/grill-me                       → 模拟答辩提问
```

**步骤：** 代码和文字都审查完 → 生成答辩材料 → 模拟答辩。

## Phase 4: 实验代码（涉及编程时）

```
/karpathy-guidelines → 简单至上：实验代码够用就行，不过度工程化
/workflow-code       → 切到完整代码工作流（如实验复杂）
```

> Karpathy 四原则在论文实验代码中的应用：
> - **先想再写** — 假设和实验设计写清楚再写代码
> - **简单至上** — 实验代码只证明论点，不加多余功能
> - **精准修改** — 改实验参数只改该改的，不顺手重构
> - **目标驱动** — "跑个实验" → "输入 X 数据集，输出 Y 指标 ≥ Z"

## 完整流水线（一次性）

```
/to-prd → /grill-me → /codex-content-research-writer → /edit-article → /ubiquitous-language → /qa → /codex-paperjsx
```
