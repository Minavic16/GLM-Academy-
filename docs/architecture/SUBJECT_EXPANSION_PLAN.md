# Subject Expansion Plan (five-subject roadmap)

Status labels used below reflect repository evidence as of 2026-10-08:
COMPLETE = implemented + validated + tested. NEXT/PLANNED = not started.

| Phase | Subject or workstream | Intended scope | Status |
|---|---|---|---|
| 11 | Architecture and visualization foundation | Multi-subject contracts, cross-subject policy, visualization layer | COMPLETE |
| 12 | Physics | Source-backed initial vertical slice (measurement, kinematics, Newton) + first Math→Physics edges | COMPLETE (this repo state) |
| 13 | Chemistry | Research + initial subject graph (matter, mole/stoichiometry slice) | PLANNED |
| 14 | Biology | Research + initial subject graph | PLANNED |
| 15 | English Language | Research + initial subject graph (exam-paper structure differs) | PLANNED |
| 16 | Cross-subject integration | Evidence-backed links, whole-curriculum audits, integration QA | PLANNED |

Mathematics remains the reference implementation and is not counted as a new expansion phase.

Principle: internal subject coherence first; cross-subject edges added only
where a target TaskModel/Method requires the source KC (Phase 12 proved the
pattern with four Mathematics → Physics DERIVED prerequisites).

## Phase 11 — COMPLETE
Research prerequisites: none (baseline). Source families: Mathematics legacy
corpus + OpenStax references. Artifacts: contracts, policy, audit, generator.
Validation: 82 tests green. Exit: architecture + visualization demonstrated.

## Phase 12 — COMPLETE
- Research prerequisites: official Physics portals located; OpenStax UP1 pages fetched (HTTP 200).
- Source families: JAMB/IBASS + WAEC + NERDC (registered, PDFs pending) + OpenStax UP1 (inspected).
- Scope boundary: measurement, kinematics, Newton's laws only.
- Required artifacts: `examples/physics_slice.py`, 8 Physics KCs, 4 TMs, 6 Methods,
  4 Math→Physics DERIVED prerequisites, `docs/research/PHYSICS_SOURCE_RESEARCH.md`,
  updated scope/audit/readiness docs, regenerated visualizations.
- Validation: store validation `[]`, full pytest green, visualization deterministic + two-subject QA.
- Dependencies: Phase 11 contracts.
- Exit criteria: slice validated, 4 cross-subject edges accepted via human review, docs regenerated.
- Owner decisions NOT made: freeze-doc content, `indicates` sign-off, 12-vs-13 count.

## Phase 13 — Chemistry (PLANNED)
- Research prerequisites: JAMB/IBASS + WAEC + NERDC Chemistry documents (same retrieval pattern as Phase 12).
- Source families: official syllabi + OpenStax Chemistry 2e (expected).
- Scope boundary: matter/atomic basics + mole/stoichiometry slice only.
- Required artifacts: chemistry slice module, batch record, scope update, audit update, regenerated docs/viz.
- Validation: same gate as Phase 12 (store `[]`, pytest green, determinism).
- Dependencies: Phase 12 pattern; Math ratio/proportion KC already exists for stoichiometry edges.
- Exit criteria: validated slice + first Math→Chemistry edge(s) or documented deferral.
- Owner decisions: same standing items; no new relation types.

## Phase 14 — Biology (PLANNED)
Same structure; scope boundary TBD from NERDC/WAEC/JAMB Biology documents.
Note practical/fieldwork emphasis expected — follow the Physics-practical precedent (PROPOSED KC first).

## Phase 15 — English Language (PLANNED)
Same structure; note examination structure differs (WAEC Papers 1–4, JAMB Use-of-English).
Do not model grammar trees; language capabilities as KCs, comprehension tasks as TaskModels.

## Phase 16 — Cross-subject integration (PLANNED)
Evidence-backed link audit across all five subjects, whole-curriculum audits,
integration QA. No bulk edge creation.

## Governance checkpoints before each phase
- FREEZE doc reconciliation if it appears.
- `indicates` owner decision.
- 12-vs-13 entity count decision.
- No new relationship types without documented necessity + owner approval.
