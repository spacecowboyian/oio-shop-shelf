# Honda S2000 — Factory Service Manual conversion

> **Scope:** The manual covers U.S. and Canadian S2000 models from 2000–2008.
> Its VIN examples identify AP1/F20C1 for 2000–03 and AP2/F22C1 for 2004–08.

## What this manual is

Honda's factory service manual for the **S2000** roadster. It is a whole-vehicle FSM covering
engine, fuel/emissions, transaxle, chassis, body, and electronics. 1970 pages,
RC4-encrypted scan (decrypted in `01`), carries an OCR text layer (ABBYY
FineReader 9.0).

The conversion registers no standalone engine manual entries in `taxonomy.yml`.
The chassis and engine examples above come from the manual's VIN pages.

## What the manual COVERS (from its embedded bookmark outline / section headers)

Front matter, General Information, Specifications, Maintenance, **Engine Electrical**,
**Engine Mechanical** (Engine Assembly, Cylinder Head, Engine Block, Lubrication,
Intake Manifold & Exhaust, Cooling), **Fuel and Emissions** (largest section — split
into parts A–F), **Transaxle** (Clutch, Manual Transmission, Rear Differential,
Driveline/Axle), **Steering**, **Suspension**, **Brakes**, **Body**,
**Heating & Air Conditioning**, **Body Electrical** (parts A–C, includes wiring), and
**Restraints / SRS** (parts A–B).

## Caveats

- **27 chapter entries** in `manifest.yml`, split at ~90-page intervals for the large
  Fuel/Emissions, Transaxle, Body, and Body-Electrical sections. Section boundaries
  were verified at **all 25 bookmark outline entries plus 30+ content pages** — the
  print→physical offset is **0**; every seam is contiguous (1→1970, no gaps).
- **OCR is spaced-out** (e.g. `T h i s m a n u a l i s d i v i d e d`) — typical of the
  ABBYY scan layer; cleanup cross-checks values against the rendered page image and
  screens for the usual OCR-misreads (`auto-mechanic` glossary).
- **Restraints / SRS (Part B)** includes the airbag/pretensioner procedures — handle
  per the manual's SRS safety notes.
- **Provenance:** original © Honda / America Honda. The publication set selected
  for this package includes the chapter text, all 1,970 rendered page images,
  and the registered diagrams. The source PDF and raw OCR remain private and
  excluded from Git.
