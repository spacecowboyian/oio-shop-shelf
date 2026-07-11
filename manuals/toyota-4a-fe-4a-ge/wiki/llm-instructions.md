# Instructions for the AI assistant

You have access to a Toyota 4A-F / 4A-GE engine service manual: OCR'd markdown for search, plus the original scanned PDF for diagrams. Read this file first, before answering anything from these documents.

## What's in this bundle
- `00-index.md` — chapter list and how the linking works
- `01` through `08` — the manual's 8 chapters (Preparation, Service Specifications, Charging, Engine Mechanical, Ignition, Lubrication, Cooling, EFI). Each opens with an "In this chapter" mini-index, then page-by-page OCR text with a `#pN` anchor per page.
- `09-torque-specs.md` — every torque value in the manual, one table, linked back to its source page.
- `10-needs-review.md` — every spot where OCR was too garbled to trust. Nothing here was guessed at or silently fixed.
- `11-alphabetical-index.md` — ~970-entry back-of-book index (component, procedure, symptom, DTC code → page). **Start here for any topic lookup.**
- `Toyota-4A-F-4A-GE-engine-manual-OCR.pdf` — the source PDF. Diagrams, exploded views, and wiring charts exist ONLY here, never as text in the markdown.

## Where the PDF lives
These markdown files may be hosted two ways:
- **As a local folder/zip** — the PDF above sits right next to these `.md` files.
- **As wiki pages (e.g. Brains)** — the wiki stores markdown only, no binary files, so the PDF is NOT a sibling page. It lives on Google Drive instead:
  - PDF direct link: https://drive.google.com/file/d/1NuA7cEAkJwiVP4l5weaB9gh5vXHIxbOh/view
  - Full source folder (all files, for reference): https://drive.google.com/drive/u/0/folders/1bs-cEDegeIJHi_ez9-p82By3WKE8AaLX

Either way, don't guess — every page citation in this bundle (`[PDF p.N]`, `(PDF p.N)`, mini-index page ranges, torque-spec source links) is already a clickable link straight to that exact page, using the Drive `#page=N` deep-link format. Follow the link rather than constructing one yourself.

## Rules
1. For any topic/component/symptom question, check `11-alphabetical-index.md` first, not a raw text search of one chapter.
2. Every entry/anchor cites a page number and links to it. When the user needs a diagram or wiring chart, follow that link (or open the PDF above at that page) — don't attempt to describe a diagram from the markdown, it isn't there.
3. Every numeric value (torque, clearance, resistance, voltage, part number) in the markdown is guaranteed byte-identical to the original OCR scan. Nothing numeric was ever "corrected" during cleanup, even when it looked wrong.
4. Before stating any spec value as fact, check if it's flagged in `10-needs-review.md`. If it is, tell the user it's flagged and why, don't just state it.
5. If a value looks wrong on its own (e.g. a unit conversion that doesn't reconcile) and it's NOT already in the review file, say so explicitly — don't silently trust it, and don't invent a "corrected" number.
6. Ω (ohms) frequently OCR'd as the digit "2" throughout this manual (e.g. "125-200Ω" reads as "125-2002"). Keep that in mind reading resistance specs — it's a reading quirk, not necessarily an error.
7. Always cite the PDF page number back to the user when you answer from this manual, so they can verify against the source themselves.
