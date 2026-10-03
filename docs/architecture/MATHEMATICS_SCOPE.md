# GLM Mathematics CDG — Scope (v0.2 working document)

Date: 2026-10-03. Status: WORKING SCOPE.

## Sources in the repository (inventory)

- Legacy corpus `glm_cdg_package.zip` (2026-09-28):
  - 169 candidate nodes across 6 curriculum domains
    (I. Number and Numeration, II. Algebra, III. Geometry/Trigonometry,
    IV. Calculus, V. Statistics, Foundational prior-knowledge).
  - 287 candidate relationships, 609 evidence records, source inventory
    including JAMB UTME Mathematics syllabus, NERDC SSS1/SSS2 2025
    curriculum, WAEC WASSCE Mathematics syllabus, OpenStax Intermediate
    Algebra 2e sections.
- **This corpus is a migration input / evidence source, NOT authoritative
  truth.** Every legacy record enters the v0.2 graph only through the
  agent-proposal → evidence/provenance → review → acceptance path.
- PDFs on device (JUPEB Mathematics practice, SS1 Mathematics exams, WAEC
  syllabi) are candidate future evidence sources; they have NOT been used
  as accepted evidence in any CDG record yet.

## Inclusion boundary (Mathematics scope)

The CDG covers the Mathematics knowledge required by the JAMB UTME /
WAEC WASSCE Mathematics use case, organized by the curriculum's own
domains:

1. Number and Numeration (incl. foundational prior knowledge)
2. Algebra (polynomials, factorisation, inequalities, progressions,
   matrices/determinants, variation, binary operations, sets)
3. Geometry and Trigonometry (Euclidean geometry, mensuration,
   trigonometry basics)
4. Coordinate Geometry
5. Calculus (differentiation, application, integration)
6. Statistics and Probability (data representation, location,
   dispersion, permutation/combination, sets statistics, probability)

## Exclusion boundary

- No learner model, learner identifiers, mastery thresholds, or
  observations (deferred to a later learner-model contract).
- No assessment-scoring, recommendation, or remediation entities.
- No probabilistic or weighted edges.
- No automatic prerequisite inference, no vector-derived edges.
- Mathematics subdomains outside the above source evidence are out of
  scope until evidence appears.

## Unresolved curriculum questions

- Ownership/home of knowledge shared between Mathematics and future
  Physics/Chemistry KCs is intentionally not decided.
- Equivalence handling for duplicate legacy nodes: legacy IDs retained in
  `legacy_ids`; no equivalence relation introduced.
- `indicates` contract (`OWNER_SIGN_OFF_REQUIRED`) remains open; any new
  `indicates` claims stay PROPOSED.
