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

## Why PDFs aren't committed — but diagram images are

**PDFs go to a Release.** They're huge (tens of MB each) and re-baking the clickable index
rewrites them, so every change would balloon `git clone` / tarball downloads. The markdown is
authoritative for specs and procedures, so the PDF is only needed to look at an original
scanned page. We host it on a Release and point `manifest.yml` at it.

**Diagram images stay in git.** A manual's `diagrams/*.png` are committed and their wiki embeds
stay relative. This is deliberate, and it is the one exception to "no binaries in history":

- A Release asset's download URL **302s to a signed URL on `release-assets.githubusercontent.com`**
  and is served as `application/octet-stream`. External AI assistants cannot follow that hop or
  recognise the result as an image — ChatGPT's web reader reports "Failed to fetch restricted
  URL", and the GitHub connector can't reach Release assets at all (they aren't repo contents).
- A file in the tree is served by `raw.githubusercontent.com` as `image/png`, same host as the
  markdown, no redirect. **Verified:** ChatGPT read a cylinder-head bolt sequence correctly off
  a raw URL, row for row.
- The cost is small. A manual's diagrams are a few MB — the A110's 72 images are 7 MB against a
  90 MB PDF — and unlike the PDF they are the thing a reader actually needs to open.

**Every page is an image too.** A manual also commits `page-images/p####.png` — the whole book,
one black-and-white PNG per page at 300 dpi — plus `data/pages.json` indexing them. That is how a
reader looks at *any* page without the PDF: each `**[PDF p.N]**` marker in the wiki links its own
page image, and `pages.json` gives a JS client (see `scripts/tv-reader`) or an assistant the page
list with both a `raw.githubusercontent.com` and a `cdn.jsdelivr.net` base URL.

Curated `diagrams/` entries stay — they are the figures worth calling out by name, with captions
and a `safety_relevant` flag — but a reader is no longer limited to them.

Cost, for the A110: 45 MB of page images and 7 MB of diagrams, against a 90 MB PDF. Only ever one
page crosses the network at a time.

So `publish-release.sh` moves **only the PDF**, and `no-pdf-guard` checks **only** `*.pdf`.

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
