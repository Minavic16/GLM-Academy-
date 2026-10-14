# Phase 13.7 Final Report — Owner Decisions and Subject Closure Gates

Baseline `2190cf6` (117 pass, `[]`) → final `1e129d6` (**119 pass**, `[]`).

## Disposition
All five owner decisions documented with evidence and recommendations;
NONE resolved on the owner's behalf. No Biology work, no schema/relation
changes, no promotions.

## OD-01 Standard v1.0 → v1.1 (still PROPOSED)
Reviewed against 12 required dimensions; two editorial additions
(approval-authority clause; provenance/legacy-id clause) — no policy change.
Approve / amend / reject remains with owner.

## OD-02 12-vs-13 (evidence CONFIRMED, ratification pending)
Chain: brief froze 13 incl. Subject; sanity §11 says 12, §12 calls
EvidenceRule "a thirteenth entity" ⇒ its 12 excludes Subject. Test
`test_entity_type_count_frozen` locks the implemented 13. Docs corrected;
no type added/removed.

## OD-03 `indicates` (unchanged, conforms)
Semantics/differences documented; sole claim stays PROPOSED; no broadening.

## OD-04 Qualified-scope (recommendation: Option 3 — separate dimensions)
Implementation-completeness vs board-verification tracked separately; the
CDG's `Claim.status` already isolates lifecycle, so verification is recorded
in `CLOSURE_REGISTERS.md` (no schema change). Strict closure judged
unsatisfiable under current network conditions.

## OD-05 Biology (BLOCKED)
Blocked by OD-01 (no gate exists) + missing explicit authorization; request
recorded.

## Subject statuses recorded (Option-3 vocabulary)
- Mathematics: IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED — 13.6 verified
  intact (median legacy id, dispersion legacy ids, quartile PARTIAL row,
  log→pH edge).
- Physics: PARTIAL / BOARD_UNVERIFIED — 19 KCs preserved; fibre/LASER/
  electronics deferrals visible.
- Chemistry: PARTIAL / BOARD_UNVERIFIED — 12 KCs preserved; polymers/
  industrial/transition deferrals visible.

## Official-source attempts (2026-10-14)
IBASS 200 (SPA, hashed assets), WAEC 200 (no syllabus links), NERDC
unreachable → OFFICIAL_VERIFICATION_GAP open for all three subjects.

## Repro
python3 -m pytest -q; python3 tools/generate_math_cdg_docs.py;
python3 tools/generate_cdg_visualization.py (byte-identical);
run_store_validation(build_graph_v36()) == [].

## Next action
Owner decisions OD-01–OD-05; then Biology may be gated, not started.
