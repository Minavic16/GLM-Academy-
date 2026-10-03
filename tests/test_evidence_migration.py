from conftest import *


def test_evidence_immutable_and_typed():
    ev = EvidenceItem(
        id="ev1", claim_id="cl.pr", source_id="src.jamb", role=EvidenceRole.DIRECT,
        stance=EvidenceStance.SUPPORTS, locator="Section 4.3", excerpt="place value …",
        excerpt_kind=ExcerptKind.VERBATIM, extracted_by_activity="act.extract",
    )
    assert ev.stance == EvidenceStance.SUPPORTS
    # frozen dataclass enforces immutability
    try:
        ev.stance = EvidenceStance.CONTRADICTS  # type: ignore
        assert False, "EvidenceItem must be immutable"
    except Exception:
        pass


def test_migration_record_keeps_legacy_identity():
    m = MigrationRecord(
        id="mig.1", legacy_ids=["EDGE.MATH.000001"], disposition=MigrationDisposition.MAPPED,
        migration_activity_id="act.mig", mapping_rule="prerequisite_of -> prerequisite(scope=ALL_RELEVANT_METHODS, purpose=UNDERSTAND)",
        target_cdg_version="v0.2.0", new_record_ids=["cl.pr"],
    )
    assert m.legacy_ids == ["EDGE.MATH.000001"]
    assert validate_migration_record(m) == []


def test_migration_record_requires_legacy_id_and_activity():
    m = MigrationRecord(
        id="mig.2", legacy_ids=[], disposition=MigrationDisposition.MAPPED,
        migration_activity_id="", mapping_rule="x", target_cdg_version="",
    )
    errs = validate_migration_record(m)
    assert any("legacy_id" in e for e in errs)
    assert any("MIGRATION Activity" in e for e in errs)


def test_store_json_round_trip_serializable():
    s = make_store()
    s.add_claim(Claim(id="cl.req1", predicate=RelationshipType.REQUIRES, subject_id="m.1",
                      object_id="kc.place_value", claim_type=ClaimType.DEPENDENCY,
                      created_by_activity="act.extract", qualifiers={"origin": "DERIVED"}))
    blob = dumps_store(s)
    assert '"kg.req1"' in blob or '"cl.req1"' in blob
    import json
    parsed = json.loads(blob)
    assert len(parsed["entities"]) > 0
    assert len(parsed["claims"]) == 1
