# Phase 13 Implementation Plan

Baseline verified 2026-10-10: branch `main` @ `7308fe2`, clean tree,
**101 tests pass**, canonical 219 entities / 55 KCs (36 Math + 19 Physics) /
357 Claims / 235 Evidence / 55 Sources. No Chemistry records exist.

## Slice boundary (043–052)

Foundational, dependency-rich Chemistry only; each KC maps to JAMB-topic
families corroborated by OpenStax Chemistry 2e sections (all URLs verified
HTTP 200 before citation). Official JAMB/WAEC/NERDC Chemistry PDFs remain
pending (same retrieval pattern as Physics — recorded, not fabricated).

| Batch | KC | TM / Methods | Key prereqs |
|---|---|---|---|
| 043 | kc.matter_classification | tm.classify_matter / separate-mixtures, identify-particles | alg (TM DERIVED) |
| 044 | kc.atomic_structure_periodicity | tm.atomic_model_problems / electron-arrangement, trend-prediction | matter→atomic (UNDERSTAND ASSERTED, ALL) |
| 045 | kc.chemical_bonding | tm.bonding_problems / ionic-vs-covalent, formula-from-valency | atomic→bonding (TM DERIVED) |
| 046 | kc.mole_stoichiometry | tm.stoichiometry_problems / mole-ratio, empirical-formula (% → method) | bonding→mole (TM DERIVED); ratio→mole (TM DERIVED); percentage→mole (method DERIVED) |
| 047 | kc.acids_bases_salts | tm.acid_base_problems / neutralisation-titration-calc | mole→acids (TM DERIVED) |
| 048 | kc.redox_electrochemistry | tm.redox_problems / redox-identification (bonding), electrolysis-quantitative (mole + physics circuits) | bonding/mole/circuits→redox (method DERIVED) |
| 049a | kc.chemical_energetics | tm.energetics_problems / enthalpy-hess (mole) | mole→energetics (method DERIVED) |
| 049b | kc.rates_equilibrium | tm.rate_equilibrium_problems / rate-curves, le-chatelier | energetics? no — standalone + alg |
| 050 | kc.gas_behaviour | tm.gas_problems / combined-gas-law (mole + ratio) | mole→gases (TM DERIVED); ratio→gases (TM DERIVED) |
| 051 | kc.organic_foundations | tm.organic_problems / hydrocarbon-naming (bonding) | bonding→organic (TM DERIVED) |
| 052 | kc.practical_chemistry | tm.practical_chemistry / titration-procedure, qualitative-tests (matter) | matter→practical (method DERIVED); units? no |

Expected deltas: +11 KCs, +11 TMs, ~15 Methods, ~110 Claims, ~60 Evidence,
~12 Sources. New relation types: none. New governance exceptions: none.

## Files
- New: `examples/chem_wave1.py` (043–047), `examples/chem_wave2.py` (048–052),
  `tests/test_chemistry_slice.py`, `docs/batch_records/BATCH_043_052_chemistry.md`,
  `docs/architecture/CHEMISTRY_SCOPE.md` (update).
- Modified: `tools/generate_math_cdg_docs.py` (builder import + DOMAIN/BATCH maps),
  `examples/math_cdg_v2.json`, generated docs + visualizations, migration ledger note.
