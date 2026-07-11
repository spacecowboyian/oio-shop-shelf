---
name: oio-shop-shelf
description: Answer questions from the OEM service manuals hosted in this repo (torque specs, procedures, diagnostics, wiring, part numbers). Use whenever the user asks about a vehicle/engine/system that has a manual under manuals/<slug>/, or asks to look something up "in the manual" or "in the service manual".
---

Read `llm-instructions.md` at the repo root first — it covers how manuals are laid out,
how to pick the right one, and the rules that apply to every manual in this repo
(never alter a spec value, check `10-needs-review.md`, cite source pages, etc.).

Once you've identified the right manual from its slug, read that manual's
`wiki/llm-instructions.md` before answering — it has manual-specific details (exact
filenames, chapter breakdown, known OCR quirks) that the root file doesn't repeat.

This skill is a thin wrapper. The root `llm-instructions.md` is written to work for any
LLM, not just Claude Code — if you're ever unsure which one has the answer, the root
file wins.
