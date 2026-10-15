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

## PHYSICS — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED
Counts: 19 KCs; 4 Math→Physics edges + further Science edges.
Verified partial/deferred:
- Fibre optics / LASER / elementary electronics — NOT_IMPLEMENTED
  (SHOULD-deferral; matrix R17).
- Friction/machines, EM spectrum depth, energy-society — PARTIAL via parent
  KCs (R06/R18/R19).
- Practicals — PARTIAL; WAEC practical detail SOURCE_UNVERIFIED (R16).
Next task: Physics SHOULD-row triage → implement fibre/LASER/electronics
slice (2 batches: 059 fibre-optics+optics-extension; 060 electronics basics)
with OpenStax UP2/UP3 evidence + review. Completion criterion: R17 COVERED,
R16 PARTIAL→COVERED on WAEC evidence, board rows verified.

## CHEMISTRY — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED
Counts: 12 KCs; pH dependency resolved (log→ph).
Verified partial/deferred:
- Organic: naming/classification only — reactions NOT_IMPLEMENTED.
- Practical: PARTIAL (WAEC detail unverified).
- Buffers proper, polymers, industrial chemistry, transition metals —
  NOT_IMPLEMENTED (deferred, documented in CHEMISTRY_COVERAGE_MATRIX).
Next task: organic-reactions batch (alkene/alkane reactions + functional
group basics) using OpenStax Chemistry 2e ch.20 evidence + review.
Completion criterion: organic family PARTIAL→COVERED, then buffers with
kc.logarithms prerequisite (already built).

## Recommended next phase
Phase 14a: Physics completion wave (fibre/LASER/electronics + practical
confirmation) — highest dependency-centrality after Math closure;
then Chemistry organic reactions. Biology remains on hold (BIOLOGY_HOLD_RECORD).
