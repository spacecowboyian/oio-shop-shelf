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

    def test_quick_reference_harvests_factory_torque_units(self):
        found = [(m.group("val"), m.group("unit")) for m in
                 SPEC_RE.finditer("100 in. lb.; 38–50 ft. lb.")]
        self.assertEqual(found, [("100", "in. lb."), ("38–50", "ft. lb.")])

    def test_quick_reference_harvests_service_intervals_and_balance(self):
        found = [(m.group("val"), m.group("unit")) for m in
                 SPEC_RE.finditer("4,000–5,000 miles; 11 inch-ounces")]
        self.assertEqual(found, [("4,000–5,000", "miles"),
                                 ("11", "inch-ounces")])

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
        self.assertFalse(any(row.get("assembly") == "Rear lower control arm" and
                             row.get("fastener") == "Cross shaft to crossmember"
                             for row in rows))
        self.assertFalse(any(row.get("_page") in
                             {*(f"p{n}" for n in range(174, 181)), "p642", "p644"}
                             for row in rows))

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

    def test_completed_suspension_covers_passenger_source_pages(self):
        chapter = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                   "corvair-1963/wiki/03-suspension.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE -->", chapter)
        for n in (*range(146, 174), 181, 182, 183, 640, 641, 643):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        for n in (*range(174, 181), 642, 644):
            self.assertNotIn(f'<a id="p{n}"></a>', chapter)

    def test_completed_steering_covers_passenger_pages_and_indexes_1963_adjustment(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/04-steering.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE -->", chapter)
        for n in (*range(184, 197), 208, 209, 645, 646, 647):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        for n in (*range(197, 208), 648):
            self.assertNotIn(f'<a id="p{n}"></a>', chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        steering = [r for r in rows if r["_file"] == "wiki/04-steering.md"]
        self.assertTrue(any(r.get("steering-gear-adjustment-passenger-car") ==
                            "Worm-bearing preload" and r.get("_page") == "p646"
                            for r in steering))
        self.assertFalse(any("20°" in r.get("text", "") or "18°" in
                             r.get("text", "") or "33½°" in r.get("text", "")
                             for r in steering))
        self.assertFalse(any("steering-arm" in r.get("text", "").lower() and
                             "40–50" in r.get("text", "") for r in steering))

    def test_1963_brake_index_uses_self_adjuster_and_excludes_old_shoe_setting(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/05-brakes.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE -->", chapter)
        for n in (*range(211, 218), *range(220, 224), 230, 231,
                  *range(649, 657)):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        for n in (*range(224, 230), 657):
            self.assertNotIn(f'<a id="p{n}"></a>', chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        brakes = [r for r in rows if r["_file"] == "wiki/05-brakes.md"]
        self.assertTrue(any(r.get("initial-1963-shoe-setting-drum-used-as-gauge") ==
                            "Retract after slight drum drag" and
                            r.get("factory-value") == "1¼ star-wheel turns"
                            for r in brakes))
        self.assertFalse(any("12 notches" in r.get("text", "") or
                             "15 notches" in r.get("text", "") for r in brakes))

    def test_1963_engine_index_preserves_spyder_and_revised_blower_height(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        engine = [r for r in rows if r["_file"] == "wiki/06a-engine.md"]
        self.assertTrue(any(r.get("compression-ratio") == "8:1" and
                            r.get("_variant") == "spyder" and
                            r.get("_original_page") == "6A-9" for r in engine))
        self.assertTrue(any("4.475 ± .015 in." in r.get("factory-value", "")
                            for r in engine))
        self.assertFalse(any("4.520" in json.dumps(r) or "4.530" in json.dumps(r)
                             for r in engine))

    def test_completed_engine_uses_supplement_oil_pan_torque_and_omits_commercial_pages(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/06a-engine.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE", chapter)
        for n in (*range(247, 300), *range(303, 307), *range(659, 668)):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        for n in range(300, 303):
            self.assertNotIn(f'<a id="p{n}"></a>', chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        engine = [r for r in rows if r["_file"] == "wiki/06a-engine.md"]
        self.assertTrue(any(r.get("1963-oil-pan-attachment") == "¼-20 bolts" and
                            r.get("torque") == "40–60 in. lb." and
                            r.get("_page") == "p629" and
                            r.get("_source_id") == "supplement-1962-63" and
                            r.get("_original_page") == "12-6" for r in engine))
        self.assertFalse(any("40–60 ft-lb" in json.dumps(r) for r in engine))

    def test_1963_clutch_omits_commercial_linkage_and_old_pedal_spring(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/06b-clutch.md").read_text()
        for n in (*range(307, 313), 317, 318, 668, 630):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        for n in (*range(313, 317), 319, 320):
            self.assertNotIn(f'<a id="p{n}"></a>', chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        clutch = [r for r in rows if r["_file"] == "wiki/06b-clutch.md"]
        self.assertTrue(any(r.get("1963-passenger-clutch-application") ==
                            "RPO 649/651 high performance, including Spyder" and
                            r.get("disc-diameter") == "8 in." and
                            r.get("_original_page") == "12-7" for r in clutch))
        self.assertFalse(any(r.get("_page") in
                             {*(f"p{n}" for n in range(313, 317)), "p319", "p320"}
                             for r in clutch))

    def test_1963_rear_axle_uses_1963_capacity_and_nominal_14_chart(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/06c-rear-axle.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE", chapter)
        for n in (*range(321, 346), *range(669, 676), 630):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        self.assertNotIn('<a id="p346"></a>', chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        axle = [r for r in rows if r["_file"] == "wiki/06c-rear-axle.md"]
        self.assertTrue(any(r.get("lubricant-capacity") == "4½ pints" and
                            r.get("_page") == "p630" and
                            r.get("_original_page") == "12-7" for r in axle))
        self.assertTrue(any(r.get("nominal-14-chart-indication") == "15+6"
                            for r in axle))
        self.assertFalse(any("3 pints" in json.dumps(r) for r in axle))

    def test_1963_manual_transmission_uses_passenger_linkage(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/06d-manual-transmission.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE", chapter)
        for n in (*range(347, 375), 676, 677):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        self.assertIn("scope=commercial; excluded=passenger", chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        transmission = [r for r in rows if r["_file"] == "wiki/06d-manual-transmission.md"]
        self.assertTrue(any(r.get("1963-four-speed-passenger-linkage") == "900" and
                            r.get("lever-setting") ==
                            "Knob center 3¼ in. rearward of housing center" and
                            r.get("_original_page") == "6D-2" for r in transmission))
        self.assertFalse(any(r.get("_page") == "p373" for r in transmission))

    def test_1963_powerglide_keeps_base_pressures_and_supplement_planet_service(self):
        manual = (Path(__file__).resolve().parent.parent / "manuals/chevrolet/vehicle/"
                  "corvair-1963")
        chapter = (manual / "wiki/06e-automatic-transmission.md").read_text()
        self.assertNotIn("<!-- INCOMPLETE", chapter)
        for n in (*range(375, 405), 678, 679, 680):
            self.assertIn(f'<a id="p{n}"></a>', chapter)
        self.assertIn("scope=commercial; excluded=passenger", chapter)
        self.assertIn("front-pump body and transmission case", chapter)
        rows = [json.loads(line) for line in
                (manual / "data/manual-index.jsonl").read_text().splitlines()]
        powerglide = [r for r in rows if r["_file"] == "wiki/06e-automatic-transmission.md"]
        self.assertTrue(any(r.get("_page") == "p400" and
                            r.get("_original_page") == "6E-26" and
                            r.get("reverse") == "81–98" for r in powerglide))
        self.assertTrue(any(r.get("_page") == "p126" and
                            r.get("_original_page") == "12-10" and
                            r.get("factory-value") == "1.82:1" for r in powerglide))
        self.assertFalse(any(r.get("_page") == "p402" for r in powerglide))

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

    def test_composite_index_preserves_variant_applicability(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "engine.md"
            path.write_text("# Engine\n<a id=\"p667\"></a> "
                            "<!-- SOURCE id=supplement page=6A-9 years=1963 "
                            "scope=passenger variant=spyder -->\n"
                            "| Engine | Compression |\n|---|---|\n| Spyder | 8:1 |\n")
            rows = harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                       "sources": [{"id": "supplement"}]})
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["_variant"], "spyder")
            self.assertEqual(rows[0]["_original_page"], "6A-9")

    def test_index_rejects_untagged_composite_spec(self):
        with TemporaryDirectory() as d:
            path = Path(d) / "spec.md"
            path.write_text("# Specs\n| Item | Value |\n|---|---|\n| Gap | 10 psi |\n")
            with self.assertRaises(ValueError):
                harvest_file(path, {"target_year": 1963, "scope": "passenger",
                                    "sources": [{"id": "supplement"}]})


if __name__ == "__main__":
    unittest.main()
