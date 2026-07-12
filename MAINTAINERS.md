# Maintainer guide — merging manual PRs

This repo stays **text-light**: the wiki markdown is committed to git, but the (large)
source **PDFs live on GitHub Releases**, never in git history. This runbook is the
contract for getting a manual PR merged the right way. It's written so a **human or an AI
agent** with repo write access can follow it verbatim.

> **The one inviolable rule: SQUASH-merge. Never "Create a merge commit" or "Rebase and
> merge."** A squash collapses the PR to a single commit built from its final tree — so if
> the PDF has been removed from the branch, it never enters `main`'s history. A merge
> commit or rebase replays the "add PDF" commit and bakes the blob into history forever.

Squash-only is enforced in repo settings (Settings → Pull Requests). The `no-pdf-guard`
check is the safety net: it fails if any `*.pdf` would land on `main`.

## Why PDFs aren't committed

They're huge (tens of MB each) and re-baking the clickable index rewrites them, so every
change would balloon `git clone` / tarball downloads. The markdown is authoritative for
specs and procedures; the PDF is only needed for diagrams, wiring charts, and exploded
views. So we host the PDF on a Release and point `manifest.yml` at it.

## What a manual PR looks like when it arrives

The contributor ran the `convert-manual` pipeline and, for convenience, **committed the
source PDF** inside the manual folder (e.g. `manuals/toyota/vehicle/mr2-aw11/…​.pdf`) plus
the text (wiki, manifest, indexes). Because the PDF is committed, the **`no-pdf-guard`
check is RED — that is expected**, not a problem. Your job at merge time is to move that
PDF to a Release, which turns the check green.

## Merge procedure

1. **Review** the wiki content as usual (spot-check numbers against `10-needs-review.md`,
   confirm links, manifest validates).

2. **Publish the PDF to a Release and strip it from the tree.** On the PR branch, for each
   manual directory the PR adds or updates:
   ```bash
   scripts/publish-release.sh <manual-dir>     # e.g. scripts/publish-release.sh manuals/toyota/vehicle/mr2-aw11
   ```
   This creates/updates the `manuals-<slug>` Release, uploads the PDF as its asset,
   repoints the manifest `source:` at the release URL, and `git rm`s the PDF. It stages
   the changes; commit them:
   ```bash
   git commit -m "chore: move <slug> source PDF to release asset"
   git push
   ```
   *(Same-repo branch: you can also trigger the **publish-pdf-release** workflow from the
   Actions tab with the PR number instead of running the script locally. Fork PRs must use
   the local script — a workflow can't push to a fork's branch.)*

3. **Confirm `no-pdf-guard` is green** on the PR (the committed PDF is gone).

4. **Squash and merge.** That's it.

## Authoring your own manual (maintainer)

Same thing without a handoff: build locally (PDF committed in the folder, or just present),
run `scripts/publish-release.sh <manual-dir>`, commit, push, squash-merge.

## Release tag convention

One Release per manual, tagged `manuals-<slug>` where `<slug>` is the manual's leaf folder
name (e.g. `manuals-mr2-aw11`, `manuals-4a-fe-4a-ge`). The asset is `<slug>.pdf`. Its URL —
`https://github.com/<owner>/<repo>/releases/download/manuals-<slug>/<slug>.pdf` — is what
each `manifest.yml` `source.location` points to.

## Repo settings this relies on

- **Pull Requests:** *Allow squash merging* ON; *Allow merge commits* and *Allow rebase
  merging* OFF.
- **Branch protection on `main`:** require the `no-pdf-guard` and `validate` checks to pass.

## One-time history cleanup (already-committed PDFs)

PDFs committed before this workflow existed still sit in `main`'s history (they bloat
`git clone`, though not the tarball download of `main`). To reclaim that space, run a
`git filter-repo` pass to purge `*.pdf` blobs from history — a **coordinated, one-time**
operation that rewrites SHAs, so do it when no important PR is open and force-push with
everyone aware. It is intentionally not automated.
