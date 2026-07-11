# LLM instructions — Toyota 4A-FE / 4A-GE Engine Repair Manual (repair)

Manual-specific guidance. Read this before answering from this manual. Also read the repo
root `llm-instructions.md` and `glossary.md`, and answer following the **auto-mechanic**
rules (never invent/adjust a spec value, cite the source page).

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

## 4A-FE vs 4A-GE — keep them straight

The book covers **both** engines and switches between them within a section, often tagging
a subsection `(4A-FE)` or `(4A-GE)` (e.g. "Throttle Body (4A-FE)", "Fuel Pressure Control
System (4A-GE Europe)", "Service Specifications … (4A-FE)"). When you quote a value or
procedure, **state which engine it applies to.** If the manual doesn't tag it, say the
tag was absent rather than assuming it applies to both.

## Cross-checking with the other 4A manual

The repo also has [`toyota-4a-fe-4a-ge`](../../toyota-4a-fe-4a-ge/wiki/00-index.md) (the
Service & Maintenance Manual). For a gap in THIS abridged scan, that manual may have the
page. When the two disagree on a value, surface both with their sources — do not silently
pick one. (A future project will formalize the best-of-breed merge.)

## Lookup

Cleanup is in progress — most chapters are still raw. For a transcribed chapter (see the
cleanup column in [00-index.md](00-index.md)), grep the `wiki/*.md` files. For a
not-yet-cleaned chapter, the answer may only exist in the source PDF pages for that range.
