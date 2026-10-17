"""Phase 16 regression tests for the official-source verification artifacts.

Phase 16 changes documentation only (no canonical-store changes). These tests
guard that the retrieval report, source metadata, coverage matrices, and gap
register exist with the required structure and vocabulary.
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ARCH = DOCS / "architecture"
SRC_DOCS = DOCS / "source-documents"

REQUIRED_MATRIX_HEADER = (
    "authority", "subject", "document_version", "official_topic",
    "official_subtopic_or_objective", "cdg_entity_ids", "coverage_status",
    "evidence_reference", "gap_description", "next_action",
)

ALLOWED_STATUSES = {
    "COVERED", "PARTIALLY_COVERED", "NOT_COVERED",
    "NOT_APPLICABLE", "UNRESOLVED",
}

MATRIX_FILES = {
    "Mathematics": ARCH / "MATHEMATICS_SYLLABUS_COVERAGE.md",
    "Physics": ARCH / "PHYSICS_SYLLABUS_COVERAGE.md",
    "Chemistry": ARCH / "CHEMISTRY_SYLLABUS_COVERAGE.md",
}


def _table_rows(path: Path) -> list[list[str]]:
    text = path.read_text()
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows


@pytest.mark.phase16
def test_phase16_retrieval_report_exists():
    report = ARCH / "PHASE16_RETRIEVAL_REPORT.md"
    assert report.is_file()
    text = report.read_text()
    for token in ("a2f618", "e0f9b0", "fc0648", "f79d3f", "88dd5d",
                  "ibass.jamb.gov.ng", "waecnigeria.org", "nerdc.gov.ng",
                  "lmis.nerdcportals.com.ng"):
        assert token in text, token


@pytest.mark.phase16
def test_phase16_source_metadata_files():
    expected = [
        "SRC.NERDC.SSEC.MATH.SS1.json", "SRC.NERDC.SSEC.MATH.SS2.json",
        "SRC.NERDC.SSEC.CHEM.SS1.json", "SRC.NERDC.SSEC.CHEM.SS2.json",
        "SRC.NERDC.SSEC.PHY.SS1.json", "SRC.NERDC.SSEC.PHY.SS2.json",
        "SRC.JAMB.IBASS.ATTEMPT.2026-10-17.json",
        "SRC.WAEC.ATTEMPT.2026-10-17.json",
        "SRC.NERDC.PORTAL.ATTEMPT.2026-10-17.json",
        "SRC.FEDMOE.CURRICULUM.OFFERINGS.2025.json",
    ]
    for name in expected:
        p = SRC_DOCS / name
        assert p.is_file(), name
        import json
        meta = json.loads(p.read_text())
        for key in ("id", "organization", "title", "subject", "type",
                    "authority", "canonical_url", "retrieved_at",
                    "bytes_retrieved", "content_extracted",
                    "authenticity_established", "limitations", "notes"):
            assert key in meta, (name, key)


@pytest.mark.phase16
@pytest.mark.parametrize("subject,path", list(MATRIX_FILES.items()))
def test_phase16_coverage_matrix_structure(subject, path):
    assert path.is_file(), subject
    rows = _table_rows(path)
    assert rows, subject
    assert rows[0] == list(REQUIRED_MATRIX_HEADER), (subject, rows[0])
    for row in rows[1:]:
        assert len(row) == len(REQUIRED_MATRIX_HEADER), (subject, row)
        status = row[6]
        assert status in ALLOWED_STATUSES, (subject, status)
        # every cited cdg entity id, if present, must be non-empty text
        assert row[5].strip(), (subject, row, "cdg_entity_ids empty")


@pytest.mark.phase16
def test_phase16_gap_register_exists():
    register = ARCH / "CROSS_SUBJECT_GAP_REGISTER.md"
    assert register.is_file()
    text = register.read_text()
    for token in ("CI-11", "CI-12", "CI-16", "CI-17", "CI-20", "CI-24",
                  "BOARD_VERIFIED", "IMPLEMENTATION_PARTIAL"):
        assert token in text, token


@pytest.mark.phase16
def test_phase16_no_store_changes():
    """Phase 16 changes documentation only; the graph store is unchanged."""
    from examples.chemistry_organic_reactions import build_graph_v39
    from cdg.validation import run_store_validation
    assert run_store_validation(build_graph_v39()) == []
