# Pull request walkthrough (first-timer friendly)

Use this to get a contributor's finished `manuals/<slug>/` package onto GitHub as a
pull request. Assume they may **never have opened a PR**. Explain each step in one
line, give the exact command, and check it worked before moving on.

## Before you start

- Confirm the package is complete and verified (skill steps 1–7): manifest valid,
  links check clean, `10-needs-review.md` reflects real open items (that's fine —
  flagged items are expected, silently-wrong numbers are not).
- Ask if they have a GitHub account and `git` installed. If not:
  - Account: https://github.com/signup
  - git: `brew install git` (macOS) / https://git-scm.com/downloads
  - `gh` CLI (optional but easier): https://cli.github.com — then `gh auth login`.

## Path A — with the `gh` CLI (simplest)

```bash
gh repo fork spacecowboyian/oio-shop-shelf --clone        # fork + clone in one step
cd oio-shop-shelf
git checkout -b add-<slug>                                 # a branch named for the manual
# ...copy the finished manuals/<slug>/ package into place...
git add manuals/<slug>
git commit -m "Add <Make Model> service manual (<slug>)"
git push -u origin add-<slug>
gh pr create --fill                                        # opens the PR; edit title/body
```

## Path B — plain git + the GitHub website

1. **Fork**: on https://github.com/spacecowboyian/oio-shop-shelf click **Fork** (top right).
2. **Clone your fork**:
   ```bash
   git clone https://github.com/<your-username>/oio-shop-shelf.git
   cd oio-shop-shelf
   ```
3. **Branch**: `git checkout -b add-<slug>`
4. **Add the files**: copy your `manuals/<slug>/` folder into the repo.
5. **Stage + commit**:
   ```bash
   git add manuals/<slug>
   git commit -m "Add <Make Model> service manual (<slug>)"
   ```
6. **Push**: `git push -u origin add-<slug>`
7. **Open the PR**: GitHub prints a "Compare & pull request" link after the push, or
   go to your fork on github.com and click **Contribute → Open pull request**. Target
   the base repo's default branch.

## What a good PR description says

- **What manual** this is (make, model, engine/system, year range, page count).
- **Rights**: where the PDF came from and your read on redistribution — the project
  commits source PDFs as a considered risk; see `CONTRIBUTING.md`. Be honest here.
- **Open items**: point to `10-needs-review.md` — list anything you flagged and
  couldn't resolve against the page image. Reviewers expect flags, not perfection.
- **Any new cleanup rule** you propose (an edit to `scripts/04_cleanup_methodology.md`),
  with the case that motivated it (ties to issue #3).

## Common snags

- **"Permission denied (publickey)"** on push → you're pushing to the base repo, not
  your fork, or need HTTPS/`gh auth login`. Check `git remote -v` points at *your* fork.
- **Large PDF** → that's expected; the repo commits source PDFs. Don't use Git LFS
  unless a maintainer asks.
- **Accidentally committed intermediates** (`prepared.pdf`, `raw-ocr/`, `pages/`) →
  they're gitignored; `git rm --cached` them if they slipped in.
- **Branch already has upstream changes** → `git pull --rebase upstream main` after
  `git remote add upstream https://github.com/spacecowboyian/oio-shop-shelf.git`.
