<!-- Adding or updating a manual? Keep this checklist. Other PRs: delete it and describe your change. -->

## Manual

- **Manual:** <!-- e.g. Toyota MR2 (AW11) 1988 FSM -->
- **Path:** `manuals/…/<slug>/`
- **Source:** <!-- where the PDF came from, e.g. archive.org item / your own scan -->

## Contributor checklist

- [ ] Ran the `convert-manual` pipeline; `wiki/` has the cleaned chapters + generated indexes.
- [ ] `manifest.yml` filled in (title, chapters with page ranges, rights note).
- [ ] `06_check_links.py` and `validate_manifests.py` pass locally.
- [ ] Source **PDF is committed** in the manual folder — this is fine and expected. A
      maintainer moves it to a GitHub Release at merge; you don't host anything.
- [ ] Numbers were never silently changed — anything uncertain is flagged
      `<!-- NEEDS REVIEW: … -->` (rolled up in `10-needs-review.md`).

> The **`no-pdf-guard`** check will be **red** while the PDF is committed — that's
> expected. It clears when a maintainer runs the release step. See
> [MAINTAINERS.md](../MAINTAINERS.md).

## Maintainer merge steps (do NOT skip — see MAINTAINERS.md)

- [ ] `scripts/publish-release.sh <manual-dir>` for each manual dir → commit → push.
- [ ] `no-pdf-guard` is green.
- [ ] **Squash-merge** (never rebase / merge-commit).
