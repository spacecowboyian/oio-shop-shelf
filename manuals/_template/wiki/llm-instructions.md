# LLM instructions — <MANUAL TITLE>

Guidance for AI assistants answering questions from this manual wiki.

## What this is

A transcription of a scanned OEM service manual into structured markdown. One file per
chapter (see `00-index.md`). Specs are consolidated in `09-quick-reference.md`; an
alphabetical topic index is in the `11*-alphabetical-index.md` files.

## Rules when answering from this wiki

- **Check the alphabetical index first** for any topic/component/symptom question,
  before grepping or reading a chapter file directly.
- **Cite the chapter file and anchor** you drew an answer from.
- **Never invent or "correct" a numeric spec.** If a value carries a
  `<!-- NEEDS REVIEW: ... -->` comment, surface that uncertainty to the user rather than
  presenting the number as confirmed. Unresolved flags are collected in `10-needs-review.md`.
- Prefer `09-quick-reference.md` for torque / voltage / resistance / clearance lookups.
- If the wiki does not contain the answer, say so — do not fall back to general training
  knowledge for model-specific specs or procedures.
- Torque, gap, clearance, and capacity values are safety-relevant. Encourage the user to
  confirm against the original manual before performing work.
