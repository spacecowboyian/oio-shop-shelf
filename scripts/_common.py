"""Shared helpers for the oio-shop-shelf pipeline scripts."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: PyYAML. Run: pip install -r scripts/requirements.txt")

REQUIRED_MANIFEST_KEYS = ("slug", "title", "source", "rights", "chapters")
REQUIRED_CHAPTER_KEYS = ("file", "title", "page_start", "page_end")


def manual_dir(arg: str, require_manifest: bool = True) -> Path:
    """Resolve and validate a manuals/<slug>/ directory passed on the CLI.

    Most scripts need the manifest and keep ``require_manifest=True``. Step 01
    (decrypt + OCR) can run before the manifest exists, so it passes False — the
    directory must exist, but manifest.yml is not yet required.
    """
    d = Path(arg).resolve()
    if not d.is_dir():
        sys.exit(f"Not a directory: {d}")
    if require_manifest and not (d / "manifest.yml").is_file():
        sys.exit(f"No manifest.yml in {d}")
    return d


def load_manifest(mdir: Path, required: bool = True) -> dict:
    """Load and lightly validate manifest.yml. Exits on schema errors.

    With ``required=False``, a missing manifest.yml returns ``{}`` instead of
    exiting (so step 01 can OCR before the manifest is authored); a manifest that
    *is* present is still validated.
    """
    mf = mdir / "manifest.yml"
    if not mf.is_file():
        if required:
            sys.exit(f"No manifest.yml in {mdir}")
        return {}
    data = yaml.safe_load(mf.read_text(encoding="utf-8")) or {}
    errors = validate_manifest(data)
    if errors:
        sys.exit("manifest.yml is invalid:\n  - " + "\n  - ".join(errors))
    return data


def validate_manifest(data: dict) -> list[str]:
    """Return a list of human-readable schema errors (empty == valid).

    Kept import-free of the filesystem so CI can call it standalone.
    """
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["top-level manifest is not a mapping"]
    for key in REQUIRED_MANIFEST_KEYS:
        if key not in data or data[key] in (None, "", []):
            errors.append(f"missing required key: {key}")
    chapters = data.get("chapters")
    if isinstance(chapters, list):
        seen_files: set[str] = set()
        for i, ch in enumerate(chapters):
            if not isinstance(ch, dict):
                errors.append(f"chapters[{i}] is not a mapping")
                continue
            for k in REQUIRED_CHAPTER_KEYS:
                if k not in ch:
                    errors.append(f"chapters[{i}] missing key: {k}")
            f = ch.get("file")
            if f in seen_files:
                errors.append(f"chapters[{i}] duplicate file: {f}")
            if f:
                seen_files.add(f)
            ps, pe = ch.get("page_start"), ch.get("page_end")
            if isinstance(ps, int) and isinstance(pe, int) and ps > pe:
                errors.append(f"chapters[{i}] page_start {ps} > page_end {pe}")
    elif chapters is not None:
        errors.append("chapters must be a list")
    return errors


def wiki_dir(mdir: Path) -> Path:
    d = mdir / "wiki"
    d.mkdir(exist_ok=True)
    return d
