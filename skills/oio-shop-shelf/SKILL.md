---
name: oio-shop-shelf
description: "Answer questions from the OEM service manuals hosted in this repo using ChatGPT, Claude, Codex, or another capable assistant: torque specs, procedures, diagnostics, wiring, part numbers, diagrams, and source-page citations. Use whenever the user asks about a vehicle/engine/system that has a manual under the manuals directory, asks to look something up \"in the manual\" or \"in the service manual\", or needs repo-specific navigation for oio-shop-shelf."
---

This repo also ships the general-purpose **auto-mechanic** skill
(`skills/auto-mechanic/`, with a Claude-compatible copy at `.claude/skills/auto-mechanic/`).
Use it together with this one; do not answer from this skill alone. `auto-mechanic` owns
the mechanic behavior: never invent or "correct" a spec value, cite sources, treat
"check engine light" as ambiguous (MIL vs. SRI), watch for OCR misreads, and do not guess
at an abbreviation or DTC code that is not documented. This skill only owns navigation:
finding the right file in this specific repo.

## Assistant capability routing

- If running as a local CLI/repository agent, inspect files directly and use `grep`/`rg`.
- If running as hosted ChatGPT/Claude with uploaded files, use the uploaded repo/manual
  files and ask for missing files only when needed.
- If running as plain chat without file access, ask the user to paste the relevant
  `llm-instructions.md`, index rows, chapter excerpt, or page image before answering
  manual-specific questions.

## The startup cost floor — read this first

Firing up an agent to answer from this repo carries a **fixed token floor that must be met
and is retained for the whole session**: the agent's own system prompt + the full JSON
schemas of every tool it holds + the task prompt are loaded on startup, *before it reads a
single repo file*. Measured 2026-07-11, that floor is **~25.5K tokens** for a general-purpose
agent here, and it stays in context until the agent exits. It is identical under every
retrieval approach and **cannot be reduced by any index, file format, or navigation choice** —
only by prompt-caching the startup context or by not spawning a fresh agent per question
(both harness-level, outside this repo).

The practical rule this implies: **you can't beat the floor, so the whole game is adding as
few tokens as possible on top of it.** That is exactly what the fast path below is for —
one grep that returns one line, instead of reading chapter files. Don't expect a lookup to
cost less than the floor; do make sure it costs barely more.

## Navigation

**Fast path — a specific value (do this first).** If the question is a single value — a spec,
torque, clearance, resistance, voltage, capacity, DTC code, or part number — do NOT read the
glossary or any chapter file first. If the manual has `manuals/<slug>/data/manual-index.jsonl`,
`grep` it for the term, read the matching row, cite its `_page`, and **surface `_flags` if
non-empty** (that value is OCR-uncertain — don't state it as settled). Empty `_flags` = clean
transcription, answer directly. That's the whole path: root `llm-instructions.md` → grep index
→ answer. This is what keeps marginal cost near the floor.

**Deeper path — procedures, diagrams, diagnosis, or a value the index doesn't have.** Only
then:
1. Read the specific manual's `wiki/llm-instructions.md` — manual-specific details (exact
   filenames, chapter breakdown, known OCR quirks).
2. Read this repo's root `glossary.md` for automotive terminology + OEM manual conventions.
   (It's the canonical copy — prefer it over auto-mechanic's bundled copy, since you're
   already inside the repo.)
3. Grep/read the chapter files for the passage you need.

Either way, answer following **auto-mechanic's** rules, using what you found as your source.

This skill is a thin wrapper. `llm-instructions.md` is written to work for any LLM; if
you are ever unsure which file has the answer, the root file wins.
