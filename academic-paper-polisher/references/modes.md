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

Prioritize natural rhythm, varied sentence structure, concrete claims, and restrained wording. Remove mechanical transitions such as `First and foremost` and `It is worth noting that` when the logic can connect naturally.

For Chinese AIGC reduction, keep technical terms unchanged. If a sentence contains many technical terms and is hard to rewrite naturally, simplify and compress it. If it contains few technical terms, expand the explanation modestly to sound more like a student or researcher writing naturally.

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
