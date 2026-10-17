# JAMB Chemistry — Official Coverage Matrix (Phase 18)

Authority: JAMB (Joint Admissions and Matriculation Board), "UTME Syllabus —
Chemistry", E-syllabus PDF as published on the official Integrated Brochure &
Syllabus System (IBASS), retrieved 2026-10-17.
Source record: docs/source-documents/SRC.JAMB.UTME.CHEM.2025.json
(SHA-256 a3c15bfee3beac0f4106a32b0091e2a2c51eaec8baa62fafa44afcad72193738;
16 pages; PDF metadata 2025-07-30; not committed — copyrighted).
Locator convention: "JAMB Chem p.N" = extracted-text page N of that exact
PDF revision.

This matrix is checked directly against the official JAMB document (NOT a
secondary mirror). It records JAMB-side requirement confirmation and CDG
coverage. It does NOT change subject governance status: WAEC official
WASSCE documents remain unretrieved and NERDC SSS 3 remains unavailable, so
Chemistry remains BOARD_UNVERIFIED at subject level (CI-24). Chemistry
implementation status is IMPLEMENTATION_PARTIAL and changes here do NOT
alter it. The Phase 16B secondary matrix
(JAMB_CHEMISTRY_SECONDARY_COVERAGE.md) is retained as audit history and
remains labelled SECONDARY.

Coverage categories: COVERED | PARTIALLY_COVERED | NOT_COVERED |
NOT_APPLICABLE | UNRESOLVED.
Coverage rule: a topic is COVERED only if the CDG supports the relevant scope
and depth of the listed topic/objective (matching names is insufficient).
CDG baseline: build_graph_v40 — Chemistry 21 KCs (IMPLEMENTATION_PARTIAL /
BOARD_UNVERIFIED).

| authority | subject | document_version | official_topic | official_subtopic_or_objective | cdg_entity_ids | coverage_status | evidence_reference | gap_description | next_action |
|---|---|---|---|---|---|---|---|---|---|
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17; no cycle year printed) | 1. Separation of Mixtures and Purification of Chemical Substances | Elements/compounds/mixtures; physical/chemical changes; pure/impure substances; m.p./b.p./density criteria; separation processes (evaporation, distillation, sublimation, recrystallization, chromatography, decantation, filtration, magnetization) | kc.matter_classification | PARTIALLY_COVERED | JAMB Chem p.1 (official); CDG classify-matter TM | Separation-process list partially evidenced (filtration/distillation/chromatography only) | C-10 owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 2. Chemical Combination | Laws of definite, multiple and reciprocal proportions; law of conservation of matter; calculations | kc.mole_stoichiometry | PARTIALLY_COVERED | JAMB Chem p.1 (official) | Proportion laws and conservation-of-matter objectives not explicitly evidenced | Owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 3. Kinetic Theory of Matter and Gas Laws | Melting/vaporization/boiling/freezing/condensation; Brownian motion; Boyle/Charles/Avogadro/Gay-Lussac/Graham/Dalton laws; molar volume; ideal gas equation; relationship with kinetic theory | kc.gas_behaviour, kc.matter_classification | PARTIALLY_COVERED | JAMB Chem p.2 (official); CDG gas_behaviour KC (tm.gas_problems) | Gas laws covered; kinetic-theory phenomena and Graham/Dalton law objectives partially evidenced | Owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 4. Atomic Structure and Bonding | Atoms/molecules/ions; Dalton–Bohr models; four quantum numbers; orbital arrangement rules; electron configuration; atomic/mass number; isotopes; bonding types | kc.atomic_structure_periodicity, kc.chemical_bonding | PARTIALLY_COVERED | JAMB Chem pp.2–3 (official) | Quantum-number/orbital detail and isotope calculations partially evidenced | Owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 5. Nuclear Chemistry | Radioactivity types/properties/detection; natural/artificial radioactivity; half-life calculations; nuclear equations; applications | kc.atomic_nuclear_physics (Physics CDG) | PARTIALLY_COVERED | JAMB Chem p.3 (official) | Chemistry-specific nuclear objectives (detection, nuclear equations, applications) not evidenced; partial overlap via physics atomic/nuclear KC | Owner decision: nuclear-chemistry scope |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 6. Solubility | Unsaturated/saturated/supersaturated solutions; solubility curves; solubility in mol/dm³; solvents for fats/oils/paints; true/false solutions (suspensions, colloids) | — | NOT_COVERED | JAMB Chem p.4 (official) | No solubility KC (C-09) | C-09 owner decision (officially confirmed) |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 7. Environmental Pollution | Air: natural gaseous constituents and proportions; pollutants and effects; water pollution (sewage/oil); pollution control | — | NOT_COVERED | JAMB Chem pp.4–5 (official) | No pollution/air KC (C-02, C-08) | Owner decision (officially confirmed) |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 8. Acids, Bases and Salts | Characteristics/properties/uses; indicators; basicity; normal/acidic/basic/double salts; H3O⁺/proton-donor definitions; organic acids; alums; salt preparation; hydrolysis | kc.acids_bases_salts, kc.ph_scale | PARTIALLY_COVERED | JAMB Chem pp.5–6 (official); CDG acids/bases and pH KCs | Salt preparation and hydrolysis detail (C-11) not evidenced | C-11 owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 9. Oxidation and Reduction — Redox | Oxidation via oxygen/hydrogen/electron transfer; oxidation numbers; balancing; IUPAC nomenclature using oxidation number; tests | kc.redox_electrochemistry | COVERED | JAMB Chem pp.6–7 (official); CDG redox KC | — | — |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 10. Electrolysis | Electrolytes; Faraday's laws; electrolysis of specified solutions; discharge factors; uses (purification, element production); electrochemical cells | kc.redox_electrochemistry | COVERED | JAMB Chem p.7 (official) | — | — |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 11. Energy Changes | Enthalpy changes (dissolution/reaction); endothermic/exothermic; entropy; spontaneity (ΔG criterion) | kc.chemical_energetics | PARTIALLY_COVERED | JAMB Chem pp.7–8 (official) | Entropy and spontaneity (ΔG) objectives not evidenced (Hess/enthalpy covered) | Owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 12. Rates of Chemical Reaction | Factors: temperature, concentration/pressure, surface area, catalyst; rate measurement (incl. iodine clock); rate curves | kc.rates_equilibrium | COVERED | JAMB Chem p.8 (official) | — | — |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 13. Chemical Equilibria | Reversible reactions; dynamic equilibrium; factors governing equilibrium position | kc.rates_equilibrium | COVERED | JAMB Chem p.8 (official) | — | — |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 14. Non-metals and their Compounds | Hydrogen (production/properties/uses/tests); halogens (chlorine representative: preparation, properties, uses); oxygen/sulphur; nitrogen; carbon; phosphorous compounds | — | NOT_COVERED | JAMB Chem pp.9–11 (official) | No non-metals KC (C-03) | C-03 owner decision (officially confirmed) |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 15. Metals and their Compounds | General properties; alkali metals (NaOH, Na2CO3, NaCl production/uses); alkaline-earth (calcium compounds); aluminium (bauxite electrolysis); iron; copper; extraction; alloys | — | NOT_COVERED | JAMB Chem pp.11–13 (official) | No metals KC (C-04); transition-metal deferral CI-14 documented | C-04/CI-14 owner decision (officially confirmed) |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 16. Organic Compounds | Tetravalency; IUPAC nomenclature; empirical formulae; aliphatic hydrocarbons (alkanes/alkenes/alkynes); benzene; alkanols; alkanals/alkanones; alkanoic acids; alkanoates (soap/margarine, saponification); amines; amides; carbohydrates; proteins; fats/oils; polymers | kc.organic_foundations, kc.reactions_of_alkanes, kc.reactions_of_alkenes, kc.isomerism, kc.alcohols, kc.ethers, kc.aldehydes_ketones, kc.carboxylic_acids, kc.amines, kc.amides | PARTIALLY_COVERED | JAMB Chem pp.13–15 (official); CDG organic KCs (b065) | Alkynes, benzene/aromatics, carbohydrates, proteins, fats/oils and polymers (C-05; polymers deferred CI-13) not evidenced | C-05 owner decision |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 17. Chemistry and Industry | Chemical industries: types, raw materials, relevance; biotechnology | — | NOT_COVERED | JAMB Chem p.15 (official) | No industrial-chemistry KC; deferral C-07/CI-14 documented | C-07/CI-14 (deferred, owner-documented) |
| JAMB | Chemistry | UTME E-syllabus (IBASS, retrieved 2026-10-17) | 18. Astronomical Chemistry | Solar system, planets, satellites; composition of the earth (atmosphere, lithosphere, hydrosphere) | — | NOT_COVERED | JAMB Chem p.15 (official) | No astronomical-chemistry KC; newly exposed by the official JAMB document (not present in the Phase 16B secondary lists) | Owner decision: new gap (recorded Phase 18) |

## Summary

- COVERED against the official JAMB Chemistry syllabus: 4 of 18 topics
  (9 Redox; 10 Electrolysis; 12 Rates of Chemical Reaction; 13 Chemical
  Equilibria).
- PARTIALLY_COVERED: 8 topics (1, 2, 3, 4, 5, 8, 11, 16). NOT_COVERED:
  6 topics (6 Solubility; 7 Environmental Pollution; 14 Non-metals;
  15 Metals; 17 Chemistry and Industry; 18 Astronomical Chemistry).
- Newly exposed official requirement: topic 18 "Astronomical Chemistry" is
  not present in the Phase 16B secondary lists — recorded as a new gap
  (Phase 18).
- Deferrals C-06/C-07 (polymers; industrial chemistry, CI-13/CI-14) remain
  owner-documented and are NOT reopened by this matrix.
- No subject status is promoted — WAEC official documents remain
  unretrieved (BOARD_UNVERIFIED); Chemistry stays IMPLEMENTATION_PARTIAL.
