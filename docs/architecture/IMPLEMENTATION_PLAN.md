# GLM CDG v0.2 — Implementation Plan (Bootstrap)

Date: 2026-10-03. Owner: GLM Academy. Status: PLAN (pre-code review gate).

## 0. Authoritative source status — FLAGGED CONFLICT

The task specifies the authoritative source as `docs/architecture/GLM_CDG_v0.2_FREEZE.md`.
That file does **not** exist in this repository (`Minavic16/GLM-Academy-` is empty),
and no copy exists on the execution device. The available authoritative-adjacent artefact is:

- `GLM_CDG_v0.2_Contract_Sanity_Check.md` (2026-09-29, pre-contract review of the frozen model)

Per the task's stop-condition rule this was escalated; the human owner elected to proceed
treating the Sanity Check document as the contract source, with the freeze-doc gap recorded
as an open risk. No semantic content beyond the Sanity Check + the task brief itself has
been invented.

## 1. Repository findings

- `Minavic16/GLM-Academy-` GitHub repo: **empty** (no commits, no branches).
- Local `/root/glm-academy`: fresh clone of the above; no existing GLM code.
- Legacy research corpus present: `glm_cdg_package.zip` (JAMB Mathematics candidate CDG,
  2026-09-28): `glm_cdg_nodes.json/csv`, `glm_cdg_edges.json/csv`,
  `glm_cdg_evidence.json/csv`, `glm_cdg_sources.json`, `glm_cdg_qc.json`.
  Status: PROPOSED, not validated. Legacy types include `prerequisite_of`,
  `alternative_group`, `necessity_class`, `dependency_strength`, legacy node ids
  like `MATH.FND.*`. To be treated as read-only research corpus, not authoritative v0.2 data.
- No existing GLM graph DB, vector DB, or API in the workspace. NestQuant/NestEdge
  directories are unrelated trading/school-engine code; they define conventions
  (pyproject + pytest + dataclasses) that we may follow for packaging style only.

## 2. Relevant existing components

- Python 3.12, pytest 9.1.1 available. No pydantic. No graph DB drivers.
- No existing GLM schemas, relationships, API, or visualization code to reconcile.
- Legacy corpus schema (columns observed) informs the migration metadata contract only.

## 3. CDG architecture mapping

Semantic layer (frozen): 13 entities (Subject, CurriculumFramework, CurriculumItem,
KnowledgeComponent, TaskModel, Method, Item, Misconception, Claim, EvidenceItem,
Source, Agent, Activity) and 11 relations (isChildOf, mapsTo, alignsTo, broader,
targets, hasMethod, requires, prerequisite, precedes, relatedMisconception, indicates).

Implementation layer (this bootstrap): a typed, in-memory Python domain model +
validation engine + pytest contract tests + developer docs. A `CDGStore` holds draft
records; `authoritative` status is derivable but the frozen CDG version snapshot rules
(§10 invariant 24) are modeled as a version stamp on every record.

## 4. Storage decision

Decision: **in-memory typed domain model + JSON-serializable records**, no external
database. Rationale: frozen v0.2 semantics are expressible as typed records and pure
validators; no persistence/scale requirement exists in this phase; introducing a graph,
vector, document, or relational DB would contradict "use the project's existing
technology" and add unjustified dependencies. Serialization round-trip to JSON preserves
future portability to any store chosen later.

## 5. Schema strategy

- Python dataclasses + Enums in the `cdg` package are the machine-readable contracts.
- Every domain relation instance is modeled as exactly one `Claim` (Sanity Check §3),
  carrying domain/range types, qualifiers, origin, purpose, scope, etc.
- Entities carry `status`, lifecycle metadata, `legacy_id`, and provenance (`created_by`).
- A method-evaluation rule function exposes AND-within-Method / OR-across-Methods.

## 6. Validation strategy

A `validate_*` ruleset producing explicit pass/fail with messages for the frozen
invariants (Sanity Check §10): relation domain/range, Method⇒TaskModel ownership,
prerequisite required qualifiers, self-loop rejection, `precedes` never diagnostic,
acyclicity rules (EXACT vs ALL scope), DERIVED reproducibility, UNDERSTAND=ASSERTED,
agent-proposal boundary, acceptance-basis admissibility, entity lifecycle gating,
`indicates` qualifier requirements, migration metadata presence.

## 7. Test strategy

pytest contract tests asserting every validator accepts valid samples and rejects
the corresponding violation, plus AND/OR evaluation tests and a round-trip
serialization test. Run with `python3 -m pytest`.

## 8. Migration strategy (contract only, no data migration)

`MigrationRecord` captures: legacy_id(s), disposition
(MAPPED/SPLIT/MERGED/CONVERTED_TO_TASKMODEL/CONVERTED_TO_METHOD/RETIRED/PENDING_REVIEW),
mapping-rule Activity, target CDG version, INHERITED evidence flag. Legacy archive is
modeled as read-only `Source` records of type LEGACY_DATASET. Full corpus migration is
deferred.

## 9. Visualization boundary

No UI built. The store exposes a documented view/projection (`export_view`) suitable
for future rendering of curriculum hierarchy, KCs, dependencies, TaskModels/Methods,
cross-subject links, and evidence. Views consume the domain model; they are never the
source of truth.

## 10. Risks / conflicts

- FREEZE doc missing (see §0). All semantics inherit from the Sanity Check.
- One open sign-off item: domain of `indicates`. Sanity Check recommends Item →
  Misconception/KC with required `response_pattern`; we adopt that as a *recorded
  assumption*, flagged for owner confirmation.
- Frozen brief's entity list and the Sanity Check's "12 entities" count differ by one
  (13 named entities). We support the 13 named ones and flag the count.
- Status representation: brief says "status lifecycle specified by CDG v0.2"; we adopt
  the Sanity Check's state machine + acceptance_bases representation as the contract and
  flag it as the adopted interpretation.
- `origin` field for prerequisites is required by the Sanity Check; the brief does not
  mention it — included as contract-level requirement with flag.

## 11. Files to create/change

Create (new):
- `cdg/__init__.py`, `cdg/enums.py`, `cdg/entities.py`, `cdg/relationships.py`,
  `cdg/prerequisites.py`, `cdg/methods.py`, `cdg/claims.py`, `cdg/evidence.py`,
  `cdg/provenance.py`, `cdg/status.py`, `cdg/migration.py`, `cdg/store.py`,
  `cdg/validation.py`, `cdg/serialization.py`
- `tests/test_*.py` (contract + invariant tests)
- `docs/architecture/*.md` (this plan, assessment, contract documentation, status note)
- `README.md`, `pyproject.toml` (minimal, pytest config)

Change: none (repo contained no GLM code).

## 12. Explicit assumptions

1. Sanity Check document stands in for the missing FREEZE spec (owner-confirmed).
2. `indicates` domain/range = Item → Misconception or KC with required
   `response_pattern` (and `polarity` for KCs) — recorded assumption, not silent invention.
3. `origin ∈ {ASSERTED, DERIVED}` is part of prerequisite qualifiers.
4. Prerequisite scope vocabulary: ALL_RELEVANT_METHODS | SPECIFIC_METHOD |
   SPECIFIC_TASK_MODEL, with a referenced id for the latter two; the brief's terms are
   used (sanity-check "ALL" ≡ ALL_RELEVANT_METHODS, "METHOD:X" ≡ SPECIFIC_METHOD,
   "TASK_MODEL:T" ≡ SPECIFIC_TASK_MODEL).
5. UNDERSTAND permits scope ALL_RELEVANT_METHODS or SPECIFIC_TASK_MODEL only.
6. Every domain relationship instance is exactly one Claim; entities also carry their
   own lifecycle status.
7. Cross-subject shared KCs: no ownership decision made; only the constraint that the
   model does not prevent them (opaque KC ids, `subject` as a versioned attribute).
