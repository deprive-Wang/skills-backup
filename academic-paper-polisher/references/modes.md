# Academic Paper Polisher Modes

## General Self-Check

Before output, verify:

- Every changed claim is supported by the input.
- No metric, dataset, model, baseline, citation, formula, or parameter was silently changed.
- LaTeX special characters are escaped when they are literal text: `%`, `_`, `&`.
- Mathematical expressions enclosed in `$` remain unchanged.
- The answer contains no extra conversation outside the required format.

## Chinese Polish

Use for Chinese thesis or paper paragraphs.

Edit conservatively. Fix clear grammar problems,口语化表达, broken logic, severe redundancy, and unclear references. Preserve the author's original style when the paragraph is already clear and academic.

Use modern academic Chinese. Avoid stale bureaucratic substitutions such as replacing `旨在` with `拟`, or `是` with `系` without need.

Output:

```text
Part 1 [Refined Text]
...

Part 2 [Review Comments]
...
```

If unchanged, repeat the original text in Part 1 and state that it is clear and needs no modification in Part 2.

## English Polish

Use for English LaTeX paper fragments.

Improve clarity, academic rigor, grammar, punctuation, article use, and sentence flow. Use simple and precise research vocabulary. Do not expand common abbreviations such as LLM unless the user asks. Avoid possessive forms for method/model/system names when an `of` structure is clearer.

Keep paragraph structure. Do not turn prose into itemized lists.

Output:

```text
Part 1 [LaTeX]
...

Part 2 [Translation]
...

Part 3 [Modification Log]
...
```

## De-AI And AIGC Reduction

Use when the user asks for 去 AI 味, 降 AIGC, 降重, or more human academic writing.

**Hard constraints:**

1. **不压缩总字数** — Do not reduce the total word count. The output should be roughly the same length as the input, or slightly longer. When restructuring sentences, expand elsewhere to compensate if a sentence is shortened. Never output a noticeably shorter version.
2. **保护正文引用标注** — Preserve all inline citation markers (e.g., `[6]`, `[7][8]`, `[12]-[14]`, `[22][25][27]`) exactly as they appear. Do not change, reorder, drop, or add citations. The citation numbers and their groupings must remain unchanged.

Prioritize formal academic naturalness: varied sentence structure, concrete claims, restrained wording, and clear logical progression. Reduce AI-like regularity without making the prose chatty, casual, anecdotal, or essay-like.

Remove mechanical transitions such as `First and foremost` and `It is worth noting that` when the logic can connect naturally. Do not replace them with colloquial connectors such as `说白了`, `其实就是`, `可以看到`, or `总的来说` unless the original text already uses that register and the user explicitly wants it.

For Chinese AIGC reduction, keep technical terms unchanged. Preserve thesis/paper register and avoid over-oralized phrasing, internet-style wording, exaggerated tone, and subjective filler such as `一炸`, `拉满`, `很猛`, `说白了`, or `其实就是`. If a sentence contains many technical terms and is hard to rewrite naturally, simplify and restructure it while retaining rigor — keep the same information density, do not shorten. If it contains few technical terms, make the causal or explanatory relation more specific (moderately expanding the text), but do not add unsupported claims or casual examples.

For Chinese thesis text, prefer precise academic expressions such as `结果表明`, `由此可见`, `该现象说明`, `在该条件下`, and `本文认为` when appropriate. Avoid lowering the register merely to reduce AIGC feel. The goal is human academic writing, not spoken narration.


### PaperPure / Whole-Thesis High-Risk De-AI

When a detector report such as PaperPure still marks most of a thesis as high-risk after light paraphrasing, treat that as evidence that synonym replacement, spacing changes, and sentence-level polishing are ineffective. Do not continue with mechanical local rewrites.

Use a structural rewrite instead:

1. Diagnose the report first: record total AIGC rate, AI-feature character count, high-risk distribution by chapter, and whether the previous revision actually reduced those numbers.
2. Prioritize the largest high-risk sections, usually experiment analysis, algorithm/model chapters, theory/background sections, then abstract and conclusion. Do not spend most effort on isolated low-impact sentences.
3. Rewrite paragraph argument structure, not just wording. Change the order of explanation, split or merge claims where needed, and rebuild the paragraph around the thesis's own model, formulas, figures, tables, experiment settings, and observed results.
4. For experiment-analysis paragraphs, write from evidence: figure/table phenomenon -> numeric or trend observation -> mechanism tied to the algorithm -> bounded conclusion. Avoid template-only claims such as "the result shows the algorithm is effective" unless supported by concrete evidence.
5. For algorithm/model paragraphs, bind prose to variables, constraints, formula roles, and module interactions. Explain why a variable affects SINR/EE/QoS, why a constraint narrows the feasible region, or why a module is separated. Generic statements like "the problem is non-convex" are not enough.
6. For abstracts, rewrite from the actual thesis contribution: scenario, service types, model components, JOCDDQN module split, baselines, and main verified outcomes. Do not only polish background sentences.
7. For conclusions and outlook, remove casual wording, but also avoid generic endings. Tie each conclusion to a chapter result or experiment condition.
8. Preserve citations, formulas, algorithm names, experiment numbers, figure/table references, and technical conclusions exactly unless the user explicitly asks to change them.
9. Clean malformed spacing introduced by prior revisions, especially broken technical names such as `JOCD DQN`, `H- NOMA`, `MA DRL`, or split abbreviations.

A successful PaperPure-oriented pass should reduce exact high-risk source passages and change the explanatory structure of the highest-risk chapters. If the AIGC rate barely changes or AI-feature characters increase, explicitly report that the prior strategy failed and switch to this structural rewrite strategy.
For English LaTeX de-AI, do not force changes if the text is already natural. In that case, keep the original in Part 1 and write this in Part 3:

```text
[检测通过] 原文表达地道自然，无明显 AI 味，建议保留。
```

## Translation

### Chinese To English

Translate Chinese drafts into polished English academic text. Treat the output as a paper fragment, not literal translation. Fix logical gaps and awkward phrasing, but do not add unsupported claims.

Use English LaTeX when the source contains formulas, citations, labels, or paper-style notation. Preserve all technical names and formulas.

Output English text, Chinese direct translation, and a short modification log unless the user asks for only one result.

### English To Chinese

Translate English LaTeX or paper text into fluent Chinese for researcher comprehension. Keep formulas, citations, labels, variables, and abbreviations unchanged. Prefer readable Chinese over word-by-word translation.

## Expand

Use for 微幅扩写 of English LaTeX.

Increase length only slightly, roughly 5-15 English words for a normal paragraph unless the user specifies otherwise. Add only implied premises, causal links, or conclusions already supported by the input. Do not add fake experimental evidence.

Output LaTeX, Chinese translation, and a modification log that names what logic was made explicit.

## Shorten

Use for 微幅缩写 or compression of English LaTeX.

Reduce length only slightly, roughly 5-15 English words for a normal paragraph unless the user specifies otherwise. Remove filler, simplify clauses, and merge redundant phrasing. Preserve all core information, conditions, parameters, formulas, and claims.

Output LaTeX, Chinese translation, and a modification log that names what was compressed.

## Logic Check

Use for final red-line review.

Assume the draft has already been revised and is mostly good. Report only blocking problems: real logical contradictions, term inconsistency that changes meaning, severe grammar that obscures meaning, or claims unsupported by the supplied context.

If no serious issue exists, output exactly:

```text
[检测通过，无实质性问题]
```

If issues exist, list them briefly in Chinese. Do not nitpick style.

## Experiment Analysis

Use for experiment data, CSV/Excel summaries, result tables, or metric comparisons.

Base every conclusion on the supplied data. Do not fabricate trends, significance, rankings, or improvement percentages. If advantages are weak or inconsistent, state that directly.

Avoid ledger-style reporting. Focus on comparison, trends, sensitivity, performance-efficiency tradeoffs, and ablation contributions.

Preferred output:

```text
Part 1 [LaTeX]
\paragraph{Concise Title Case Finding} ...

\paragraph{Another Finding} ...

Part 2 [Translation]
...
```

Do not use `\textbf` or `\emph` for emphasis in the analysis prose.

## Caption Generation

Use for English figure or table captions from Chinese descriptions.

For noun-phrase captions, use Title Case and no final period. For complete-sentence captions, use sentence case and a final period.

Figure captions should be direct and not start with `The figure shows` or `This diagram illustrates`. Table captions may use standard forms such as `Comparison with`, `Ablation Study on`, and `Results on`.

Output only the caption text. Do not include `Figure 1:` or `Table 1:`.

## Plot Recommendation

Use when the user asks how to draw experiments or which plot to use.

Recommend 1-2 academic chart types. Prefer standard choices:

- Grouped vertical bar chart for compact SOTA comparison.
- Horizontal bar chart for long method names or many methods.
- Pareto frontier for tradeoffs between two constrained metrics.
- Radar chart for multi-dimensional capability summaries.
- Stacked bar chart for decomposed totals.
- Line chart with confidence interval for training curves or multi-seed trends.
- Zoomed inset line chart for close late-stage convergence.
- Scatter or fitted scatter plot for relationships between continuous variables.
- ROC or precision-recall curve for classification.
- Heatmap for matrices, correlations, confusion matrices, or task-method grids.
- Violin or box plot for distributions.
- Dual-axis or bar-line chart only when units differ and the relationship is justified.
- Faceted grid when too many variables would crowd one plot.

For each recommendation, include:

1. Recommended chart type.
2. Core reason tied to the data story.
3. Visual design specifications: axes, scale handling, statistical elements, colors/style, and expected conclusion.

If scales differ greatly, recommend a broken axis, log scale, or normalization according to the data story.

## Architecture Figure

Use for paper architecture diagrams from method descriptions.

First identify modules, data flow, training/inference paths, inputs/outputs, and what contribution the diagram must make visually obvious. Recommend a clean academic architecture figure with labeled modules and arrows. Do not over-decorate.

Output should include:

- Core modules.
- Layout direction.
- Arrow/data-flow semantics.
- Visual hierarchy and grouping.
- Caption suggestion if useful.

## Reviewer Report

Use for whole-paper review from PDF/manuscript and a target venue.

Be strict, specific, and fair. Separate fatal problems from fixable revision issues. Do not punish a paper for lacking unnecessary mathematical derivation if contribution lies in method, data, evaluation, or systematic analysis.

Review dimensions:

- Contribution to the community.
- Rigor of claims, baselines, ablations, and evaluation fairness.
- Consistency between introduction claims and experimental verification.
- Specificity of weaknesses at the level of dataset, experiment, reasoning step, or writing defect.

Output only:

```text
Part 1 [The Review Report]
Summary: ...
Strengths: ...
Weaknesses (Critical): ...
Rating: ...

Part 2 [Strategic Advice]
问题根源：...
可救性判断：...
行动指南：...
```

Use Chinese unless the user requests English.
