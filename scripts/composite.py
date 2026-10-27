"""Applicability and supersession rules for manuals made from factory sources.

Selection fails closed: an unstated year or unresolved conflict yields no fact.
Single-source manuals do not need to use this module.
"""
from __future__ import annotations

import re


SOURCE_COMMENT_RE = re.compile(r"<!--\s*SOURCE\b(.*?)-->", re.DOTALL)


def parse_source_marker(line: str) -> tuple[str, str, list[int], str | None, str | None] | None:
    """Read source provenance, including annotations on excluded pages.

    A missing year or scope makes the page inapplicable to a target lookup.
    Additional annotations (for example applicability or excluded) may follow
    the core fields without preventing the marker from resetting provenance.
    """
    match = SOURCE_COMMENT_RE.search(line)
    if not match:
        return None
    body = match.group(1)

    def field(name: str) -> str | None:
        found = re.search(rf"\b{name}=([^\s;]+)", body)
        return found.group(1) if found else None

    source_id, page = field("id"), field("page")
    if not source_id or not page:
        raise ValueError(f"Malformed SOURCE marker: {line}")
    year_text = field("years")
    years = [int(y) for y in year_text.split(",")] if year_text else []
    return source_id, page, years, field("scope"), field("variant")


class UnresolvedSourceConflict(ValueError):
    pass


def applicable(item: dict, year: int, scope: str, options: set[str] | None = None) -> bool:
    """Whether an explicitly tagged procedure or value covers this vehicle."""
    years = item.get("years")
    if not isinstance(years, list) or year not in years:
        return False
    if item.get("scope") not in (scope, "all"):
        return False
    required = set(item.get("options") or [])
    return required <= (options or set())


def resolve(candidates: list[dict], year: int, scope: str,
            options: set[str] | None = None) -> dict | None:
    """Select one fact by explicit applicability and supersession.

    Candidates for the same subject and option context have `id`, `value`, `source_id`,
    `years`, `scope`, `priority`, and optionally `supersedes` (list of candidate IDs).
    Differing equally specific values are conflicts even when priorities differ;
    priority selects the source to cite only when values agree.
    """
    pool = [x for x in candidates if applicable(x, year, scope, options)]
    removed = {sid for x in pool for sid in x.get("supersedes", [])}
    pool = [x for x in pool if x.get("id") not in removed]
    if not pool:
        return None
    most_specific = min(len(x["years"]) for x in pool)
    winners = [x for x in pool if len(x["years"]) == most_specific]
    if len({str(x.get("value")) for x in winners}) > 1:
        raise UnresolvedSourceConflict(f"Conflicting applicable values: {[x.get('id') for x in winners]}")
    return max(winners, key=lambda x: x.get("priority", 0))
