# Chemistry Scope (Phase 11 — RESEARCHED, not accepted data)

## 1. NERDC scope
- Revised SSS 1–3 science curriculum with Chemistry as a core science.
- Foundations in SSS1 (matter, states, particles, separation); organic
  introduction in SSS2; broader organic, energetics, equilibrium/
  industrial chemistry in SSS3 (per public summaries of the 2025 scheme).
- Limitation: full per-topic list requires NERDC PDF retrieval.

## 2. WAEC scope
- WASSCE Chemistry covers: basic concepts (matter, elements/compounds,
  mixtures, separation), atomic structure & bonding, periodicity, mole
  concept & stoichiometry, gases, energetics, rates & equilibrium, acids/
  bases/buffers, redox/electrochemistry, organic (alkanes, alkenes,
  ethanol/ethanoic acid derivatives), hydrocarbons, polymer basics,
  practices: test-tube tests, combined volumetric (titrimetry).

## 3. JAMB scope
- JAMB UTME Chemistry: matter, atomic theory, periodic classification,
  chemical bonding, mole concept, stoichiometric calculations, rates,
  equilibrium, acids & bases, redox, electrolysis, organic chemistry
  (structure/naming/reactions), qualitative analysis basics.

## 4. Normalized canonical domains (proposed, PROPOSED label)
1. Basics of Matter & States
2. Atomic Structure & Periodicity
3. Chemical Bonding & Structure
4. Mole Concept & Stoichiometry
5. Gases & Solutions
6. Energetics
7. Rates of Reaction & Equilibrium
8. Acids, Bases, Buffers
9. Redox & Electrochemistry
10. Organic Chemistry — Introduction
11. Hydrocarbons
12. Organic Reactions & Polymers
13. Industrial Chemistry
14. Qualitative Analysis & Practicals

## 5. Topic mappings (facts from official pages)
- Mole concept ↔ WAEC essay+objective questions; NERDC treats stoichiometry
  as a compulsory SSS1 topic (per the 2025 scheme summary).
- Organic naming systematic Nomenclature ↔ WAEC/JAMB align.
- Electrolysis → WAEC electrochemistry section; JAMB focuses electrolysis.

## 6. Source conflicts
- Extent of "industrial chemistry" differs: WAEC includes several large-scale
  named processes; JAMB keeps a limited set; NERDC emphasizes local
  industrial context.
- Buffer-solution depth in JAMB vs WAEC.

## 7. Terminology normalization
- "mole concept" / "mole calculations" — canonical: `mole_concept`
- "redox reaction" / "oxidation-reduction" — canonical: `redox_reaction`
- "structural formula" vs "displayed formula" — canonical: `structural_formula`

## 8. Candidate KC areas
- matter_states, separation_techniques, atomic_structure_periods,
  ionic_covalent_bonding, mole_and_stoichiometry, gas_laws,
  enthalpy_changes, rate_of_reaction, equilibrium_law, acid_base_titrations,
  redox_electrolysis, functional_groups, alkane_alkene_reactions,
  polymerisation_basics, qualitative_tests.
- All PROPOSED; none entered into the CDG this phase.

## 9. Candidate TaskModel areas
- compute_molar_mass, apply_stoichiometry_ratio, write_balanced_equation,
  predict_periodic_trends, conduct_titration_calculation, name_simple_alkanes.

## 10. Practical/laboratory considerations
- WAEC requires practical paper; NERDC requires laboratory exercises;
  JAMB omits practical. Titration appears in WAEC/NERDC.

## 11. Mathematical prerequisites (research hypotheses, evidence-gated)
- Ratio/proportion → stoichiometry and molar ratios
- Algebraic equations → balancing equations, gas law rearrangements
- Scientific notation/indices → concentration, Avogadro-scale calculations
- Logarithms → pH calculations (pH = -log[H+])
- Graph interpretation → rate curves, equilibrium shifts
- Percentage calculations → empirical formula work

## 12. Unresolved questions
- Detailed buffer/industrial-chemistry split across boards unresolved.
- Exact NERDC PDF retrieval still pending.

## 13. Explicit exclusions
- No chemistry KCs created in CDG. No item bank, scoring, lab manual, or
  observations stored.

---

## Phase 13 update — foundational slice implemented (043–052)

11 KCs ACCEPTED across matter → atomic → bonding → mole → acids/redox/
energetics/rates/gases/organics/practical (see CHEMISTRY_COVERAGE_MATRIX.md).
All content evidence OpenStax Chemistry 2e (URLs verified HTTP 200 pre-build);
official JAMB/WAEC/NERDC Chemistry PDFs still pending — board-level
confirmation remains OWNER_REVIEW_REQUIRED. Deferred: buffers/pH (needs Math
log KC), polymers, industrial chemistry, transition-metal detail.
