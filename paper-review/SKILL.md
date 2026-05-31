---
name: paper-review
description: Reviews thesis, manuscript, defense, and submission documents from a final-reviewer perspective by rendering native files to PDF and auditing layout, language, logic, figure-text consistency, data consistency, and citation support. Use when the user asks to check whether a paper can be printed/submitted, review a thesis or manuscript, inspect PDF/DOCX/PPT layout, compare text with figures/tables, or judge reviewer-facing risks.
---

# Paper Review

Use this skill for final-stage academic document review. Treat the task as a reviewer-facing risk audit, not just proofreading.

## Core Rules

- Do not modify the source file unless the user explicitly asks for edits.
- Copy native files to a temporary workspace before conversion or extraction.
- Prefer rendered PDF evidence over native text extraction for layout, formulas, superscripts, page numbers, and figures.
- Report only checks actually performed. Do not claim visual, citation, or reference validation without evidence.
- If external literature is not provided, limit conclusions to internal consistency and reviewer risk.

## Use Related Skills

- Use `doc` for DOCX reading, Word/LibreOffice conversion, tables, styles, and structured extraction.
- Use `pdf` for PDF rendering, page-image inspection, text extraction, page size, blank page, and layout checks.
- Use `academic-paper-polisher` for academic wording, de-AI/口语化 checks, logic checks, and conservative rewrite suggestions.
- Use `nature-reader`, `content-research-writer`, or research-oriented skills when reference papers, DOI/arXiv links, BibTeX, or benchmark literature must be read.

## Workflow

1. **Establish review target**
   - Identify file type, review purpose, audience, and deadline: print, defense, submission, or reviewer-style audit.
   - Identify whether the user wants only final-layout review or also logic, novelty, related work, and citation support.

2. **Render first**
   - For DOCX/PPT/native office files, copy to temp and convert to PDF using `soffice`, LibreOffice, or Word automation.
   - For existing PDFs, use the given PDF directly.
   - Render pages to images with Poppler/`pdftoppm` when available; otherwise use `fitz` or `pypdfium2`.
   - Keep generated final PDFs only when the user asks or a non-temporary output path is agreed.

3. **Audit dimensions**
   - **Format/layout:** cover, declaration/signature areas, table of contents, page numbers, headers/footers, section breaks, blank pages, page size, clipped figures, overflowing tables, unreadable glyphs.
   - **Language:** typos, punctuation, informal wording, AI-flavored repetition, term consistency, acronym expansion, units, numeric formatting, Chinese/English spacing.
   - **Logic and narrative:** motivation, problem definition, method handoff, chapter flow, abstract-body-conclusion consistency, whether the paper explains why the model/experiment/result matters.
   - **Figure/text match:** figure and table numbering, caption placement, first mention, text claims supported by plotted trends, missing or contradictory figure descriptions.
   - **Data consistency:** repeated metrics, percentages, units, baseline names, experiment settings, trend descriptions, and conclusion claims.
   - **Citation support:** citation continuity, reference format, whether important background/method/comparison claims have traceable support.

4. **Reference-reading branch**
   - If the user asks whether novelty, related work, baselines, theoretical support, or reviewer acceptance is strong enough, ask whether reference papers, PDFs, BibTeX, DOI/arXiv links, project notes, or target requirements are available.
   - If references are provided, read only the relevant materials needed to judge the claim.
   - If references are unavailable, explicitly say the review is internal-only and frame findings as reviewer risks, not confirmed literature gaps.

5. **Classify severity**
   - `P0 必须修`: blocks printing/submission or damages basic credibility, such as broken references, missing values, unreadable pages, serious contradictions, placeholder text, or unsupported central claims.
   - `P1 建议修`: visible quality or reviewer-risk issues, such as weak logic transitions, informal wording, figure/text mismatch, inconsistent terminology, or incomplete citation support.
   - `P2 可选优化`: polish-level improvements that do not block submission.

## Output Format

Use this structure unless the user requests otherwise:

```markdown
## 结论
[可以打印/不建议打印/需先处理若干问题]，一句话说明主要原因。

## P0 必须修
- 位置：...
  问题：...
  证据：...
  建议：...

## P1 建议修
- 位置：...
  问题：...
  建议：...

## P2 可选优化
- ...

## 逻辑与讲述问题
- ...

## 参考文献阅读建议
[是否需要读参考文献；需要哪些材料；未读参考文献时的结论边界。]

## 验证记录
- 实际执行过的转换、渲染、抽取、检查命令或工具。

## 临时文件处理
- 临时文件是否清理；若保留 PDF 或输出文件，写明路径。
```

If there are no findings in a section, say `未发现需要报告的问题` rather than omitting the section when the user asked for a final audit.
