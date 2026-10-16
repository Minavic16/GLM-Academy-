# Chemistry Coverage Matrix (Phase 13)

Scope: foundational Chemistry slice 043–052. Denominator = candidate scope
families from the Phase 13 plan (OpenStax Chemistry 2e structure corroborated
by known JAMB/WAEC topic families). Official Chemistry PDFs pending — every
row citing only OpenStax + mirror knowledge is marked accordingly; no row
claims official alignment.

| Family | KC | TM / Methods | Status | Evidence |
|---|---|---|---|---|
| Matter, mixtures, separation | kc.matter_classification | tm.classify_matter / separate-mixtures | COVERED | CHEM2E 1.2 |
| Atomic structure, periodicity | kc.atomic_structure_periodicity | tm.atomic_model_problems / electron-arrangement, trend-prediction | COVERED | CHEM2E 2.1 |
| Bonding, formulae | kc.chemical_bonding | tm.bonding_problems / ionic-vs-covalent, formula-from-valency | COVERED | CHEM2E 7.1/7.2 |
| Mole, stoichiometry | kc.mole_stoichiometry | tm.stoichiometry_problems / mole-ratio, empirical-formula | COVERED | CHEM2E 3.1/4.2 |
| Acids, bases, salts, titration calc | kc.acids_bases_salts | tm.acid_base_problems / neutralisation-titration | COVERED | CHEM2E 14.1 |
| Redox, electrolysis | kc.redox_electrochemistry | tm.redox_problems / redox-identification, electrolysis-quantitative | COVERED | CHEM2E 17.1/17.7 |
| Energetics | kc.chemical_energetics | tm.energetics_problems / enthalpy-hess | COVERED | CHEM2E 5.1 |
| Rates, equilibrium | kc.rates_equilibrium | tm.rate_equilibrium_problems / rate-curves, le-chatelier | COVERED | CHEM2E 12.1/13.1 |
| Gases, molar volume | kc.gas_behaviour | tm.gas_problems / combined-gas-law | COVERED | CHEM2E 9.2 |
| Organic foundations — naming only | kc.organic_foundations | tm.organic_problems / hydrocarbon-naming | COVERED (naming only) | CHEM2E 20.1 |
| Organic reactions (Phase 15, batch 065) | kc.reactions_of_alkanes, kc.reactions_of_alkenes, kc.isomerism, kc.alcohols, kc.ethers, kc.aldehydes_ketones, kc.carboxylic_acids, kc.amines, kc.amides | one TM per reaction family (tm.alkane_reactions … tm.amide_reactions) | COVERED | CHEM2E 20.1–20.4 |
| Practical chemistry | kc.practical_chemistry | tm.practical_chemistry / titration-procedure, qualitative-tests | PARTIAL (WAEC detail unverified) | CHEM2E 14.7 + WAEC (unverified detail) |
| Buffers (buffer solutions) | — | — | NOT_COVERED — BLOCKED (Phase 15 scope constraint) | CHEM2E 14-6 verified; see PHASE15_GAP_AUDIT.md |
| Polymers, industrial chemistry | — | — | NOT_COVERED (deferred) | — |
| Electrolytic cells detail, transition metals | — | — | NOT_COVERED (deferred) | — |

Notes on the Phase 15 update (2026-10-16):
- Row "Organic reactions" was the only implementation gap in Chemistry's
  declared scope. It is IMPLEMENTED by batch 065
  (`examples/chemistry_organic_reactions.py`, `build_graph_v39`):
  the nine KCs above, each with a targeting TM, Methods, Items, and
  ACCEPTED claims; all prerequisites are Chemistry-internal (no new
  cross-subject dependency claims).
- Row "Buffers" cannot be implemented in Phase 15: buffer pH calculations
  require the Mathematics logarithms KC. Creating that prerequisite edge
  would modify Mathematics-side records, which Phase 15 forbids.
  Blocked with this constraint; re-evaluate only after owner
  authorization.
- Rows "Polymers" and "Industrial chemistry" were explicitly deferred by
  owner-documented scope decisions and are unchanged.
- Row "Electrolytic cells detail / transition metals" was explicitly
  deferred; unchanged.
- Row "Practical chemistry" remains PARTIAL only with respect to official
  board verification (CI-05); its implementation is complete.

Cross-subject edges added (all existing contract, reviewed, accepted):
ratio→mole, percentage→mole (method), mole→acids, bonding→mole,
bonding→redox (method), mole→redox (method), circuits(Physics)→redox
(method), mole→energetics (method), mole→gases, ratio→gases,
bonding→organic, acids→practical (method), matter→practical (method),
function→rates (method), matter→atomic (UNDERSTAND ASSERTED).
No Chemistry KC duplicates any Math/Physics KC (test-enforced).
Phase 15 added no cross-subject prerequisite claims (all new
prerequisites are Chemistry-internal).
