# LLM instructions — Toyota 4A-FE Engine Repair Manual (repair)

Manual-specific guidance. Read this before answering from this manual. Also read the repo
root `llm-instructions.md` and `glossary.md`, and answer following the **auto-mechanic**
rules (never invent/adjust a spec value, cite the source page).

> **Fetch-only agent (no shell / no GitHub MCP)?** Don't browse the folder — every file in
> this manual is listed as an absolute raw URL in [`all-files.md`](all-files.md). See the
> repo-root [`llm-instructions.md`](../../../../../llm-instructions.md) for why `/tree/` browsing
> fails and how to navigate by raw URL.

## Fast path for a specific value — `../data/manual-index.jsonl`
For any single-value lookup (a spec, torque, clearance, resistance, voltage, capacity, or part number), `grep ../data/manual-index.jsonl` for the term and stop — one flat file holds one JSON row per retrievable fact across the *whole* manual, so this resolves in one hop with no chapter-file read. Each row has the value fields plus `_page` (cite it), `_file`, `_section`, and `_flags`. **If `_flags` is non-empty, surface that OCR-uncertainty rather than stating the value as fact; if it's empty, the value is a clean transcription — answer directly.** This index is authoritative; do not also check the chapter files for the same value. Only fall through to the chapter files when the value isn't in `manual-index.jsonl` or the question is a procedure/diagnosis rather than a value lookup.

**This is a 4A-FE manual.** Toyota's cover titles it "4A-FE, 4A-GE," but the 4A-GE content
is incidental and insufficient for a 4A-GE repair. Answer 4A-GE questions only from the
handful of explicitly `(4A-GE)`-tagged items, and say plainly that this manual doesn't
cover a 4A-GE rebuild — point the user to a 4A-GE-specific manual.

## Three provenance landmines — do not ignore

1. **Bogus "reduce torque 40%" sticker.** The cover carries a Danish sticker:
   *"Alle mom[ent]er opgivet i den håndbog skal reduceres med 40%"* ("all torque values
   in this manual must be reduced by 40%"). This is a **third-party annotation** on this
   particular "Auto College Aalborg" copy, **not Toyota text.** Report Toyota's printed
   torque values verbatim. Never apply the 40% reduction, and warn the user the sticker
   exists if torque comes up.
2. **Abridged scan — pages are missing.** This is not a complete manual. Section page
   numbers skip (e.g. Starting System jumps ST-2 → ST-15; Engine Mechanical is missing
   ~24 numbered pages). If a procedure or spec seems to be missing, it probably is —
   say so rather than guessing, and suggest the other 4A manual. Run
   `scripts/check_page_continuity.py` to see the gap map.
3. **Encrypted source.** The original PDF was AES-encrypted (copy/print disabled);
   the committed copy was decrypted with `qpdf --decrypt`. No content was altered.

## Incidental 4A-GE content

A few items the manual prints for the 4A-GE are tagged `(4A-GE)` in the text and index
(e.g. a 4A-GE troubleshooting page, the planetary-starter component diagram, a thermostat
water-inlet fastener note, an ECU-voltage table for the 4A-GE w/o air flow meter). Treat
these as **incidental reference**, not 4A-GE repair coverage. Everything untagged is 4A-FE.

## Cross-checking with the other 4A manual

The repo also has [`toyota-4a-fe-4a-ge`](../../4a-fe-4a-ge/wiki/00-index.md) (the
Service & Maintenance Manual). For a gap in THIS abridged scan, that manual may have the
page. When the two disagree on a value, surface both with their sources — do not silently
pick one.

## Lookup

All 9 chapters are transcribed. Grep the `wiki/*.md` files, or use the baked-in alphabetical
index in the PDF. Cite the source page. This scan is abridged — if a procedure or spec seems
missing, it probably is; say so rather than guessing.
