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

| 04-cooling-system | Missing pages CO-16…CO-20 | Radiator components/disassembly/assembly absent from this scan (jumps CO-15 → CO-21). |
| 04-cooling-system | Thermostat valve lift "at 95°C" | OCR read 96°C; page image (CO-13) and the °F value (203°F = 95°C) confirm **95°C** — corrected from image. |
| 04-cooling-system | Cooling-fan circuit fuse/FL ratings | Read from a wiring diagram (e.g. "80A (AT171)" OCR'd "SOA"); verify against the page image before quoting. |

| 05-lubrication-system | Missing pages ≈ LU-10…LU-13 | Oil-pump removal/disassembly/inspection/assembly absent (section ends at LU-9); troubleshooting cites LU-12/13 for the relief valve but those pages aren't present. |
| 05-lubrication-system | Oil capacity differs vs Service Specs | LU-8 prints w/ filter 3.2 L (3.3 US qts); the A-2 spec section (not yet transcribed) prints 3.3 L (3.5 US qts). Reconcile when Service Specs is done. |
| 06-ignition-system | 4WD ignition-coil values | Primary 0.38–0.46 Ω / secondary 7.7–10.3 kΩ appear ONLY in the OCR'd diagnostic flowchart (unit-ambiguous); the IG-8 detail page shows 2WD only. Verify against a complete copy. This scan is a 2WD 4A-FE. |
| 06-ignition-system | Missing pages IG-3, IG-5, IG-10…IG-14 | Troubleshooting (IG-3) and distributor R&R detail (IG-10…14) absent from this scan. |

| 08-charging-system | Missing page CH-3 + alternator R&R (CH-8+) | On-vehicle inspection first steps (CH-3) and the alternator disassembly/inspection/reassembly (CH-8 onward) are absent; this scan ends at CH-7 (components). |
| 08-charging-system | Charging-circuit fuse/FL ratings | Read from the wiring diagram; verify against the page image. |

| 02-engine-mechanical | **Physical pages out of logical order** | The scan's physical page order does not follow the section codes (e.g. physical p23=EM-33, but p28–32=EM-6…10). Content in the EM file is ordered by physical page (so `[PDF p.N]` links are correct); read by the EM-code in each heading, not scroll order. |
| 02-engine-mechanical | Missing pages throughout EM | Many EM pages absent (EM-37 missing; EM-11…EM-32 not present in the p33+ range; cylinder-block detail largely absent). |
| 03-efi-system | FI section-page skips | The abridged FI section skips pages in several places (flagged inline per block). |

**All 9 chapters transcribed** (Introduction, Cooling, Lubrication, Ignition, Charging,
Starting, Engine Mechanical, EFI System, Service Specifications). Service Specs was
image-verified cell-by-cell at 200 dpi; where the manual's own imperial conversions look
off (e.g. a piston-diameter inch value), the printed value was kept verbatim per Rule 0.

The alphabetical index currently covers the first five chapters. **A consolidated per-engine
index expansion (adding EM/FI/Charging terms) + a density pass will run after Service
Specifications**, per plan — the EM/FI content is transcribed and ready to index. The FI and Service-Specification sections' running page codes did not OCR in the
header/footer band, so `check_page_continuity.py` can't gap-check them automatically; check
them by eye during cleanup.

### Note on 4A-FE vs 4A-GE specificity
Per [issue #9](https://github.com/spacecowboyian/oio-shop-shelf/issues/9), the alphabetical
index is split per engine. Many spec/procedure pages in this scan are titled `(4A-FE)`; the
4A-GE equivalents (ignition IIA, EFI) are largely **not present** in this scan. When a value
is engine-specific, cite the engine; when the manual leaves it untagged, don't assume it
applies to both without checking.
