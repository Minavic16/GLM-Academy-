# GLM CDG v0.2 — Contract Documentation

This document describes how to use the bootstrap contracts in the `cdg` package.
Semantics come from the frozen v0.2 model as reviewed in
`GLM_CDG_v0.2_Contract_Sanity_Check.md` (the FREEZE doc itself is missing; see
`IMPLEMENTATION_PLAN.md` §0).

## Creating an entity

```python
from cdg.entities import KnowledgeComponent, TaskModel, Method, Item
kc = KnowledgeComponent(id="kc.001", label="Signed-number arithmetic",
                        subject="Mathematics")
```

- `id` must be opaque and must NOT encode the subject (e.g. no `MATH.*` prefix).
- `subject` is a versioned attribute that may be re-homed later.
- Entities start with `status=ClaimStatus.PROPOSED` and carry provenance fields
  (`created_by_activity`, `created_at`, `cdg_version`, `legacy_ids`).
- A KC may leave PROPOSED only when at least one TaskModel targets it
  (`validate_kc_lifecycle`).

## Creating a relationship

Every domain relationship instance is exactly one `Claim`:

```python
from cdg.claims import Claim
from cdg.enums import ...
Claim(
    id="cl.001", predicate=RelationshipType.REQUIRES,
    subject_id="m.001", object_id="kc.001",
    claim_type=ClaimType.DEPENDENCY,
    qualifiers={}, created_by_activity="act.extraction.1",
)
```

Validators enforce explicit domain/range for every predicate, required
qualifiers (`match`, `alignment`, `purpose`/`scope`/`origin`, `response_pattern`,
`polarity`), and self-loop prohibition (`prerequisite`, `broader`, `precedes`,
`isChildOf`).

## TaskModel with multiple Methods (AND / OR)

```python
tm = TaskModel(id="tm.1", ...)
ma = Method(id="m.A", task_model_id="tm.1")
mb = Method(id="m.B", task_model_id="tm.1")
# requires edges: m.A -> kc1, kc2, kc3 ; m.B -> kc4, kc5
from cdg.methods import evaluate_task_model
satisfied = evaluate_task_model([["kc1","kc2","kc3"], ["kc4","kc5"]],
                                satisfied_kcs={"kc4", "kc5"})
```

Rule: within a Method, required KCs are ANDed; across Methods of the same
TaskModel, Methods are ORed. A Method belongs to exactly one TaskModel; the same
strategy reused elsewhere is a separate Method record with the same label.

## Prerequisite purpose/scope/origin

`Claim.predicate == PREREQUISITE` requires all three qualifiers:

- `purpose`: EXECUTE or UNDERSTAND
- `scope`: ALL_RELEVANT_METHODS | SPECIFIC_METHOD | SPECIFIC_TASK_MODEL
  (`scope_ref` names the method/task model for the specific scopes)
- `origin`: ASSERTED or DERIVED

Rules enforced by validators:

- EXECUTE + SPECIFIC_METHOD/SPECIFIC_TASK_MODEL ⇒ origin must be DERIVED
  (these are computed from `requires`; never hand-asserted).
- EXECUTE + ALL_RELEVANT_METHODS may be ASSERTED (hypothesis) or DERIVED
  (computed as: the KC is required by every Method of every TaskModel targeting
  the object KC — see `derive_all_scope_execute_prerequisites`).
- UNDERSTAND ⇒ always ASSERTED, scope ALL_RELEVANT_METHODS or SPECIFIC_TASK_MODEL.
- No cycles among EXECUTE/ALL prerequisites (acyclicity validator).
- No extra classifications may be added.

## `precedes` and diagnostics

`precedes` is a soft navigation/documentation relation only.
`CDGStore.diagnostic_prerequisite_claims()` never returns it, and it must not be
consumed by diagnostic logic. Vector similarity output is likewise never a
source of authoritative graph truth — it may only contribute PROPOSAL candidates.

## Evidence and provenance

```python
EvidenceItem(id=..., claim_id=..., source_id=..., role=..., stance=...,
             locator=..., excerpt=..., excerpt_kind=ExcerptKind.VERBATIM,
             extracted_by_activity=..., inherited_from_legacy=False)
```

- EvidenceItems are immutable frozen dataclasses; corrections create new records.
- Learner responses are NOT EvidenceItems; they are learner-model Observations
  (outside this contract) and may reach a Claim only via a cited Source with role
  EMPIRICAL_LEARNER.
- Agent reasoning may PROPOSE; it never silently validates. A Claim cannot reach
  ACCEPTED when its only support has role AGENT_INFERENCE.

## Status lifecycle

```
PROPOSED → UNDER_REVIEW → ACCEPTED | REJECTED | CONTESTED
CONTESTED → UNDER_REVIEW
ACCEPTED → DEPRECATED   (only via a superseding record)
```

- Transitions are enforced by `validate_status_transition`.
- ACCEPTED requires: an admissible `acceptance_basis` for the claim's type, and a
  HUMAN review Activity (or documented rationale for leaving PROPOSED).
- Each status change is recorded as a REVIEW Activity.

## Entity types and closure

The frozen entity set is the only one supported. Note: the task brief lists 13
entity names while the sanity-check review text says "12 frozen entities" — this
bootstrap supports the 13 named ones and flags the counting difference as an open
question. `indicates` uses the recommended interpretation:
Item → Misconception|KC, required `response_pattern` (and `polarity` for KC
targets), pending explicit owner sign-off (marked
**OWNER_SIGN_OFF_REQUIRED**). It must not be broadened without an owner decision.

## Legacy records

No full migration is performed. The contract is `MigrationRecord`:
`legacy_ids`, `disposition` (MAPPED/SPLIT/MERGED/CONVERTED_TO_TASKMODEL/
CONVERTED_TO_METHOD/RETIRED/PENDING_REVIEW), the MIGRATION Activity, mapping
rule, target CDG version, and new record ids. Legacy evidence that is carried
over becomes an EvidenceItem flagged `inherited_from_legacy` and must be
re-reviewed. The legacy corpus is stored as read-only `Source` records of type
LEGACY_DATASET.

## Cross-subject use

Mathematics, Physics, and Chemistry share the same ontology through `subject`
attributes and opaque KC ids. Shared concepts across subjects are referenced, not
duplicated, and the contract deliberately does not decide ownership of shared KCs.
