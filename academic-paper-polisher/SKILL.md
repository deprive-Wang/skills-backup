---
name: academic-paper-polisher
description: Academic paper writing assistant for Chinese and English manuscripts. Use when the user asks to polish, translate, rewrite, de-AI, reduce AIGC feel, expand, shorten, check logic, review a paper, analyze experiment results, draft figure/table captions, recommend academic plots, or design paper architecture figures for computer-science research text, LaTeX, Word-friendly Chinese prose, PDFs, or experiment data.
---

# Academic Paper Polisher

## Core Rule

Preserve factual truth. Do not invent data, claims, references, baselines, improvements, or test results. If the input lacks evidence for a claim, weaken the claim or say the evidence is insufficient.

Keep technical terms, formulas, citations, labels, and LaTeX commands intact unless the user explicitly asks to change them. Preserve `$...$`, `\cite{}`, `\ref{}`, `\eg`, `\ie`, algorithm/model names, dataset names, metric names, and experiment parameters.

## Mode Selection

Choose one mode from the user's wording, then follow the matching details in `references/modes.md` when needed:

- `chinese-polish`: Chinese thesis/paper paragraph polishing, Word-friendly output, conservative edits.
- `english-polish`: English LaTeX polishing for CS papers, stronger academic rewrite.
- `de-ai`: Reduce AI-detection rates via a 5-dimension tiered framework. Supports three intensity levels — `light` (connectors + sentence length), `medium` (structure + density), `heavy` (term context + structural reordering). Default: `medium` for Chinese thesis text, `light` for English. When a PaperPure or similar AIGC detector report shows persistent high-risk marking, activates the whole-thesis structural rewrite strategy. Produces `humanize_matrix.md` as the teaching deliverable.
- `translate-cn-en`: Turn Chinese draft into English academic LaTeX/prose.
- `translate-en-cn`: Translate English LaTeX/paper text into fluent Chinese.
- `expand`: Slightly expand English LaTeX text by adding only implied logic.
- `shorten`: Slightly shorten English LaTeX text without losing information.
- `logic-check`: Final red-line consistency check; report only serious issues.
- `experiment-analysis`: Analyze provided experiment data and write LaTeX analysis.
- `caption`: Generate English figure/table captions from Chinese descriptions.
- `plot-recommendation`: Recommend 1-2 rigorous academic plot designs.
- `architecture-figure`: Convert method descriptions into paper architecture figure design guidance.
- `reviewer-report`: Review a PDF or manuscript as a strict but fair CS reviewer.

If the request combines modes, run them in the natural order: understand evidence, translate if needed, polish, then check logic.

## Humanize Tiers (de-ai mode)

When de-ai is selected, determine the tier from context or ask the user. Default: `medium` for Chinese thesis/manuscript text, `light` for English.

- `light`: Fix D4 connectors and D1 sentence-length uniformity.
- `medium`: Light + D2 paragraph structure diversity + D3 information density variation + first-person insertion + strengthened D1.
- `heavy`: Medium + D5 term-context breaking + structural reordering + density labeling + uncommon vocabulary + tightened connectors.

### AIGC Detection Framework

The humanize process works against 5 detection dimensions used by CNKI AIGC 2026 v3.0 and similar systems:

| Dim | What It Measures | AI Text Signature |
|-----|-----------------|-------------------|
| D1-Sentence Length | Histogram of sentence lengths | AI: 15-25 chars single-peak bell; Human: multi-peak (5-8 + 15-25 + 40+) |
| D2-Paragraph Structure | Cosine similarity of paragraph "grammar skeletons" | AI: 0.7-0.9; Human: 0.2-0.5 |
| D3-Information Density | Independent info points per 100 chars/words | AI: 65%-75% flat; Human: 40%-85% fluctuating |
| D4-Connector Frequency | Connectors per 1000 chars + paragraph-start ratio | AI: 8-15/1k uniform; Human: 2-6/1k clustered |
| D5-Term-Context Match | Ratio of terms appearing in "most standard" context | AI: ~100% standard; Human: occasional colloquial substitution |

Read `references/humanize-tiers-zh.md` or `references/humanize-tiers-en.md` for complete tier-specific directives.

### Humanize Matrix Deliverable

Produce `humanize_matrix.md` alongside the polished output. Record every change:

| Row ID | Manuscript Unit | AI Pattern Found | Detection Dim | Severity | Applied Change | Expected Effect | Teaching Note |

Rules:
- At least one row per writing unit for D1 (sentence length)
- At least one row per paragraph for D2 (paragraph structure)
- At least one row per connector replaced (D4)
- At least one row per density adjustment (D3, medium+)
- At least one row per term substitution (D5, heavy only)
- Fill all 8 columns for every row — no empty cells
- Severity: High (>50% contribution to detection) / Medium (20-50%) / Low (<20%)

### PaperPure / Whole-Thesis High-Risk Strategy

When a detector report (PaperPure, CNKI AIGC, etc.) shows most of a thesis as high-risk after light paraphrasing, treat that as evidence that surface rewrites are ineffective. Switch to structural rewrite:

1. Diagnose the report first: total AIGC rate, AI-feature character count, high-risk distribution by chapter, whether prior revision actually reduced those numbers.
2. Prioritize the largest high-risk sections (experiment analysis, algorithm/model, theory/background, then abstract and conclusion).
3. Rewrite paragraph argument structure, not just wording. Change explanation order, split or merge claims, rebuild paragraphs around the thesis's own model, formulas, figures, tables, experiment settings, and observed results.
4. For experiment analysis: write from evidence — figure/table phenomenon → numeric or trend observation → mechanism tied to algorithm → bounded conclusion.
5. For algorithm/model paragraphs: bind prose to variables, constraints, formula roles, and module interactions. Explain why a variable affects the outcome, why a constraint narrows the feasible region, why a module is separated.
6. For abstracts: rewrite from the actual thesis contribution — scenario, service types, model components, module split, baselines, and main verified outcomes.
7. For conclusions and outlook: remove casual wording; tie each conclusion to a chapter result or experiment condition.
8. Preserve all citations, formulas, algorithm names, experiment numbers, figure/table references, and technical conclusions exactly.
9. Clean malformed spacing introduced by prior revisions, especially broken technical names such as `JOCD DQN`, `H- NOMA`, `MA DRL`.

### Verification (de-ai mode)

```powershell
python "$env:USERPROFILE/.claude/paper-spine/scripts/humanize_check.py" paper_rewriting_output --markdown --write
```

Produces `paper_rewriting_output/humanize_report.md` with sentence-length stddev, connector density, matrix coverage, and remaining AI pattern flags.

## Output Discipline

Match the user's requested format exactly. If no format is specified:

- For English LaTeX editing, output `Part 1 [LaTeX]`, `Part 2 [Translation]`, and `Part 3 [Modification Log]`.
- For Chinese polishing, output `Part 1 [Refined Text]` and `Part 2 [Review Comments]`.
- For logic checks with no serious issue, output exactly: `[检测通过，无实质性问题]`
- For captions, output only the caption text without `Figure 1:` or `Table 1:`.
- For reviewer reports, output only `Part 1 [The Review Report]` and `Part 2 [Strategic Advice]`.

Do not add prefaces, apologies, generic explanations, or extra chat after the requested result.

## Editing Standards

Use plain, precise academic wording. Avoid ornate vocabulary and common AI-flavored words unless technically necessary, such as `leverage`, `delve into`, `tapestry`, `showcase`, and `depict`.

Avoid unnecessary bold, italics, itemized lists, or new formatting commands in manuscript text. Preserve existing formatting commands when they are already present in the input.

Prefer minimal edits when the source is already clear. Do not rewrite merely to create visible changes.

## Required Reference

Read `references/modes.md` before executing any non-trivial paper-writing task with this skill. It contains the mode-specific thresholds, output formats, and quality checks distilled from the user's prompt collection.
