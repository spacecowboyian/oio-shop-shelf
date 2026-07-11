# Needs Review — Toyota 4A-FE / 4A-GE Engine Repair Manual (repair)

Open flags for this manual. Priority items first. This scan is abridged and carries a
bogus third-party torque sticker — both are documented here so nobody trusts them by
accident.

## Priority

| Item | Reason | Source |
| ---- | ------ | ------ |
| **"Reduce all torque 40%" sticker is NOT Toyota** | Third-party Danish sticker on the cover of this "Auto College Aalborg Special Edition" copy. Do not apply it to any torque value; record Toyota's printed values verbatim. | PDF p.1 (cover) |
| **Abridged scan — pages missing throughout** | `check_page_continuity.py` flags gaps in EM, IG, ST (e.g. ST-2→ST-15; EM missing ~24 numbered pages; section page numbers run past the physical pages present). Do not assume any section is complete. | whole manual |

## Per-chapter (cleanup in progress)

Only Starting System is transcribed so far; its flags:

| Chapter | Item | Reason |
| ------- | ---- | ------ |
| 07-starting-system | Missing pages ST-4…ST-14 | Starter removal/disassembly/inspection/reassembly absent from this scan (jumps ST-3 → ST-15). |
| 07-starting-system | Pinion clearance "1 – 5 mm (0.04 – 0.20 in.)" | Verified against page image and internally consistent, but unusually large; confirm against a complete copy. |
| 07-starting-system | Fusible-link ratings in circuit diagram | OCR'd from a wiring diagram (e.g. "80A"/"BOA", "AT180"/"AT1 BO" ambiguous); verify against the page image before quoting. |

Chapters IN, EM, FI, CO, LU, IG, CH, and the spec sections are **not yet cleaned** — their
flags will be added as they're transcribed. The FI, CO, and Service-Specification sections'
running page codes did not OCR in the header/footer band, so `check_page_continuity.py`
can't gap-check them automatically; check them by eye during cleanup.
