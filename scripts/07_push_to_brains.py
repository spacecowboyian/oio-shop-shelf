#!/usr/bin/env python3
"""07 — OPTIONAL, DISABLED BY DEFAULT — mirror a manual's wiki into a Brains instance.

This is a deliberate stub. The repo is the source of truth; a Brains mirror is an
optional one-way adapter, and the larger "Brains-skill lobe" idea is an open research
question (see the project's open-loop note). Do not build this out beyond a stub until
that open loop has an answer.

Usage (once implemented):
    python scripts/07_push_to_brains.py <manuals/slug/> --confirm

Without --confirm it does nothing but explain itself.
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manual_dir")
    ap.add_argument("--confirm", action="store_true")
    args = ap.parse_args()

    if not args.confirm:
        print(__doc__)
        print("Disabled. This adapter is intentionally not implemented yet.")
        return 0

    sys.exit(
        "07_push_to_brains.py is a stub. Implementing the Brains mirror is blocked on the "
        "'Brains-skill lobe' open loop — resolve that design question first."
    )


if __name__ == "__main__":
    raise SystemExit(main())
