#!/usr/bin/env bash
# publish-release.sh — move a manual's committed binaries (source PDF + diagram images)
# to a GitHub Release and repoint the manifest / wiki at the release URLs, so nothing
# binary ever lands in git history (keeps clones light — see MAINTAINERS.md).
#
# Run this on a manual PR's branch BEFORE squash-merging. It is idempotent: re-running
# re-uploads (--clobber) and leaves the manifest/wiki pointing at the same URLs.
#
#   scripts/publish-release.sh manuals/toyota/vehicle/mr2-aw11
#
# Handles two kinds of committed binary, both stripped from the tree here:
#   - the source PDF        -> manifest `source:` flips local -> release URL
#   - diagrams/*.webp       -> relative wiki embeds rewrite to the release URL (issue #1)
#
# Requires: gh (authenticated with repo write access), python3, git.
set -euo pipefail

dir="${1:?usage: scripts/publish-release.sh <manual-dir>   e.g. manuals/toyota/vehicle/mr2-aw11}"
dir="${dir%/}"
[ -f "$dir/manifest.yml" ] || { echo "No manifest.yml in '$dir'." >&2; exit 1; }

pdf="$(git ls-files "$dir/*.pdf" | head -1 || true)"
imgs="$(git ls-files "$dir/diagrams/*" || true)"
if [ -z "$pdf" ] && [ -z "$imgs" ]; then
  echo "No tracked PDF or diagram images under '$dir' — nothing to publish." >&2
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
    --notes "Source PDF + diagram images for \`$dir\`.

Kept out of git history (see MAINTAINERS.md): the wiki markdown in the repo is authoritative
for specs and procedures. The PDF and the rendered diagram/wiring/exploded-view images are
only needed to *show* the user something that has no text equivalent, so they live here."
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

# --- Diagram images: upload, rewrite relative wiki embeds to release URLs, strip ---------
if [ -n "$imgs" ]; then
  n="$(printf '%s\n' "$imgs" | grep -c . || true)"
  echo "→ Publishing $n diagram image(s) → release '$tag'"
  ensure_release
  # shellcheck disable=SC2086
  printf '%s\n' "$imgs" | xargs gh release upload "$tag" --clobber
  base="https://github.com/$repo/releases/download/$tag"

  # Rewrite each image's relative embed (e.g. ](../diagrams/pNNNN.webp)) to its release URL
  # across the manual's wiki/*.md — the same "flip the link at merge" the PDF does. The
  # committed relative form is what let a reviewer preview the image inside the PR.
  python3 - "$dir/wiki" "$base" <<'PY'
import re, sys, pathlib
wiki, base = pathlib.Path(sys.argv[1]), sys.argv[2]
# ](<any ../>diagrams/<name>) -> ](<base>/<name>)
pat = re.compile(r'\]\((?:\.\./)*diagrams/([^)\s]+)\)')
for md in wiki.glob("*.md"):
    s = md.read_text(encoding="utf-8")
    ns = pat.sub(lambda m: "](%s/%s)" % (base, m.group(1)), s)
    if ns != s:
        md.write_text(ns, encoding="utf-8")
PY

  while IFS= read -r img; do
    [ -n "$img" ] && git rm --quiet "$img"
  done <<EOF
$imgs
EOF
  git add "$dir/wiki" 2>/dev/null || true
  echo "✓ diagram image(s) removed from git; wiki embeds repointed to $base/"
fi

echo "  Next: commit these changes, confirm the 'no-binary' checks are green, then SQUASH-merge."
