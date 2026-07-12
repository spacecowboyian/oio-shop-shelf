"""Shared helpers for the oio-shop-shelf pipeline scripts."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: PyYAML. Run: pip install -r scripts/requirements.txt")

REQUIRED_MANIFEST_KEYS = ("slug", "title", "source", "rights", "chapters", "taxonomy")
REQUIRED_CHAPTER_KEYS = ("file", "title", "page_start", "page_end")
TAXONOMY_CATEGORIES = ("engine", "vehicle")


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
    errors += _taxonomy_shape_errors(data.get("taxonomy"))
    return errors


def _taxonomy_shape_errors(tax) -> list[str]:
    """Shape-only checks for the manifest `taxonomy:` block (no registry needed).

    Registry cross-reference (do these keys EXIST in taxonomy.yml?) is a separate step —
    see validate_against_taxonomy — because that needs the filesystem and this must stay
    import-free so CI can call validate_manifest standalone.
    """
    errors: list[str] = []
    if tax is None:
        return errors  # absence already reported by the REQUIRED_MANIFEST_KEYS loop
    if not isinstance(tax, dict):
        return ["taxonomy must be a mapping"]
    if not tax.get("make"):
        errors.append("taxonomy.make is required")
    cat = tax.get("category")
    if cat not in TAXONOMY_CATEGORIES:
        errors.append(f"taxonomy.category must be one of {TAXONOMY_CATEGORIES}")
    if cat == "engine":
        if not _nonempty_list(tax.get("engines")):
            errors.append("taxonomy.engines must be a non-empty list for category: engine")
    elif cat == "vehicle":
        if not _nonempty_list(tax.get("models")):
            errors.append("taxonomy.models must be a non-empty list for category: vehicle")
    for key in ("engines", "models", "chassis"):
        if key in tax and not isinstance(tax[key], list):
            errors.append(f"taxonomy.{key} must be a list")
    return errors


def _nonempty_list(v) -> bool:
    return isinstance(v, list) and len(v) > 0


def taxonomy_path(manuals_root: Path) -> Path:
    return manuals_root / "taxonomy.yml"


def load_taxonomy(manuals_root: Path) -> dict:
    """Load manuals/taxonomy.yml (the controlled vocabulary). Exits if missing/broken."""
    p = taxonomy_path(manuals_root)
    if not p.is_file():
        sys.exit(f"No taxonomy.yml in {manuals_root} — the taxonomy registry is required.")
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    if not isinstance(data.get("makes"), dict):
        sys.exit(f"{p} is invalid: top-level `makes:` mapping missing.")
    return data


def validate_against_taxonomy(data: dict, taxonomy: dict) -> list[str]:
    """Cross-reference a manifest's `taxonomy:` block against taxonomy.yml.

    Returns human-readable errors when a make/model/chassis/engine the manifest declares
    is not registered in taxonomy.yml. Keeps the registry canonical (register-first).
    """
    errors: list[str] = []
    tax = data.get("taxonomy")
    if not isinstance(tax, dict):
        return errors  # shape errors already reported elsewhere
    makes = taxonomy.get("makes") or {}
    mk = tax.get("make")
    make_entry = makes.get(mk)
    if make_entry is None:
        errors.append(
            f"taxonomy.make '{mk}' is not in taxonomy.yml — add it there first "
            f"(see manuals/taxonomy.md)."
        )
        return errors  # can't check sub-keys without the make
    known_engines = (make_entry.get("engines") or {})
    for e in tax.get("engines") or []:
        if e not in known_engines:
            errors.append(
                f"taxonomy.engines '{e}' is not under makes.{mk}.engines in taxonomy.yml."
            )
    known_models = (make_entry.get("models") or {})
    for mdl in tax.get("models") or []:
        if mdl not in known_models:
            errors.append(
                f"taxonomy.models '{mdl}' is not under makes.{mk}.models in taxonomy.yml."
            )
    # chassis is advisory: check each declared chassis is listed under one of the manifest's
    # models in taxonomy.yml (only when the model resolved).
    declared_chassis = [c for c in (tax.get("chassis") or [])]
    if declared_chassis:
        registered_chassis = {
            code
            for mdl in tax.get("models") or []
            for code in (known_models.get(mdl, {}) or {}).get("chassis", []) or []
        }
        for code in declared_chassis:
            if code not in registered_chassis:
                errors.append(
                    f"taxonomy.chassis '{code}' is not registered under makes.{mk}."
                    f"models.*.chassis in taxonomy.yml."
                )
    return errors


def wiki_dir(mdir: Path) -> Path:
    d = mdir / "wiki"
    d.mkdir(exist_ok=True)
    return d
