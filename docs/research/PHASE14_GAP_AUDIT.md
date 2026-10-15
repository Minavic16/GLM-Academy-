# Phase 14A Gap Audit — Physics

Baseline verified 2026-10-15: `58a562c`, 119 tests, `[]`, 19 ACCEPTED
Physics KCs, 4 Math→Physics DERIVED edges (batch 030) + method-scope edges
from batches 031–042 (all preserved).

| # | Target | Existing records | Verdict | Deficiency | Class |
|---|---|---|---|---|---|
| 1 | Fibre optics | none | UNCOVERED | no KC/TM | IMPLEMENTATION_GAP |
| 2 | Lasers | none | UNCOVERED | no KC/TM | IMPLEMENTATION_GAP |
| 3 | Electronics | kc.electric_circuits (UP2 9.4/10.3) covers circuits only | PARTIAL | no semiconductor/diode/transistor/logic concept | IMPLEMENTATION_GAP |
| 4 | Friction/machines | kc.work_energy_power; Newton KCs | PARTIAL | no friction-force concept; no efficiency/mechanical-advantage relationship | IMPLEMENTATION_GAP |
| 5 | EM spectrum depth | kc.wave_phenomena (UP1 15.1/16.1); kc.electromagnetism (13.1) | PARTIAL | spectrum ordering/properties (UP2 16.5) absent | IMPLEMENTATION_GAP |
| 6 | Energy and society | kc.work_energy_power, kc.heat_temperature | PARTIAL | sources-of-energy/renewable distinction absent (UP1 8.5) | IMPLEMENTATION_GAP |
| 7 | Practical detail | kc.practical_measurement + tm.practical_physics (b042) | PARTIAL (evidence) | WAEC practical detail SOURCE_UNVERIFIED; implementation acceptable | OFFICIAL_VERIFICATION_GAP (not implementation) |

## Scope decision (PROPOSED, evidence-backed)
Items 1–6 are JAMB-numbered topic families (R17/R18/R19 rows in
PHYSICS_COVERAGE_MATRIX.md were deferred as SHOULD). Under Standard v1.2
clause B ("no material omissions in scope"), the deferred SHOULD rows now
block IMPLEMENTATION_COMPLETE. Build them unless owner marks OUT_OF_SCOPE —
flagged as prospective, owner override recorded in closure register (not
decided silently).

## Implementation sequence (dependency-aware)
059 friction + machines (KC friction; extends existing work/energy chain)
060 EM spectrum depth (KC em_spectrum; downstream of wave_phenomena)
061 sources of energy / energy and society (KC energy_sources; downstream
of work/energy + heat)
062 fibre optics (KC fibre_optics; downstream of optics)
063 lasers (KC laser_basics; downstream of optics + em_spectrum)
064 electronics (KC semiconductor_electronics; downstream of circuits)

Each: KC + TM + Methods + DERIVED/scoped prereqs + evidence (OpenStax
vol pages verified 200) + HUMAN review + updates to matrix. Store `[]` gate
per batch; full-suite gate at phase end.
