"""Applicability and supersession rules for manuals made from factory sources.

Selection fails closed: an unstated year or unresolved conflict yields no fact.
Single-source manuals do not need to use this module.
"""
from __future__ import annotations


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
