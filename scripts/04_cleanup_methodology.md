# 04 — Cleanup Methodology (the AI reconstruction prompt)

This is **not a script.** It is the instruction set a contributor feeds to their AI agent
(Claude Code, plain Claude, ChatGPT, etc.) to turn one chapter's raw OCR draft into a
clean `wiki/<chapter>.md`. Give the agent: (a) this file, (b) the raw draft from
`03_split_manifest.py`, and (c) the rendered page images from `02_render_pages.py` for
the same page range.

Treat everything below as hard rules, not suggestions.

---

## Your job

Reconstruct the raw OCR text of ONE chapter into clean, structured, faithful markdown.
You are a transcriptionist and typesetter, **not** an editor, summarizer, or engineer.
Preserve the manual's meaning and every value exactly; improve only structure and
readability.

## Rule 0 — Never silently change a number (most important rule)

- Do not alter, round, "fix," or normalize any numeric or spec value: torque figures,
  clearances, voltages, resistances, capacities, part numbers, page references, years.
- If OCR is ambiguous or the value looks implausible, **keep the OCR value as-is** and
  flag it inline:
  ```markdown
  Valve clearance (intake): 0.20 mm <!-- NEEDS REVIEW: OCR unclear; page image may show 0.28 — verify -->
  ```
- Cross-check ambiguous cells against the **rendered page image** before flagging. If the
  image resolves it unambiguously, use the image's value and note it:
  ```markdown
  Torque: 44 N·m <!-- NEEDS REVIEW: OCR read "4 N·m"; page image clearly shows "44" — corrected from image -->
  ```
- When unsure whether something is a spec, treat it as one and flag it. Over-flagging is
  cheap; a wrong number is dangerous.

## Rule 1 — Tables over ASCII art

Image-based charts often OCR into ragged columns of numbers and dashes. Reconstruct them
as real GitHub-flavored markdown tables. Preserve column headers and units. Example:

Raw OCR:
```
Item          Standard    Limit
End play      0.05-0.15   0.30
Thrust clr    0.04-0.24   0.30
```
Clean:
```markdown
| Item                | Standard (mm) | Limit (mm) |
| ------------------- | ------------- | ---------- |
| Crankshaft end play | 0.05–0.15     | 0.30       |
| Thrust clearance    | 0.04–0.24     | 0.30       |
```

## Rule 2 — Numbered procedures become ordered lists

Steps that read "1. Remove... 2. Disconnect..." become a markdown ordered list. Keep
sub-steps as nested lists. Keep any CAUTION / WARNING / NOTE callouts as blockquotes:
```markdown
> **CAUTION:** Do not reuse the gasket.
```

## Rule 3 — Diagnostic flowcharts become step-tables

Troubleshooting trees don't survive as prose. Render them as a table of
condition → check → result → next action:

```markdown
| Step | Check                       | Result | Go to |
| ---- | --------------------------- | ------ | ----- |
| 1    | Battery voltage ≥ 12 V?     | Yes    | 2     |
| 1    | Battery voltage ≥ 12 V?     | No     | Charge battery |
```

## Rule 4 — Headings and anchors

- One `#` H1 per file: the chapter title.
- Use `##`/`###` for sections and sub-sections so `05_build_indexes.py` can build the TOC.
- Section headings generate GitHub anchors automatically; keep them stable and descriptive
  because the quick-reference and alphabetical indexes link to them.

## Rule 5 — Cross-references are links, not duplication

When the text says "see Engine Mechanical," link it:
`see [Engine Mechanical](04a-engine-mechanical.md#cylinder-head)`. Do not copy content
from another chapter.

## Rule 6 — Drop the noise, keep the substance

Remove OCR artifacts that carry no information: page headers/footers, scan speckle
rendered as stray characters, running chapter titles repeated on every page. Do **not**
remove actual content, figure captions, or notes. If a figure is essential and only
exists as an image, leave a placeholder: `*(Figure 4-3: timing marks — see page image p.58)*`.

## Rule 7 — Spec callouts for the quick-reference index

So `05_build_indexes.py` can harvest specs, write recognizable spec lines wherever a
value appears in running text (tables are auto-detected already). Keep the unit attached
to the number (`44 N·m`, `0.20 mm`, `13.8 V`, `1.6 Ω`). The builder regexes on
number+unit patterns.

## Output checklist (self-verify before saving)

- [ ] Every number matches the OCR/image; none silently changed.
- [ ] Every uncertain value has a `<!-- NEEDS REVIEW: reason -->` comment.
- [ ] Charts are markdown tables; procedures are ordered lists; flowcharts are step-tables.
- [ ] Exactly one H1; sensible `##`/`###` structure.
- [ ] Cross-references are relative links; nothing duplicated from other chapters.
- [ ] No page headers/footers or scan speckle left in the body.
