# Phase 17 Mathematics Scope Expansion — Four-Family Audit

Date: 2026-10-17. Baseline: commit `1afe4a4` ("Phase 16B: secondary syllabus comparison … 151 tests green"),
working tree clean. Canonical store (builder `build_graph_v39`): 340 entities / 554 claims /
276 evidence / 83 sources; Mathematics 39 KCs, status IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED
(declared OpenStax-based scope, Phases 11–13.6).

Purpose: audit the four owner-authorized Mathematics topic families before any implementation:
(1) Sets and logic, (2) Sequences and series, (3) Matrices and determinants, (4) Mensuration.

## Source evidence inspected (official)

- NERDC / Federal Ministry of Education, "New Revised Senior Secondary School Curriculum —
  Mathematics SSS 1", © October 2025 (retrieved + text-extracted Phase 16; SHA-256 a2f618…11c).
  Topics: Sets p.7; Logic p.8; Mensuration p.11.
- NERDC / Federal Ministry of Education, "New Revised Senior Secondary School Curriculum —
  Mathematics SSS 2", © October 2025 (retrieved + text-extracted Phase 16; SHA-256 f79d3f…f1cd).
  Topic: Sequence and Series p.1.
- Secondary (non-authoritative): Syllabus NG JAMB/WAEC Mathematics pages (Phase 16B). Used for
  matrices/determinants only where NERDC SSS1/SSS2 are silent; current-cycle applicability UNRESOLVED.

## B1 — Sets and logic (audit)

| Subtopic | Status | Evidence | CDG entities | Deficiency |
|---|---|---|---|---|
| Meaning of a set; set notations (roster, rule, set-builder) | MISSING | NERDC Math SSS1 p.7 (objective 1–2; knowledge: definition, notations) | none | No sets KC/TM/method/item |
| Types of sets (empty, subset, infinite, universal) | MISSING | NERDC Math SSS1 p.7 (objective 3; knowledge: types of sets) | none | No sets KC |
| Set operations: union, intersection, complement | MISSING | NERDC Math SSS1 p.7 (objective 4; knowledge: set operations) | none | No set-operation KC |
| Apply sets to daily-life problems | MISSING | NERDC Math SSS1 p.7 (objective 5; skill) | none | No assessment item |
| Simple/compound statements; logical operators; truth values | MISSING | NERDC Math SSS1 p.8; SSS2 p.9 (logic objectives 1–6) | none | No logic KC |
| Negations, conjunctions, disjunctions, conditional, bi-conditional | MISSING | NERDC Math SSS1 p.8 (knowledge: compound statements) | none | No logic KC |

Verdict: Sets and logic are MISSING (no existing representation). Source: NERDC official
(SSS1 pp.7–8; SSS2 p.9 duplicate logic topic). Prerequisites: none defensibly required — both are
foundational topics in the Algebraic Processes theme. Logic may adjacently relate to sets
(curriculum-adjacency elaboration, not source-mandated); mark project-authored.

## B2 — Sequences and series (audit)

| Subtopic | Status | Evidence | CDG entities | Deficiency |
|---|---|---|---|---|
| Meaning and types of sequences and series | MISSING | NERDC Math SSS2 p.1 (knowledge 1) | none | No sequences KC |
| A.P.: first term, common difference, nth term, arithmetic mean | MISSING | NERDC Math SSS2 p.1 (knowledge 2; objectives 2, 4) | none | No A.P. KC |
| G.P.: first term, common ratio, nth term, geometric mean | MISSING | NERDC Math SSS2 p.1 (knowledge 3; objectives 3, 4) | none | No G.P. KC |
| Real-life problems involving A.P. and G.P. | MISSING | NERDC Math SSS2 p.1 (objective 4; skill) | none | No assessment item |

Verdict: Sequences and series MISSING. Source: NERDC official (Math SSS2 p.1). Prerequisite:
number-pattern work builds on integer arithmetic/algebra — link UNDERSTAND from
`kc.integer_arithmetic` (curricular adjacency, project-authored).

## B3 — Matrices and determinants (audit)

| Subtopic | Status | Evidence | CDG entities | Deficiency |
|---|---|---|---|---|
| Matrix notation, dimensions, equality | MISSING | JAMB SN6; WAEC topic 11 (secondary via Syllabus NG) | none | No matrices KC |
| Matrix operations (add/subtract/scalar multiply/multiply) | MISSING | JAMB SN6; WAEC topic 11 (secondary) | none | No matrix-operation KC |
| Determinants (≤3×3); inverses (2×2) | MISSING | JAMB SN6; WAEC topic 11 (secondary) | none | No determinant/inverse KC |
| Solving simultaneous equations using matrices | MISSING | JAMB SN6; WAEC topic 11 (secondary) | none | No assessment item |

Verdict: Matrices and determinants MISSING. SCOPE CONFLICT: authorized by owner for Phase 17, but
NOT present in NERDC SSS1/SSS2 topic lists (SSS3 unretrieved). Only secondary-source evidence
(JAMB/WAEC via Syllabus NG) is available. Per Subject Completion Standard clause A
("Secondary mirrors never authoritative"; "Official alignment claimed only from official
evidence"), matrices content is implemented with explicit disclosure that its evidence is
secondary-only and official verification remains BOARD_UNVERIFIED. Prerequisite: UNDERSTAND from
`kc.linear_equations_one_var` (simultaneous-equations context, project-authored).

## B4 — Mensuration (audit)

| Subtopic | Status | Evidence | CDG entities | Deficiency |
|---|---|---|---|---|
| Lengths of arcs of circles | MISSING | NERDC Math SSS1 p.11 (objective 1; knowledge 1) | none | No mensuration KC |
| Perimeters and areas of sectors and segments | MISSING | NERDC Math SSS1 p.11 (objectives 2–3; knowledge 2–4) | none | No mensuration KC |
| Surface areas and volumes of solid shapes (cube, cuboid, cylinder, cone, prism, pyramid) | MISSING | NERDC Math SSS1 p.11 (objective 5; knowledge 6) | none | No mensuration KC |
| Frustum of cone and pyramid; compound shapes | MISSING | NERDC Math SSS1 p.11 (objectives 6–7; knowledge 7–8) | none | No mensuration KC |

Verdict: Mensuration MISSING. Source: NERDC official (Math SSS1 p.11). Prerequisite: circle
measurement builds on circle geometry — link UNDERSTAND from `kc.circle_angle_theorems`
(curricular adjacency, project-authored).

## B5 — Duplicate / conflict check

- No existing KC id collides with proposed new ids (`kc.sets_operations`, `kc.logical_reasoning`,
  `kc.sequences_series`, `kc.matrix_algebra`, `kc.mensuration`). Verified against all 39
  Mathematics KCs.
- No existing TaskModel/Method/Item covers sets, logic, sequences, matrices, or mensuration.
- No cross-subject dependency changes required. Mathematics remains independent root subject.
- No cycles introduced (all new prerequisites point downward into existing foundational KCs;
  matrices → linear equations, sequences → integer arithmetic, mensuration → circle theorems;
  sets/logic are foundational with no prerequisite).
- Existing Mathematics median/dispersion, logarithms, and all cross-subject edges unaffected.

## Proposed implementation delta (dependency-aware sequence)

| Batch | Family | New KC | TM | Methods | Items | Prerequisite claims |
|---|---|---|---|---|---|---|
| 066 | Sets & logic | kc.sets_operations; kc.logical_reasoning | tm.set_operations; tm.logical_reasoning | 2–3 each | 1 each | logic UNDERSTAND→sets (ALL/ASSERTED) |
| 067 | Sequences & series | kc.sequences_series | tm.sequences_series | 2 | 1 | sequences UNDERSTAND→integer_arithmetic (ALL/ASSERTED) |
| 068 | Matrices & determinants | kc.matrix_algebra | tm.matrix_algebra | 2 | 1 | matrix UNDERSTAND→linear_equations_one_var (ALL/ASSERTED) |
| 069 | Mensuration | kc.mensuration | tm.mensuration | 2 | 1 | mensuration UNDERSTAND→circle_angle_theorems (ALL/ASSERTED) |

All new claims ACCEPTED with HUMAN review; evidence excerpts paraphrased from NERDC (official)
for sets/logic/sequences/mensuration, and from Syllabus NG JAMB/WAEC (secondary, disclosed) for
matrices. No schema change; 13 entity types preserved; `indicates` untouched (PROPOSED);
no Biology/English artifacts.

## Gate

Before implementation: baseline tests 151 passing, store validation `[]`. After implementation:
full suite green, store `[]`, generators byte-identical, new tests added for each family.
