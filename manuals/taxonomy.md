# The automotive taxonomy

How manuals in this repo are organized so a human can browse to one and an agent can find
the right one for a given car. Two mechanisms, doing two different jobs:

1. **Folders** give every manual ONE human-browsable home.
2. **Front-matter tags** give every manual MANY machine-searchable match-keys.

A whole manual often spans several years, models, or cars — folders can't express that, so
they don't try. The crossover lives in the tags.

## 1. Folders — one home per manual

```
manuals/
  taxonomy.yml                       # the controlled vocabulary (see §3)
  taxonomy.md                        # this file
  <make>/                            # e.g. toyota/  (a make key from taxonomy.yml)
    vehicle/                         # whole-vehicle / chassis manuals
      <unit>/                        # e.g. mr2-aw11/
        manifest.yml
        README.md                    # front matter generated from the manifest (§2)
        wiki/ …
    engine/                          # engine-family manuals (span many cars)
      <unit>/                        # e.g. 4a-fe-repair/
        manifest.yml
        README.md
        wiki/ …
  _template/                         # skeleton for a new manual
```

Exactly **two buckets** under each make: `vehicle` and `engine`. That binary is what
handles "some manuals cross cars":

- **`vehicle/`** — a manual tied to one vehicle generation/chassis (a whole FSM, or a
  body/transmission/electrical manual for that chassis). Whatever systems it covers, it's
  one chassis, so it gets one home.
- **`engine/`** — a manual for an engine *family* (e.g. 4A-FE) that was fitted to many
  different cars. It has no single "model", so it lives by engine, not by car.

We deliberately do **not** split by system (brakes/suspension/etc.). `<unit>` is a short
folder name — the make is already implied by the parent, so `mr2-aw11`, not
`toyota-mr2-aw11`. The manifest's `slug` stays the globally-unique id and need not equal
the folder name.

## 2. Front-matter tags — many keys per manual

Each manual's `README.md` opens with a YAML front-matter block. **It is generated — never
hand-edit it.** `scripts/10_write_frontmatter.py` builds it from the manifest's `taxonomy:`
block, resolving keys to their canonical names in `taxonomy.yml`:

```yaml
---
# AUTO-GENERATED — taxonomy front matter (scripts/10_write_frontmatter.py); do not edit
slug: "toyota-mr2-aw11"
title: "Toyota MR2 (AW11) 1988 Service Manual"
make: "Toyota"
category: "vehicle"
models: ["MR2"]
chassis: ["AW11"]
engines: ["4A-GE", "4A-GZE"]
years: "1984-1989"
---
```

This is the discovery layer. An agent answering "1988 MR2, 4A-GE cam-cap torque" greps
`chassis: AW11` **or** `engines: 4A-GE` and lands on the right manual — the list fields mean
one manual matches many searches. Because it's generated from the manifest, it can never
drift from the source of truth.

## 3. `taxonomy.yml` — the controlled vocabulary

`taxonomy.yml` fixes the canonical spelling of every make, model, chassis and engine, so
"Toyota"/"toyota" and "MR2"/"MR-2" never fork across contributions. Every manifest's
`taxonomy:` block must resolve to keys defined there; **CI blocks a manifest that names a
make/model/engine not in the registry** (`scripts/validate_manifests.py`).

**Provenance.** Make and model names/IDs are anchored to the NHTSA **vPIC** catalog — the
US DOT's public-domain Vehicle Product Information Catalog
(<https://vpic.nhtsa.dot.gov/api/>). `vpic_make_id` is that catalog's stable `Make_ID`.
Engine-family codes have no clean open catalog, so those are OEM designations kept by hand.

Seed **only what a committed manual needs** — do not import all of vPIC.

## 4. Adding a manual — the taxonomy steps

The `convert-manual` skill walks the whole conversion; these are just the taxonomy-specific
parts.

### a. Decide the category
Engine-family manual → `engine`. Whole-vehicle/chassis manual → `vehicle`.

### b. Register the make/model/engine in `taxonomy.yml` (if new)
Do this **before** referencing it. For a make not yet present, look up its canonical name +
`Make_ID`:

```
curl -s 'https://vpic.nhtsa.dot.gov/api/vehicles/GetMakeForManufacturer/<mfr>?format=json'
# then, for a model list under that make:
curl -s 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/<id>?format=json'
```

Add the entry (keys are lower-kebab; `name` is the canonical vPIC value):

```yaml
makes:
  toyota:
    name: Toyota
    vpic_make_id: 448
    models:
      mr2:
        name: MR2
        chassis: [AW11]        # generation/chassis codes this repo has manuals for
    engines:
      4a-ge: { name: 4A-GE, family: A }
      4a-gze: { name: 4A-GZE, family: A }
```

### c. Put the manifest's `taxonomy:` block in it
```yaml
# engine manual
taxonomy:
  make: toyota
  category: engine
  engines: [4a-fe]

# vehicle manual
taxonomy:
  make: toyota
  category: vehicle
  models: [mr2]
  chassis: [aw11]
  engines: [4a-ge, 4a-gze]   # engines the vehicle uses
  years: "1984-1989"         # optional free-text span
```

### d. Place the folder + generate front matter
Copy `_template/` to `manuals/<make>/<category>/<unit>/`, then:

```
python scripts/validate_manifests.py                       # registry must resolve (CI gate)
python scripts/10_write_frontmatter.py manuals/<make>/<category>/<unit>/
```

The generator writes the README front matter. Never edit that block by hand — change the
manifest (or `taxonomy.yml`) and re-run.
