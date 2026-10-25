import unittest
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from composite import UnresolvedSourceConflict, applicable, resolve
from build_manual_index import harvest_file
SPEC_RE = __import__("05_build_indexes").SPEC_RE
from validate_composite_map import validate


class CompositeRulesTest(unittest.TestCase):
    def test_quick_reference_preserves_printed_fractions(self):
        found = [(m.group("val"), m.group("unit")) for m in
                 SPEC_RE.finditer("33½° and 3⁄32″ and ⅛″–⅜″")]
        self.assertEqual(found, [("33½", "°"), ("3⁄32", "″"),
                                 ("⅛", "″"), ("⅜", "″")])

    def test_committed_corvair_index_contains_only_1963_passenger_rows(self):
        index = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                 "corvair-1963/data/manual-index.jsonl")
        rows = [json.loads(line) for line in index.read_text().splitlines()]
        self.assertTrue(rows)
        self.assertTrue(all(1963 in row["_applicable_years"] and
                            row["_scope"] == "passenger" for row in rows))
        self.assertFalse(any("[PDF p." in row.get("text", "") for row in rows))
        quick = index.parent.parent / "wiki/09-quick-reference.md"
        self.assertNotIn('&lt;a id="p', quick.read_text())
        self.assertFalse(any("steering arm to steering knuckle" in
                             row.get("text", "").lower() for row in rows))

    def test_page_marker_is_not_harvested_as_a_specification(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "spec.md"
            path.write_text('# Specs\n<a id="p533"></a> **[PDF p.533](../p0533.png)** '
                            '<!-- SOURCE id=supplement page=1-2 years=1963 scope=passenger -->\n'
                            'Pressure: 26 psi\n')
            rows = harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                       "sources": [{"id": "supplement"}]})
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["text"], "Pressure: 26 psi")

    def test_fractional_prose_spec_keeps_source(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "height.md"
            path.write_text('# Height\n<a id="p153"></a> '
                            '<!-- SOURCE id=base page=3-8 years=1961,1962,1963 scope=passenger -->\n'
                            'Ride height is 9⅜″ ± ½″.\n')
            rows = harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                       "sources": [{"id": "base"}]})
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["text"], "Ride height is 9⅜″ ± ½″.")
            self.assertEqual(rows[0]["_original_page"], "3-8")

    def test_inch_pound_torque_is_searchable(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "bearings.md"
            path.write_text('# Bearings\n<a id="p640"></a> '
                            '<!-- SOURCE id=supplement page=3-1 years=1963 scope=passenger -->\n'
                            'Tighten the adjusting nut to 100 in. lb. while turning the wheel.\n')
            rows = harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                       "sources": [{"id": "supplement"}]})
            self.assertEqual(len(rows), 1)
            self.assertIn("100 in. lb.", rows[0]["text"])

    def test_committed_composite_covers_every_source_page_once(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        self.assertEqual(validate(manual), [])

    def test_1962_only_value_cannot_answer_1963_query(self):
        old = {"id": "old", "value": "1962 value", "years": [1962], "scope": "passenger"}
        self.assertIsNone(resolve([old], 1963, "passenger"))

    def test_supplement_supersedes_applicable_base(self):
        base = {"id": "base", "value": "base value", "years": [1961, 1962, 1963],
                "scope": "passenger", "priority": 0}
        update = {"id": "update", "value": "1963 value", "years": [1963],
                  "scope": "passenger", "priority": 1, "supersedes": ["base"]}
        self.assertEqual(resolve([base, update], 1963, "passenger"), update)

    def test_1963_column_precedes_shared_1962_63_column(self):
        shared = {"id": "shared", "value": "shared", "years": [1962, 1963],
                  "scope": "passenger", "priority": 2}
        specific = {"id": "specific", "value": "1963", "years": [1963],
                    "scope": "passenger", "priority": 2}
        self.assertEqual(resolve([shared, specific], 1963, "passenger"), specific)

    def test_fc_does_not_apply_to_passenger(self):
        self.assertFalse(applicable({"years": [1963], "scope": "commercial"}, 1963, "passenger"))

    def test_unresolved_same_priority_conflict_fails(self):
        a = {"id": "a", "value": "10", "years": [1963], "scope": "passenger"}
        b = {"id": "b", "value": "11", "years": [1963], "scope": "passenger"}
        with self.assertRaises(UnresolvedSourceConflict):
            resolve([a, b], 1963, "passenger")

    def test_higher_priority_does_not_hide_unresolved_conflict(self):
        a = {"id": "a", "value": "10", "years": [1963], "scope": "passenger", "priority": 1}
        b = {"id": "b", "value": "11", "years": [1963], "scope": "passenger", "priority": 2}
        with self.assertRaises(UnresolvedSourceConflict):
            resolve([a, b], 1963, "passenger")

    def test_unknown_year_is_not_applicable(self):
        self.assertFalse(applicable({"scope": "passenger"}, 1963, "passenger"))

    def test_index_drops_1962_only_row_and_keeps_provenance(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "spec.md"
            path.write_text("# Specs\n<!-- SOURCE id=supplement page=12-1 years=1962 scope=passenger -->\n"
                            "**[PDF p.1]**\n| Item | Value |\n|---|---|\n| Gap | 10 psi |\n"
                            "<!-- SOURCE id=supplement page=12-2 years=1963 scope=passenger -->\n"
                            "**[PDF p.2]**\n| Item | Value |\n|---|---|\n| Gap | 12 psi |\n")
            rows = harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                       "sources": [{"id": "supplement"}]})
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["value"], "12 psi")
            self.assertEqual(rows[0]["_original_page"], "12-2")

    def test_index_rejects_untagged_composite_spec(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "spec.md"
            path.write_text("# Specs\n| Item | Value |\n|---|---|\n| Gap | 10 psi |\n")
            with self.assertRaises(ValueError):
                harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                    "sources": [{"id": "supplement"}]})


if __name__ == "__main__":
    unittest.main()
