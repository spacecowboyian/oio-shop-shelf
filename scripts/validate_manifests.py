#!/usr/bin/env python3
"""Validate every manuals/*/manifest.yml against the schema. Used by CI.

Usage:
    python scripts/validate_manifests.py

Exits non-zero if any manifest is invalid. Skips manuals/_template/.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import validate_manifest  # noqa: E402

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: PyYAML. Run: pip install -r scripts/requirements.txt")


def main() -> int:
    root = Path(__file__).resolve().parent.parent / "manuals"
    manifests = [p for p in root.glob("*/manifest.yml") if p.parent.name != "_template"]
    if not manifests:
        print("No manuals to validate (only _template present). OK.")
        return 0

    failed = False
    for mf in sorted(manifests):
        try:
            data = yaml.safe_load(mf.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            print(f"[{mf.parent.name}] YAML parse error: {e}", file=sys.stderr)
            failed = True
            continue
        errors = validate_manifest(data)
        if errors:
            failed = True
            print(f"[{mf.parent.name}] INVALID:", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
        else:
            print(f"[{mf.parent.name}] manifest OK")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
