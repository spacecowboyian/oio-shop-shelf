# 04 — Cleanup Methodology (the AI reconstruction prompt)

This is **not a script.** It is the instruction set a contributor feeds to their AI agent
(Claude Code, plain Claude, ChatGPT, etc.) to turn one chapter's raw OCR draft into a
clean `wiki/<chapter>.md`. Give the agent: (a) this file, (b) the raw draft from
`03_split_manifest.py`, and (c) the rendered page images from `02_render_pages.py` for
the same page range.

Treat everything below as hard rules, not suggestions.

> **Living standard.** These rules evolve as we convert more manuals. **Rule 0
> (never silently change a number) is inviolable; everything else is amendable.**
> If a manual surfaces a case the rules don't cover, or a rule turns out wrong,
> propose an edit to *this file* in your PR with the case that motivated it, and add
> a line to the changelog at the bottom. The reference 4A-GE manual is **not perfect
> yet** — its open items live in `manuals/toyota-4a-fe-4a-ge/wiki/10-needs-review.md`,
> the canonical example of "flag, don't guess." Tracked in
> [issue #3](https://github.com/spacecowboyian/oio-shop-shelf/issues/3).

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
exists as an image, **don't leave a bare "see page image" placeholder — deliver it**
per Rule 12 (add it to `diagrams:` and embed the rendered image at the citation point).

## Rule 7 — Spec callouts for the quick-reference index

So `05_build_indexes.py` can harvest specs, write recognizable spec lines wherever a
value appears in running text (tables are auto-detected already). Keep the unit attached
to the number (`44 N·m`, `0.20 mm`, `13.8 V`, `1.6 Ω`). The builder regexes on
number+unit patterns.

## Rule 8 — Source misprints vs OCR errors (state which)

Two different failure modes, both handled by "keep as printed + flag," but the flag must say
which:
- **OCR error** you resolved from the page image → use the image value and note
  `<!-- NEEDS REVIEW: OCR read X; page image shows Y — corrected from image -->`.
- **The manual itself misprints** a value (the page image confirms the wrong value, e.g. a
  unit conversion that can't reconcile) → keep it exactly as printed and note
  `<!-- NEEDS REVIEW: source misprint, not OCR — printed "X"; the (…) conversion implies Y -->`.
Never silently "fix" either. A reader must be able to tell an OCR artifact from a real
manual typo.

## Rule 9 — Duplicate / abridged scans and misfiled pages

A chapter's page range sometimes contains a **duplicate (often abridged) scan** of the same
content, or a few pages **belonging to another chapter** (misfiled in the scan). Transcribe
the **most complete pass once**, drop the duplicate/foreign pages, and record the dedup
decision in an HTML source-note comment at the top of the file. (The repo's
`check_page_continuity.py` also surfaces suspected gaps — but note it reads the manual's own
in-body page-code cross-references as page markers, so it over-reports; confirm real gaps
against the images before recording them.)

## Rule 10 — Diagram-only data and electrical matrices

- **Torque/spec callouts that appear only in an exploded-view diagram** (never restated in
  prose): pull them into a components torque table. If the diagram's leader line doesn't make
  the target fastener unambiguous, transcribe the value and flag the attribution.
- **Switch/relay continuity matrices** (dot-and-line grids): render as a "switch position →
  connected terminal groups" table. **Hysteresis switch-point diagrams** (ON/OFF thresholds):
  render as a "switching point → state" table. Where a grid is too dense/ambiguous to read
  reliably, leave a figure placeholder and flag it rather than guessing every dot.

## Rule 11 — Anchor slugs for THIS repo's link checker

`06_check_links.py` slugifies headings as: lowercase → strip non-`[\w\s-]` → collapse
**whitespace runs to a single `-`**. Consequences for intra-file links you write:
- An em-dash heading "Foo — Bar" becomes `#foo-bar` (single hyphen), **not** `#foo--bar`.
- The checker does **not** add GitHub-style `-1`/`-2` suffixes for duplicate headings — so
  don't link to `#heading-1`; make the heading text unique instead (see Rule 4 anchor note).

> **Chapter numbering:** don't collide with the generated index filenames. `05_build_indexes.py`
> now reserves only the specific `11a..11d-alphabetical-index.md` names (not the bare `11`
> prefix), so a chapter numbered `11a` is fine — but keep generated names (`00-`, `09-`,
> `10-`, `11?-alphabetical-index`) clear of chapter files.

## Rule 12 — Diagram delivery: deliver the image, don't just link the page

Diagrams, wiring charts, and exploded views live only in the source PDF — never as
faithful text. Historically the wiki could only say "open PDF p.N yourself." When a page
(or a figure on it) is **diagram-only** — a wiring chart, exploded view, torque/loosening
**sequence** figure, or any essential figure with no faithful text equivalent — register it
for in-chat delivery instead of only citing the page (see [issue #1](https://github.com/spacecowboyian/oio-shop-shelf/issues/1)):

1. **Add an entry to `manifest.yml` `diagrams:`** (CI validates the shape):
   ```yaml
   diagrams:
     - page: 66
       file: "diagrams/p0066-headbolt-loosening-sequence.webp"
       kind: sequence          # sequence | wiring | exploded | chart
       depth: mono             # mono = pure line art (~30 KB); gray = page has a photo/halftone (~70 KB)
       caption: "Cylinder head bolt loosening sequence"
       safety_relevant: true   # set when a wrong reading risks damage/injury (bolt order, torque sequence)
   ```
   Name the file `diagrams/p<NNNN>-<short-slug>.webp` (zero-padded source page). Pick
   `depth: mono` for clean line art; `gray` only if the page carries a photo or halftone
   shading that a 1-bit threshold would wreck.
2. **Render it:** `python scripts/02_render_pages.py manuals/<slug>/ --diagrams` (renders
   every `diagrams:` page at its depth to a lossless WebP).
3. **Embed it at the citation point** with a **relative** path — not a bare page reference:
   ```markdown
   ![Cylinder head bolt loosening sequence — PDF p.66](../diagrams/p0066-headbolt-loosening-sequence.webp)
   ```
   Keep it relative so it previews inside the PR; `publish-release.sh` rewrites it to the
   stable Release URL at merge (the image is stripped from git, same as the source PDF).

Still transcribe every value, table, or step you *can* faithfully pull from the figure
(Rule 10) — the image supplements the text, it does not excuse skipping transcription.
And reserve delivery for genuinely diagram-only content: don't image-dump a page whose
substance is already faithfully in the markdown.

## Output checklist (self-verify before saving)

- [ ] Every number matches the OCR/image; none silently changed.
- [ ] Every uncertain value has a `<!-- NEEDS REVIEW: reason -->` comment.
- [ ] Charts are markdown tables; procedures are ordered lists; flowcharts are step-tables.
- [ ] Exactly one H1; sensible `##`/`###` structure.
- [ ] Cross-references are relative links; nothing duplicated from other chapters.
- [ ] No page headers/footers or scan speckle left in the body.
- [ ] Every diagram-only figure the user would need to *see* is delivered per Rule 12
      (in `diagrams:`, rendered, embedded as a relative image) — not left as a bare page link.

## Changelog

Record rule changes here so contributors can see how the standard evolved. One line
per change: date · what changed · why (link the PR/issue).

- 2026-07-11 · Marked this doc a living standard; added changelog + link to
  `10-needs-review.md` as the canonical "flag, don't guess" example (#3).
- 2026-07-12 · Added Rules 8–11 from the Toyota MR2 (AW11) conversion (24-chapter whole-
  vehicle FSM): source-misprint vs OCR flag wording; duplicate/abridged-scan & misfiled-page
  handling; diagram-only torque callouts + electrical continuity/hysteresis matrices; and this
  repo's anchor-slug rules (single-hyphen collapse, no `-N` suffixes). Also fixed
  `05_build_indexes.py` to reserve only the specific `11?-alphabetical-index.md` filenames so a
  chapter numbered `11a` is no longer silently dropped from the indexes.
- 2026-07-12 · Added Rule 12 (diagram delivery): diagram-only figures are now rendered to a
  compact WebP and embedded at the citation point (relative link, flipped to the Release URL
  at merge), instead of a bare "see PDF p.N" placeholder. Updated Rule 6 accordingly (#1).
