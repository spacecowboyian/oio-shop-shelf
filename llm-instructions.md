# oio-shop-shelf — LLM instructions

Point any AI assistant at this file first. It works whether you're Claude Code, plain
Claude, ChatGPT, or anything else — this repo is designed to not require a specific tool.

## What this is

A collection of OEM service manuals, each converted from a scanned PDF into a clean
markdown wiki (real tables, numbered procedures, a back-of-book index) plus the
**source PDF itself, committed alongside it** for diagrams, wiring charts, and exploded
views that never made it into text.

## Finding a manual

Each manual lives in `manuals/<slug>/`:

```
manuals/<slug>/
  manifest.yml              title, chapter map, rights note
  <manual-name>.pdf          the committed source PDF
  wiki/
    llm-instructions.md      MANUAL-SPECIFIC entry point — read this before answering
                              anything about this particular manual (exact filenames,
                              chapter breakdown, known OCR quirks)
    00-index.md               chapter list
    11*-alphabetical-index.md back-of-book index — usually the fastest way to find a topic
```

`ls manuals/` to see what's available. If the user's question names a make/model/engine,
match it to a slug (check each `manifest.yml`'s `title:` if the slug isn't obvious), then
read that manual's `wiki/llm-instructions.md` before answering.

## Read the glossary before answering

**Read [`glossary.md`](glossary.md) too, not just the manual-specific file.** Having
access to a manual isn't the same as understanding it — abbreviations (SST, DTC, MIL vs.
SRI), unit/torque-table conventions, and known OCR misread patterns are exactly the kind
of context that's easy to get wrong even when the raw text is right there. The glossary
covers this once, for every manual in the repo.

## Rules that apply to every manual in this repo

These are enforced by the cleanup process (`scripts/04_cleanup_methodology.md`) that
built every wiki here, so they hold regardless of which manual you're reading:

1. **Every numeric value (torque, clearance, resistance, voltage, part number) is
   guaranteed byte-identical to the original OCR scan.** Nothing numeric was ever
   "corrected" during cleanup, even when it looked wrong.
2. **Check `10-needs-review.md` before stating a spec as fact.** If a value is flagged,
   tell the user it's flagged and why — don't just state it.
3. **If a value looks wrong and is NOT already flagged**, say so explicitly. Don't
   silently trust it, and don't invent a "corrected" number yourself.
4. **Diagrams, wiring charts, and exploded views exist only in the PDF**, never as text
   in the markdown. When the user needs one, open the manual's committed PDF at the
   cited page rather than trying to describe it from markdown alone.
5. **Cite the source page number** when you answer from a manual, so the user can verify
   against the PDF themselves.
6. **Always check the alphabetical index first for any topic/component/symptom
   question** — before grepping or reading a chapter file directly. Do this even when
   you think you already know which chapter has the answer.

## Copyright note

These are copyrighted OEM manuals, committed here deliberately without a manufacturer
license (see [CONTRIBUTING.md](CONTRIBUTING.md)). That's a fact about how this repo was
built, not something you need to act on when answering questions — just don't reproduce
large verbatim chunks of manual text back to the user beyond what's needed to answer.
