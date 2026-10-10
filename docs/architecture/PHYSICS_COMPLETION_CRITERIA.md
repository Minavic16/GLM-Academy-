# Physics Completion Criteria (Phase 12B)

Date: 2026-10-10. Scope: Nigerian senior-secondary Physics for JAMB UTME +
WAEC WASSCE preparation, NERDC-aligned where verifiable.

## Completion statuses

- Engineering complete: store validation `[]`, full pytest green, serialization
  round-trip OK, export_view OK, visualization deterministic.
- Curriculum mapped: every requirement row in `PHYSICS_COVERAGE_MATRIX.md` has
  a mapping status; no mandatory row left blank.
- Source verified: a COVERED claim cites an inspected document (OpenStax page
  fetched HTTP 200, or official PDF if retrieved). Mirror-derived topic
  wordings are SOURCE_UNVERIFIED and cannot alone support COVERED.
- Scope complete: every MUST-level requirement is COVERED with accepted,
  human-reviewed claims; practicals accounted for (modeled or gap-recorded).
- Partially complete: any MUST requirement NOT_COVERED/PARTIALLY_COVERED, or
  official-document confirmation pending.
- Blocked: missing evidence prevents any defensible assessment.
- OWNER_REVIEW_REQUIRED: scope decisions for the owner (e.g., treating mirror
  topic lists as the JAMB denominator).

## Mandatory requirement levels

- MUST: JAMB-numbered topic families present in the mirror reconstruction AND
  corroborated by OpenStax/university-physics content or WAEC structure
  knowledge explicitly cited; measurement, kinematics, Newton, work/energy,
  waves, optics, electricity, magnetism, modern physics, practicals.
- SHOULD: second-order subtopics (e.g., Lenz's-law direction reasoning,
  transformer calculations) — accept PARTIALLY_COVERED.
- DEFER: university-level depth beyond SS scope (e.g., Maxwell derivations).

## Per-entity gates

1. Every ACCEPTED KC has ≥1 targeting TaskModel with ≥1 Method; every Method
   has ≥1 `requires`; every ACCEPTED claim has evidence + HUMAN review +
   admissible basis (existing validators enforce).
2. Practical competencies: modeled as KCs with TMs, or recorded as explicit
   gaps — never silently dropped.
3. Cross-subject edges: DERIVED from a Method's `requires` wherever possible;
   ASSERTED only with dedicated evidence.
4. No requirement marked COVERED without resolvable entity IDs + evidence.
5. Proposed entities never counted as accepted coverage (tests enforce).
