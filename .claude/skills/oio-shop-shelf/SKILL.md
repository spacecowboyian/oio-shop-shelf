---
name: oio-shop-shelf
description: Answer questions from the OEM service manuals hosted in this repo (torque specs, procedures, diagnostics, wiring, part numbers). Use whenever the user asks about a vehicle/engine/system that has a manual under manuals/<slug>/, or asks to look something up "in the manual" or "in the service manual".
---

This repo also ships the general-purpose **auto-mechanic** Skill
(`.claude/skills/auto-mechanic/`) — use it together with this one, don't answer from this
skill alone. auto-mechanic owns the actual mechanic behavior: never invent or "correct" a
spec value, cite sources, treat "check engine light" as ambiguous (MIL vs. SRI), watch
for OCR misreads, and don't guess at an abbreviation or DTC code that isn't documented.
This skill (oio-shop-shelf) only owns *navigation* — finding the right file in this
specific repo.

## Navigation

1. Read `llm-instructions.md` at the repo root — it covers how `manuals/<slug>/` is laid
   out and how to pick the right manual for the user's question.
2. Read this repo's root `glossary.md` for automotive terminology + OEM manual
   conventions. (It's the canonical copy — prefer it over auto-mechanic's bundled copy
   of the same file, since you're already inside the repo.)
3. Read the specific manual's `wiki/llm-instructions.md` — manual-specific details (exact
   filenames, chapter breakdown, known OCR quirks) that the root file doesn't repeat.
4. Answer following auto-mechanic's rules, using what you found in steps 1–3 as your
   source material.

This skill is a thin wrapper. `llm-instructions.md` is written to work for any LLM, not
just Claude Code — if you're ever unsure which one has the answer, the root file wins.
