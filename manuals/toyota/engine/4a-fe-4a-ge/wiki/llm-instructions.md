# Instructions for the AI assistant

You have access to a Toyota 4A-F / 4A-GE engine service manual: OCR'd markdown for search, plus the original scanned PDF for diagrams. Read this file first, before answering anything from these documents.

> **Fetch-only agent (no shell / no GitHub MCP)?** Don't browse the folder — every file in this manual is listed as an absolute raw URL in [`all-files.md`](all-files.md). See the repo-root [`llm-instructions.md`](../../../../../llm-instructions.md) for why `/tree/` browsing fails and how to navigate by raw URL.

## Fast path for a specific value — `../data/manual-index.jsonl`
**Experimental.** For any single-value lookup (a spec, torque, clearance, resistance, voltage, capacity, DTC code, or part number), `grep ../data/manual-index.jsonl` for the term and stop — one flat file holds one JSON row per retrievable fact across the *whole* manual, so this resolves in one hop with no chapter-file read. Each row has the value fields plus `_page` (cite it), `_file`, `_section`, and `_flags`. **If `_flags` is non-empty, surface that OCR-uncertainty rather than stating the value as fact; if it's empty, the value is a clean transcription — answer directly.** Never alter a numeric value. Only fall through to the chapter files / index below when the value isn't in `manual-index.jsonl` or the question is a procedure/diagram/diagnosis rather than a value lookup.

## What's in this bundle
- `00-index.md` — chapter list and how the linking works
- `01` through `08` — the manual's 8 chapters (Preparation, Service Specifications, Charging, Engine Mechanical, Ignition, Lubrication, Cooling, EFI). Each opens with an "In this chapter" mini-index, then page-by-page OCR text with a `#pN` anchor per page.
- `09-torque-specs.md` — every torque value in the manual, one table, linked back to its source page.
- `10-needs-review.md` — every spot where OCR was too garbled to trust. Nothing here was guessed at or silently fixed.
- `11-alphabetical-index.md` — ~970-entry back-of-book index (component, procedure, symptom, DTC code → page). Useful when a direct `grep` for a common component name returns too many unrelated hits to disambiguate — see Rules below.
- `Toyota-4A-F-4A-GE-engine-manual-OCR.pdf` — the source PDF. Diagrams, exploded views, and wiring charts exist ONLY here, never as text in the markdown.

## Where the PDF lives
The PDF is committed at `manuals/toyota-4a-fe-4a-ge/Toyota-4A-F-4A-GE-engine-manual-OCR.pdf`, a sibling of this `wiki/` folder — open it directly rather than following an external link. (If you're instead reading this via a wiki tool that stores markdown only, e.g. Brains, the PDF may not be a sibling page there; fall back to the source pointer in `manifest.yml`.)

Don't guess page numbers — every page citation in this bundle (`[PDF p.N]`, `(PDF p.N)`, mini-index page ranges, torque-spec source links) already tells you the exact source page to open.

## Rules
1. **Grep first.** For a specific spec value, DTC code, part number, or exact procedure name, `grep` across `wiki/*.md` — it almost always lands you on the right passage in one hop. **Escalate to `11-alphabetical-index.md` only when grep is too noisy** — i.e. the term is a common component/system name (e.g. "oil pump," "cylinder head") that shows up in many unrelated contexts and you can't quickly tell which hit answers the question. The index pre-splits common terms into disambiguated entries (e.g. "Oil pump, body clearance" vs. "Oil pump, installation") — search it for the specific phrase from the question, not just the bare component name.
2. Every entry/anchor cites a page number and links to it. When the user needs a diagram or wiring chart, follow that link (or open the PDF above at that page) — don't attempt to describe a diagram from the markdown, it isn't there.
3. Every numeric value (torque, clearance, resistance, voltage, part number) in the markdown is guaranteed byte-identical to the original OCR scan. Nothing numeric was ever "corrected" during cleanup, even when it looked wrong.
4. Before stating any spec value as fact, check if it's flagged in `10-needs-review.md`. If it is, tell the user it's flagged and why, don't just state it.
5. If a value looks wrong on its own (e.g. a unit conversion that doesn't reconcile) and it's NOT already in the review file, say so explicitly — don't silently trust it, and don't invent a "corrected" number.
6. Ω (ohms) frequently OCR'd as the digit "2" throughout this manual (e.g. "125-200Ω" reads as "125-2002"). Keep that in mind reading resistance specs — it's a reading quirk, not necessarily an error.
7. Always cite the PDF page number back to the user when you answer from this manual, so they can verify against the source themselves.
