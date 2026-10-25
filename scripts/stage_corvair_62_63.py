#!/usr/bin/env python3
"""Stage Corvanatics 1962-63 Corvair supplement PDFs for oio-shop-shelf.

Run from the repository root:
    python3 scripts/stage_corvair_62_63.py

The source archive contains repeated links under 'FC pages'; URLs are
intentionally de-duplicated. Output stays in the repo's gitignored _inbox/.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

SOURCE = 'https://corvanatics.org/service-dept/repair-manuals-bulletins/shop-manuals/'
DEST = Path('_inbox/chevrolet-corvair-1962-1963-supplement')
USER_AGENT = 'oio-shop-shelf-manual-staging/1.0 (personal archival research)'


class PdfLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != 'a':
            return
        href = dict(attrs).get('href')
        if href:
            url = urljoin(SOURCE, href)
            path = urlsplit(url).path
            if '/shop62-63/' in path.lower() and path.lower().endswith('.pdf'):
                # Strip querystrings and fragments from the canonical source URL.
                parts = urlsplit(url)
                clean = urlunsplit((parts.scheme, parts.netloc, parts.path, '', ''))
                if clean not in self.links:
                    self.links.append(clean)


def get(url: str) -> bytes:
    last = None
    for attempt in range(4):
        try:
            req = Request(url, headers={'User-Agent': USER_AGENT, 'Referer': SOURCE})
            with urlopen(req, timeout=60) as response:
                return response.read()
        except Exception as error:
            last = error
            if attempt < 3:
                time.sleep(2 ** attempt)
    raise RuntimeError(f'Could not fetch {url}: {last}')


def order_key(url: str) -> tuple[int, str, str]:
    name = unquote(urlsplit(url).path.rsplit('/', 1)[-1]).lower()
    match = re.match(r'^(\d+)([a-z]?)\W?', name)
    return (int(match.group(1)) if match else 999,
            match.group(2) if match else '', name)


def valid_pdf(data: bytes) -> bool:
    return data[:1024].lstrip().startswith(b'%PDF-') and b'%%EOF' in data[-2048:]


def main() -> int:
    html = get(SOURCE).decode('utf-8', errors='replace')
    parser = PdfLinkParser()
    parser.feed(html)
    links = sorted(parser.links, key=order_key)
    if len(links) < 15:
        raise RuntimeError(f'Only found {len(links)} unique supplement PDFs (expected ~17). '
                           'The source page may have changed; no downloads attempted.')
    DEST.mkdir(parents=True, exist_ok=True)
    print(f'Found {len(links)} distinct 1962-63 PDF links; staging in {DEST}/')

    entries = []
    for idx, url in enumerate(links, 1):
        filename = Path(unquote(urlsplit(url).path)).name
        target = DEST / filename
        reused = target.is_file() and valid_pdf(target.read_bytes())
        if not reused:
            blob = get(url)
            if not valid_pdf(blob):
                raise RuntimeError(f'Not a complete PDF: {url} ({len(blob)} bytes)')
            target.write_bytes(blob)
        blob = target.read_bytes()
        entry = {'filename': filename, 'url': url, 'bytes': len(blob),
                 'sha256': hashlib.sha256(blob).hexdigest(),
                 'status': 'reused' if reused else 'downloaded'}
        entries.append(entry)
        print(f'  {idx:02d}/{len(links)} {filename} ({len(blob):,} B; {entry["status"]})')

    merged_filename = 'chevrolet-corvair-1962-1963-shop-manual-supplement.pdf'
    merge_error = None
    try:
        import fitz  # PyMuPDF; included in the repository's scripts/requirements.txt.
        combined = fitz.open()
        toc = []
        for item in entries:
            src = fitz.open(DEST / item['filename'])
            if src.page_count == 0:
                raise RuntimeError(f'Empty PDF: {item["filename"]}')
            start = combined.page_count + 1
            toc.append([1, item['filename'].rsplit('.', 1)[0], start])
            combined.insert_pdf(src)
            item['pages'] = src.page_count
            item['merged_page_start'] = start
            item['merged_page_end'] = combined.page_count
            src.close()
        combined.set_toc(toc)
        output = DEST / merged_filename
        combined.save(output, garbage=4, deflate=True)
        combined.close()
        print(f'Merged {len(entries)} parts into {output} ({sum(x["pages"] for x in entries)} pages).')
    except ImportError:
        merge_error = ('PyMuPDF unavailable: PDFs are staged, but merging and per-file page ranges '
                       'require: python3 -m pip install -r scripts/requirements.txt')
        print('NOTE:', merge_error)

    inventory = {
        'title': 'Chevrolet Corvair and Corvair 95 — 1962–1963 Shop Manual Supplement',
        'source_page': SOURCE,
        'downloaded_at_utc': datetime.now(timezone.utc).isoformat(),
        'manual_kind': 'supplement',
        'dependency': '1961 Corvair and Corvair 95 Shop Manual (base manual, not included)',
        'note': 'Multiple archive links may point to one PDF; duplicates are downloaded once. '
                'Separate supplement sections are preserved here alongside the merged PDF.',
        'merged_pdf': merged_filename if not merge_error else None,
        'merge_error': merge_error,
        'parts': entries,
    }
    (DEST / 'sources.json').write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + '\n')
    print(f'Wrote {DEST / "sources.json"}')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(1)
