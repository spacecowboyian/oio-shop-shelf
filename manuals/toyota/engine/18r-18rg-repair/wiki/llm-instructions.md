# LLM instructions — Toyota 18R / 18R-C / 18R-G Engine Repair Manual

Guidance for AI assistants answering questions from this manual wiki.

> **Fetch-only agent (no shell / no GitHub MCP)?** Don't browse the folder — every file in
> this manual is listed as an absolute raw URL in [`all-files.md`](all-files.md). See the
> repo-root [`llm-instructions.md`](../../../../../llm-instructions.md) for why `/tree/` browsing
> fails and how to navigate by raw URL.

## Fast path for a specific value — `../data/manual-index.jsonl`
For any single-value lookup (a spec, torque, clearance, resistance, voltage, capacity, or part number), `grep ../data/manual-index.jsonl` for the term and stop — one flat file holds one JSON row per retrievable fact across the *whole* manual, so this resolves in one hop with no chapter-file read. Each row has the value fields plus `_page` (cite it), `_file`, `_section`, and `_flags`. **If `_flags` is non-empty, surface that OCR-uncertainty rather than stating the value as fact; if it's empty, the value is a clean transcription — answer directly.** This index is authoritative; do not also check the chapter files for the same value. Only fall through to the chapter files when the value isn't in `manual-index.jsonl` or the question is a procedure/diagnosis rather than a value lookup.

## What this is

A transcription of a scanned OEM service manual into structured markdown. One file per
chapter (see `00-index.md`). Specs are consolidated in `09-quick-reference.md`; an
alphabetical topic index is in the `11*-alphabetical-index.md` files.

## Rules when answering from this wiki

- **Grep first, escalate to the alphabetical index only when grep is too noisy.** For a
  specific spec value, code, part number, or exact procedure name, `grep` across the
  chapter files — it almost always lands you on the right passage in one hop. Escalate
  to `11*-alphabetical-index.md` when the term is a common component/system name that
  turns up in many unrelated contexts and you can't quickly tell which hit is relevant —
  the index pre-splits common terms into disambiguated sub-topic entries.
- **Cite the chapter file and anchor** you drew an answer from.
- **Never invent or "correct" a numeric spec.** If a value carries a
  `<!-- NEEDS REVIEW: ... -->` comment, surface that uncertainty to the user rather than
  presenting the number as confirmed. Unresolved flags are marked inline with `<!-- NEEDS REVIEW: ... -->` comments in the chapter.
- Prefer `09-quick-reference.md` for torque / voltage / resistance / clearance lookups.
- If the wiki does not contain the answer, say so — do not fall back to general training
  knowledge for model-specific specs or procedures.
- Torque, gap, clearance, and capacity values are safety-relevant. Encourage the user to
  confirm against the original manual before performing work.
