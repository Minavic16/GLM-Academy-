# Phase 13.8 Roadmap — Mathematics, Physics, Chemistry

Statuses under ratified model (OD-01/OD-04):

## MATHEMATICS — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED
Completed: 39 KCs, full-chains validated, CI-01/CI-02 closed (median +
dispersion with preserved legacy ids), kc.logarithms (b055) enables
Chemistry pH; log→pH edge cl.pre56.log_ph ACCEPTED and intact.
Remaining gaps:
1. Official-board verification (M-1): retrieval + content-check of JAMB/WAEC/
   NERDC Math documents; map syllabus rows to KC coverage; promote rows to
   BOARD_VERIFIED only on checked content.
2. Scope items marked deferred (mode/mean-grouped/ogive) stay out unless
   owner extends declared scope.
Tests for closure: full suite ≥ current, store `[]`, coverage matrix rows
all COVERED-or-excluded with evidence refs.
Next task: M-1 official-source verification plan (shared infra for 3 subjects).

## PHYSICS — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED (updated 2026-10-15, Phase 14)
Phase 14 closed all seven audit targets: friction/machines (b059), EM spectrum
depth (b060), energy sources/society (b061), fibre optics (b062), lasers
(b063), electronics (b064); practical implementation acceptable with WAEC
detail still unverified. Historical section below retained for audit trail.

### PHYSICS — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED
Counts: 19 KCs; 4 Math→Physics edges + further Science edges.
Verified partial/deferred:
- Fibre optics / LASER / elementary electronics — NOT_IMPLEMENTED
  (SHOULD-deferral; matrix R17).
- Friction/machines, EM spectrum depth, energy-society — PARTIAL via parent
  KCs (R06/R18/R19).
- Practicals — PARTIAL; WAEC practical detail SOURCE_UNVERIFIED (R16).
Next task: DONE in Phase 14 — Physics is IMPLEMENTATION_COMPLETE; next is board
verification (M-1 plan) or Chemistry organic-reactions batch.

## CHEMISTRY — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED (updated 2026-10-16, Phase 15)
Counts: 21 KCs (12 foundational + 9 organic-reactions), 81 TMs.

Phase 15 closed the organic-reactions gap (the only implementation gap in
Chemistry's declared scope):
- Batch 065 (`examples/chemistry_organic_reactions.py`,
  `build_graph_v39`): kc.reactions_of_alkanes, kc.reactions_of_alkenes,
  kc.isomerism, kc.alcohols, kc.ethers, kc.aldehydes_ketones,
  kc.carboxylic_acids, kc.amines, kc.amides — each with a targeting TM,
  Methods, Items, and ACCEPTED claims. Evidence: OpenStax Chemistry 2e
  20-1–20-4 (verified). Prerequisites are Chemistry-internal; no new
  cross-subject dependency claims were created (Phase 15 restriction).
- CI-10 closed (see CLOSURE_REGISTERS.md).

Remaining gaps:
- Buffers proper — BLOCKED (Phase 15 scope constraint). Buffer pH
  calculations require the Mathematics logarithms KC, and creating
  that prerequisite edge would modify Mathematics-side records.
  Re-evaluate only with owner authorization.
- Polymers, industrial chemistry — DEFERRED (owner-documented deferral).
- Electrolytic cells detail / transition metals — DEFERRED (owner-documented
  deferral).
- Practical: implementation complete; official verification outstanding
  (CI-05). Board verification status remains BOARD_UNVERIFIED for all
  three subjects.

Next task: M-1 official-source verification plan (shared infrastructure
for JAMB/WAEC/NERDC retrieval and content-check); no further
implementation gap exists within Phase 15's authorized scope.
Biology remains on hold (BIOLOGY_HOLD_RECORD.md).
## Recommended next phase
Phase 14a/14b: Physics completion wave — DONE (implemented in Phase 14).
Phase 15: Chemistry organic-reactions wave — DONE (implemented in Phase 15).
Next: Phase 16 — official-source verification (M-1) for Mathematics,
Physics, and Chemistry; then Biology only after all three subjects are
sufficiently closed and the owner authorizes it.
Biology remains on hold (BIOLOGY_HOLD_RECORD.md).
