#!/usr/bin/env bash
# publish-release.sh — move a manual's source PDF to a GitHub Release and repoint the
# manifest at the release URL, so the (large) PDF never lands in git history (keeps clones
# light — see MAINTAINERS.md). Diagram images stay in the tree; see below.
#
# Run this on a manual PR's branch BEFORE squash-merging. It is idempotent: re-running
# re-uploads (--clobber) and leaves the manifest/wiki pointing at the same URLs.
#
#   scripts/publish-release.sh manuals/toyota/vehicle/mr2-aw11
#
# Handles the source PDF only: manifest `source:` flips local -> release URL and the PDF is
# removed from the tree.
#
# Diagram images are NOT touched. They stay committed in `diagrams/` so that
# `raw.githubusercontent.com` serves them to external readers: a Release asset 302s to a
# signed URL on another host and is served as application/octet-stream, which an external AI
# assistant can neither fetch nor read. A file in the tree is served as image/png from the
# same host as the markdown. Wiki embeds therefore stay relative (`../diagrams/x.png`).
#
# Requires: gh (authenticated with repo write access), python3, git.
set -euo pipefail

dir="${1:?usage: scripts/publish-release.sh <manual-dir>   e.g. manuals/toyota/vehicle/mr2-aw11}"
dir="${dir%/}"
[ -f "$dir/manifest.yml" ] || { echo "No manifest.yml in '$dir'." >&2; exit 1; }

pdf="$(git ls-files "$dir/*.pdf" | head -1 || true)"
if [ -z "$pdf" ]; then
  echo "No tracked PDF under '$dir' — nothing to publish. (Diagram images stay in the tree by design.)" >&2
  exit 1
fi

slug="$(basename "$dir")"
tag="manuals-$slug"
repo="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
title="$(grep -m1 '^title:' "$dir/manifest.yml" | sed -E 's/^title:[[:space:]]*//; s/^"//; s/"$//')"
[ -n "$title" ] || title="$slug"

# Ensure the manuals-<slug> release exists (both binary kinds upload into it). A manual's
# first PR usually carries the PDF; a later "add diagrams" PR may find the release already
# there from the original merge.
ensure_release() {
  gh release view "$tag" >/dev/null 2>&1 && return 0
  gh release create "$tag" \
    --title "$title — source material" \
    --notes "Source PDF for \`$dir\`.

Kept out of git history (see MAINTAINERS.md): the wiki markdown in the repo is authoritative
for specs and procedures, and this PDF is only needed for the original scanned pages. The
rendered diagram images are NOT here — they live in the repo under \`diagrams/\`, so that
raw.githubusercontent.com serves them to external readers."
}

# --- Source PDF: upload as a slug-named asset, repoint manifest, strip from tree ---------
if [ -n "$pdf" ]; then
  asset="$slug.pdf"                 # source PDFs are sometimes named generically
  upload="$pdf"
  if [ "$(basename "$pdf")" != "$asset" ]; then
    upload="$(dirname "$pdf")/$asset"
    cp "$pdf" "$upload"
  fi
  url="https://github.com/$repo/releases/download/$tag/$asset"

  echo "→ Publishing '$pdf' → release '$tag' on $repo (asset: $asset)"
  ensure_release
  gh release upload "$tag" "$upload" --clobber

  # Repoint the manifest: source.type -> url, source.location -> release URL. Targeted
  # regex so comments and the rest of the file are preserved (only the first 2-space
  # -indented type:/location: — which belong to the source: block — are touched).
  python3 - "$dir/manifest.yml" "$url" <<'PY'
import re, sys
f, url = sys.argv[1], sys.argv[2]
s = open(f, encoding="utf-8").read()
s = re.sub(r'(?m)^(\s{2}type:)[^\n]*', r'\1 url', s, count=1)
s = re.sub(r'(?m)^\s{2}location:[^\n]*', '  location: "%s"' % url, s, count=1)
open(f, "w", encoding="utf-8").write(s)
PY

  # Refresh the README so its front matter + visible "Source PDF" link point at the URL.
  if python3 scripts/10_write_frontmatter.py "$dir" >/dev/null 2>&1; then
    git add "$dir/README.md"
  else
    echo "  note: run 'python scripts/10_write_frontmatter.py $dir' to refresh the README PDF link (needs PyYAML)"
  fi

  [ "$upload" = "$pdf" ] || rm -f "$upload"
  git rm --quiet "$pdf"
  git add "$dir/manifest.yml"
  echo "✓ '$pdf' removed from git; manifest source → $url"
fi


echo "  Next: commit these changes, confirm the 'no-binary' checks are green, then SQUASH-merge."
