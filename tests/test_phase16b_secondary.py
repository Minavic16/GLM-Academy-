"""Phase 16B regression tests for secondary-syllabus comparison artifacts.

Phase 16B changes documentation only (no canonical-store changes). These tests guard
that the six Syllabus NG coverage matrices, the consolidated comparison, and the
deduplicated gap register exist with the required structure and vocabulary, and that
the canonical store and protected records remain unchanged.
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ARCH = ROOT / "docs" / "architecture"

MATRIX_FILES = {
    "JAMB Mathematics": ARCH / "JAMB_MATHEMATICS_SECONDARY_COVERAGE.md",
    "JAMB Physics": ARCH / "JAMB_PHYSICS_SECONDARY_COVERAGE.md",
    "JAMB Chemistry": ARCH / "JAMB_CHEMISTRY_SECONDARY_COVERAGE.md",
    "WAEC Mathematics": ARCH / "WAEC_MATHEMATICS_SECONDARY_COVERAGE.md",
    "WAEC Physics": ARCH / "WAEC_PHYSICS_SECONDARY_COVERAGE.md",
    "WAEC Chemistry": ARCH / "WAEC_CHEMISTRY_SECONDARY_COVERAGE.md",
}

OTHER_FILES = {
    "consolidated comparison": ARCH / "CONSOLIDATED_NERDC_JAMB_WAEC_COMPARISON.md",
    "deduplicated gap register": ARCH / "DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md",
    "retrieval report": ARCH / "PHASE16_RETRIEVAL_REPORT.md",
    "16B report": ROOT / "docs" / "PHASE16B_REPORT.md",
}

REQUIRED_MATRIX_COLUMNS = (
    "authority_claimed_by_source",
    "source_type",
    "subject",
    "displayed_syllabus_year",
    "source_url",
    "topic",
    "subtopic_or_objective",
    "cdg_entity_ids",
    "coverage_status",
    "evidence_reference",
    "gap_description",
    "recommended_action",
    "official_verification_status",
)

ALLOWED_STATUSES = {
    "COVERED", "PARTIALLY_COVERED", "NOT_COVERED", "NOT_APPLICABLE", "UNRESOLVED",
}


def _table_rows(path: Path) -> list[list[str]]:
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


@pytest.mark.phase16b
def test_phase16b_six_matrices_exist():
    for label, path in MATRIX_FILES.items():
        assert path.is_file(), f"missing matrix: {label}"


@pytest.mark.phase16b
def test_phase16b_other_deliverables_exist():
    for label, path in OTHER_FILES.items():
        assert path.is_file(), f"missing deliverable: {label}"


@pytest.mark.phase16b
@pytest.mark.parametrize("label,path", list(MATRIX_FILES.items()))
def test_phase16b_matrix_structure(label, path):
    rows = _table_rows(path)
    assert rows, label
    assert rows[0] == list(REQUIRED_MATRIX_COLUMNS), (label, rows[0])
    for row in rows[1:]:
        assert len(row) == len(REQUIRED_MATRIX_COLUMNS), (label, row)
        assert row[1].upper() == "SECONDARY", (label, row, "source_type not SECONDARY")
        assert row[2], (label, row, "subject empty")
        assert row[5], (label, row, "topic empty")
        assert row[8] in ALLOWED_STATUSES, (label, row, "coverage_status invalid")
        assert row[9], (label, row, "evidence_reference empty")
        assert row[12].upper() == "BOARD_UNVERIFIED", (
            label, row, "secondary matrix must not promote BOARD_VERIFIED")


@pytest.mark.phase16b
def test_phase16b_secondary_only_labels():
    """No matrix row may claim anything other than SECONDARY source type."""
    for label, path in MATRIX_FILES.items():
        for row in _table_rows(path)[1:]:
            assert row[1].upper() == "SECONDARY", (label, row)


@pytest.mark.phase16b
def test_phase16b_store_and_protected_records_unchanged():
    """Phase 16B changes documentation only; the graph store is unchanged."""
    from examples.chemistry_organic_reactions import build_graph_v39
    from cdg.enums import EntityType
    from cdg.validation import run_store_validation

    assert run_store_validation(build_graph_v39()) == []
    s = build_graph_v39()
    kc_counts = {}
    for subj in ("Mathematics", "Physics", "Chemistry", "Biology", "English"):
        kc_counts[subj] = sum(
            1 for e in s.entities.values()
            if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == subj)
    assert kc_counts == {"Mathematics": 39, "Physics": 25, "Chemistry": 21,
                         "Biology": 0, "English": 0}
    # the proposed indicates claim stays PROPOSED
    from cdg.enums import ClaimStatus, RelationshipType
    inds = [c for c in s.claims.values()
            if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED
