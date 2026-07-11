# oio-shop-shelf

> Turn scanned OEM service-manual PDFs into clean, AI- and human-readable markdown wikis.

`oio-shop-shelf` is an open-source, extensible toolkit that converts scanned/OCR'd
service-manual PDFs into a well-structured markdown wiki: real tables (not ASCII-art
dumps of image-based charts), numbered procedures as lists, diagnostic flowcharts as
step-tables, a chapter index, an alphabetical back-of-book index, a quick-reference
spec index, and a consolidated "needs review" log.

The output is **plain markdown, browsable on GitHub as-is** — no hosted product, no
database, no lock-in to any particular tool.

## Why

Service manuals are indispensable and almost universally awful to read as scanned PDFs:
image-based tables, no search, no cross-references, no clean text layer. Once a manual
is transcribed into structured markdown it becomes greppable, linkable, diffable, and
readable by both people and AI assistants.

## The core promise: never silently change a number

Cleanup **never alters a numeric or spec value**. Where OCR is ambiguous, the value is
flagged inline with a reason:

```markdown
Torque: 34 <!-- NEEDS REVIEW: OCR read "34" but page image may show "84"; verify against p.112 -->
```

Flags are rolled up into a single `10-needs-review.md` per manual so a human can resolve
them. Garbage-in stays flagged — it is never guessed at.

## Reference implementation

The pipeline was first built by hand against the **Toyota 4A-F / 4A-GE engine manual**
(a 219-page scanned PDF reduced to a ~25-page structured markdown wiki). That manual is
the worked example this repo generalizes from.

## How it works

Deterministic work is done by ordinary CLI scripts. The one expensive,
human-supervised step — reconstructing clean tables and procedures from messy OCR — is
driven by a **written methodology prompt** ([`scripts/04_cleanup_methodology.md`](scripts/04_cleanup_methodology.md))
that *any* capable AI agent can follow (Claude Code, plain Claude, ChatGPT, etc.). You
do not need any specific tool to contribute.

```
PDF ──01_prepare──▶ OCR'd PDF ──02_render──▶ page PNGs ┐
                          │                             ├─▶ [AI cleanup step] ─▶ wiki/*.md
                          └──03_split──▶ per-chapter raw drafts ┘
                                                                       │
                              05_build_indexes ◀──────────────────────┘
                                     │
                              06_check_links (also runs in CI)
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full end-to-end workflow.

## Repo layout

```
manuals/
  <manual-slug>/            e.g. toyota-4a-fe-4a-ge/
    manifest.yml            title, source pointer, license note, chapter page-ranges → filenames
    <manual>.pdf             source PDF, committed alongside the wiki — see Licensing below
    wiki/                   generated output — THE SOURCE OF TRUTH
      00-index.md
      01-....md, 02-....md  one file per chapter (split further if huge)
      09-quick-reference.md torque/voltage/resistance/clearance specs, linked to source anchors
      10-needs-review.md    consolidated flag list
      11a..-alphabetical-index.md
      llm-instructions.md   per-manual guidance for AI assistants consuming the wiki
    raw-ocr/                gitignored intermediate OCR text (regenerable, not committed)
  _template/                skeleton for a new manual

scripts/                    01-06 pipeline + 07 optional Brains mirror (disabled)
.github/workflows/          CI: link check + manifest schema validation
llm-instructions.md         entry point for ANY LLM answering questions from a manual here
glossary.md                  automotive terminology + OEM manual conventions an LLM needs
                              to correctly interpret a manual, not just read it
.claude/skills/              thin Claude Code Skill wrapper around llm-instructions.md
```

## Using this repo with an AI assistant

Point it at [`llm-instructions.md`](llm-instructions.md) — works with any LLM, not just
Claude Code. It explains how manuals are laid out and the rules every manual's wiki
follows (never alter a spec value, cite source pages, etc.), points at
[`glossary.md`](glossary.md) for the automotive terminology and OEM manual conventions
an LLM needs to *understand* a manual rather than just read it, then routes to the
manual-specific `wiki/llm-instructions.md` for the one the user's asking about. Claude
Code users get this automatically via `.claude/skills/oio-shop-shelf/`.

## Status

Pre-release (**v0.1**, scaffolding). See the milestones below.

- **v0.1** — scaffold repo, port the Toyota 4A manual as the reference example, scripts 01–06 functional end to end.
- **v0.2** — CI validation wired up, manifest schema finalized, dogfood on a second manual to prove the pipeline generalizes.
- **v0.3** — revisit optional Brains mirror (`07_push_to_brains.py`).
- **v0.4** — public announcement.

## Licensing

The **tooling** in this repo is released under [MIT](LICENSE) *(placeholder — may change to Apache-2.0)*.

**Source manuals are a separate matter.** OEM service manuals are typically copyrighted
by the manufacturer/publisher, and this repo commits the source PDF alongside each
manual's wiki anyway — deliberately, so both the markdown and an AI assistant reading it
can cross-check diagrams, wiring charts, and exploded views that never made it into text.
This is a considered risk, not an oversight: no license/permission has been sought from
any manufacturer, and a takedown request could land at any time. See
[CONTRIBUTING.md](CONTRIBUTING.md) before adding a new manual.

---

Part of the **oio** family of tools.
