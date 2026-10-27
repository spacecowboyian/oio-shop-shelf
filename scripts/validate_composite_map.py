#!/usr/bin/env python3
"""Check a composite's source-page map for missing or duplicated physical pages."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import load_manifest, manual_dir  # noqa: E402


def validate(mdir: Path) -> list[str]:
    manifest = load_manifest(mdir)
    composite = manifest.get("composite")
    if not composite:
        return []
    rows = [json.loads(line) for line in
            (mdir / composite["provenance_map"]).read_text().splitlines()]
    errors = []
    actual = [r["combined_page"] for r in rows]
    expected = list(range(1, manifest["source"]["pages"] + 1))
    if actual != expected:
        errors.append("combined pages are missing, duplicated, or out of order")
    valid_ids = {s["id"] for s in composite["sources"]}
    groups = defaultdict(list)
    for row in rows:
        if row["source_id"] not in valid_ids:
            errors.append(f"unknown source ID: {row['source_id']}")
        groups[(row["source_id"], row["filename"])].append(row)
    for key, pages in groups.items():
        if [x["pdf_page"] for x in pages] != list(range(1, len(pages) + 1)):
            errors.append(f"noncontinuous original PDF pages: {key}")
        if len({x["sha256"] for x in pages}) != 1:
            errors.append(f"inconsistent source hash: {key}")
    inventory_path = composite.get("source_inventory")
    if inventory_path:
        inventory = json.loads((mdir / inventory_path).read_text())
        entries = {(e["source_id"], e["filename"]): e for e in inventory["entries"]}
        if set(entries) != set(groups):
            errors.append("source inventory and page map list different PDFs")
        for key, pages in groups.items():
            entry = entries.get(key)
            if entry and (len(pages) != entry["pages"] or
                          pages[0]["sha256"] != entry["sha256"] or
                          pages[0]["combined_page"] != entry["combined_page_start"] or
                          pages[-1]["combined_page"] != entry["combined_page_end"]):
                errors.append(f"source inventory mismatch: {key}")
    covered = []
    for ch in manifest["chapters"]:
        for source_range in ch.get("source_ranges") or [ch]:
            covered.extend(range(source_range["page_start"], source_range["page_end"] + 1))
            for n in range(source_range["page_start"], source_range["page_end"] + 1):
                if (n > len(rows) or rows[n - 1]["source_id"] != source_range["source_id"] or
                        rows[n - 1]["filename"] != source_range.get("source_file", rows[n - 1]["filename"])):
                    errors.append(f"chapter source/range mismatch: {ch['file']}")
                    break
    if sorted(covered) != expected:
        errors.append("chapter source ranges do not cover every combined page exactly once")
    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python scripts/validate_composite_map.py <manual-dir>")
    failures = validate(manual_dir(sys.argv[1]))
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    if failures:
        sys.exit(1)
    print("Composite source-page map OK")
