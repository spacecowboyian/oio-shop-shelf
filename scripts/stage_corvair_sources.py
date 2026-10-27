#!/usr/bin/env python3
"""Stage the original 1961 base and 1962–63 supplement PDF parts.

The catalog repeats links in its FC column. Files and inventories remain in _inbox/.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

import fitz

CATALOG = "https://corvanatics.org/service-dept/repair-manuals-bulletins/shop-manuals/"
ROOT = Path("_inbox/chevrolet-corvair-1963")
FALLBACKS = {
    "6e-autotrns-62-63.pdf": "https://www.corvairforum.com/forum/download/file.php?id=17676",
}


def fetch(url: str) -> bytes:
    cmd = ["curl", "--fail", "--location", "--silent", "--show-error", "--retry", "3"]
    if "corvanatics.org" in url:
        cmd += ["--user-agent", "Mozilla/5.0"]
    return subprocess.check_output(cmd + [url])


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href") or ""
        url = urljoin(CATALOG, href)
        path = urlsplit(url).path
        if path.lower().endswith(".pdf") and any(x in path.lower() for x in ("/shop61/", "/shop62-63/")):
            canonical = urlunsplit(("https", "corvanatics.org", path, "", ""))
            self.urls.setdefault(path.lower(), canonical)


def stage(url: str) -> dict:
    path = urlsplit(url).path
    source_id = "base-1961" if "/shop61/" in path.lower() else "supplement-1962-63"
    target = ROOT / source_id / Path(path).name
    target.parent.mkdir(parents=True, exist_ok=True)
    download_url = FALLBACKS.get(target.name.lower(), url)
    data = target.read_bytes() if target.exists() else fetch(download_url)
    if not (data.startswith(b"%PDF-") and b"%%EOF" in data[-2048:]):
        raise ValueError(f"Invalid/incomplete PDF: {url}")
    if not target.exists():
        target.write_bytes(data)
    with fitz.open(stream=data, filetype="pdf") as pdf:
        pages = pdf.page_count
        if not pages:
            raise ValueError(f"Empty PDF: {url}")
        page_labels = [pdf[i].get_label() or None for i in range(pages)]
        printed = []
        for page in pdf:
            top_blocks = sorted((block for block in page.get_text("blocks")
                                 if len(block) > 6 and block[6] == 0 and
                                 block[1] < page.rect.height * .12), key=lambda block: block[1])
            match = next((m for block in top_blocks
                          if (m := re.search(r"\b(6[A-E]|1[0-2]|[1-9])-([0-9]{1,3})\b", block[4]))), None)
            printed.append(match.group(0) if match else None)
    return {"source_id": source_id, "filename": target.name, "url": download_url,
            "catalog_url": url,
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
            "pages": pages, "pdf_page_labels": page_labels, "printed_page_ocr": printed,
            "scope": "commercial-only" if "body-FC" in target.name else "mixed-or-passenger"}


def main() -> None:
    parser = Links()
    parser.feed(fetch(CATALOG).decode("utf-8", "replace"))
    catalog_urls = list(parser.urls.values())
    urls = sorted((u for u in catalog_urls if "body-fc-61.pdf" not in u.lower()),
                  key=lambda x: ("/shop62-63/" in x, x.lower()))
    if sum("/shop61/" in u.lower() for u in catalog_urls) != 21 or sum("/shop62-63/" in u.lower() for u in catalog_urls) != 17:
        raise ValueError(f"Catalog changed: found {len(urls)} unique relevant PDFs")
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(stage_or_unavailable, urls))
    entries = [x for x in results if x.get("status") != "unavailable"]
    unavailable = [x for x in results if x.get("status") == "unavailable"]
    inventory = {"catalog": CATALOG, "captured_at_utc": datetime.now(timezone.utc).isoformat(),
                 "excluded_catalog_urls": [u for u in catalog_urls if "body-fc-61.pdf" in u.lower()],
                 "unavailable": unavailable,
                 "entries": entries}
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
    combined = fitz.open()
    with (ROOT / "source-page-map.jsonl").open("w") as out:
        for entry in entries:
            with fitz.open(ROOT / entry["source_id"] / entry["filename"]) as part:
                start = combined.page_count + 1
                combined.insert_pdf(part)
                entry["combined_page_start"] = start
                entry["combined_page_end"] = combined.page_count
            for number, label in enumerate(entry["pdf_page_labels"], 1):
                out.write(json.dumps({"source_id": entry["source_id"], "filename": entry["filename"],
                                      "pdf_page": number, "pdf_page_label": label,
                                      "original_page": entry["printed_page_ocr"][number - 1],
                                      "original_page_evidence": "OCR header" if entry["printed_page_ocr"][number - 1] else None,
                                      "combined_page": start + number - 1,
                                      "sha256": entry["sha256"], "url": entry["url"]}) + "\n")
    combined.set_toc([[1, entry["filename"], entry["combined_page_start"]] for entry in entries])
    combined.save(ROOT / "combined-working.pdf", garbage=4, deflate=True)
    combined.close()
    (ROOT / "inventory.json").write_text(json.dumps(inventory, indent=2) + "\n")
    print(f"Staged {len(entries)} PDFs, {sum(x['pages'] for x in entries)} pages in {ROOT}")
    if unavailable:
        raise RuntimeError(f"{len(unavailable)} relevant PDF(s) unavailable; see inventory.json")


def stage_or_unavailable(url: str) -> dict:
    try:
        return stage(url)
    except subprocess.CalledProcessError as exc:
        return {"url": url, "status": "unavailable", "error": str(exc)}


if __name__ == "__main__":
    main()
