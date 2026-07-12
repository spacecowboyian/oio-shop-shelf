#!/usr/bin/env bash
# publish-release.sh — move a manual's committed source PDF to a GitHub Release asset
# and repoint its manifest at the release URL, so the PDF never lands in git history.
#
# Run this on a manual PR's branch BEFORE squash-merging (see MAINTAINERS.md). It is
# idempotent: re-running re-uploads (--clobber) and leaves the manifest pointing at the
# same URL.
#
#   scripts/publish-release.sh manuals/toyota/vehicle/mr2-aw11
#
# Requires: gh (authenticated with repo write access), python3, git.
set -euo pipefail

dir="${1:?usage: scripts/publish-release.sh <manual-dir>   e.g. manuals/toyota/vehicle/mr2-aw11}"
dir="${dir%/}"
[ -f "$dir/manifest.yml" ] || { echo "No manifest.yml in '$dir'." >&2; exit 1; }

pdf="$(git ls-files "$dir/*.pdf" | head -1 || true)"
[ -n "$pdf" ] || { echo "No tracked PDF under '$dir' — nothing to publish." >&2; exit 1; }

slug="$(basename "$dir")"
tag="manuals-$slug"
repo="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
title="$(grep -m1 '^title:' "$dir/manifest.yml" | sed -E 's/^title:[[:space:]]*//; s/^"//; s/"$//')"
[ -n "$title" ] || title="$slug"

# Give the release asset a clean, slug-based name (source PDFs are sometimes named
# generically, e.g. "source.pdf").
asset="$slug.pdf"
upload="$pdf"
if [ "$(basename "$pdf")" != "$asset" ]; then
  upload="$(dirname "$pdf")/$asset"
  cp "$pdf" "$upload"
fi
url="https://github.com/$repo/releases/download/$tag/$asset"

echo "→ Publishing '$pdf' → release '$tag' on $repo (asset: $asset)"
if gh release view "$tag" >/dev/null 2>&1; then
  gh release upload "$tag" "$upload" --clobber
else
  gh release create "$tag" "$upload" \
    --title "$title — source PDF" \
    --notes "OCR'd + indexed source PDF for \`$dir\`.

Kept out of git history (see MAINTAINERS.md): the wiki markdown in the repo is authoritative
for specs and procedures — this PDF is only needed for diagrams, wiring charts, and exploded
views. This manual's \`manifest.yml\` \`source.location\` points at this asset."
fi

# Repoint the manifest: source.type -> url, source.location -> release URL. Edited with a
# targeted regex so comments and the rest of the file are preserved (only the first
# 2-space-indented type:/location: — which belong to the source: block — are touched).
python3 - "$dir/manifest.yml" "$url" <<'PY'
import re, sys
f, url = sys.argv[1], sys.argv[2]
s = open(f, encoding="utf-8").read()
s = re.sub(r'(?m)^(\s{2}type:)[^\n]*', r'\1 url', s, count=1)
s = re.sub(r'(?m)^\s{2}location:[^\n]*', '  location: "%s"' % url, s, count=1)
open(f, "w", encoding="utf-8").write(s)
PY

[ "$upload" = "$pdf" ] || rm -f "$upload"
git rm --quiet "$pdf"
git add "$dir/manifest.yml"

echo "✓ '$pdf' removed from git; manifest source → $url"
echo "  Next: commit these changes, confirm the 'no-pdf' check is green, then SQUASH-merge."
