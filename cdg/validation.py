"""Machine-testable validation of the frozen CDG v0.2 invariants."""
from __future__ import annotations

from typing import List, Optional, Set

from .claims import Claim
from .entities import EntityBase, Item, KnowledgeComponent, Method, TaskModel
from .enums import (
    AcceptanceBasis,
    ActivityType,
    AgentKind,
    ClaimOrigin,
    ClaimStatus,
    ClaimType,
    EntityType,
    EvidenceRole,
    MatchQualifier,
    AlignmentQualifier,
    PrerequisitePurpose,
    PrerequisiteScope,
    RelationshipType,
)
from .relationships import (
    NO_SELF_LOOP,
    RELATIONSHIP_DOMAIN_RANGE,
    REQUIRED_QUALIFIERS,
)
from .status import ADMISSIBLE_ACCEPTANCE_BASES, transition_allowed


def v(msg: str) -> str:
    return msg


# ---------- structural / relational ----------

def validate_relationship_claim(c: Claim, entities: dict[str, EntityBase]) -> List[str]:
    errs: List[str] = []
    if c.predicate is None:
        return errs
    if c.subject_id not in entities or (c.object_id and c.object_id not in entities):
        return [f"{c.id}: endpoint missing from store"]
    src = entities[c.subject_id]
    dst = entities[c.object_id] if c.object_id else None
    if dst is None:
        return [f"{c.id}: relationship requires a target entity"]

    if c.predicate == RelationshipType.PRECEDES:
        if src.entity_type != dst.entity_type:
            errs.append(f"{c.id}: precedes endpoints must be the same type")
        if src.entity_type not in (EntityType.KNOWLEDGE_COMPONENT, EntityType.CURRICULUM_ITEM):
            errs.append(f"{c.id}: precedes only connects KC-KC or CurriculumItem-CurriculumItem")
    else:
        dom, rng = RELATIONSHIP_DOMAIN_RANGE[c.predicate]
        if src.entity_type != dom:
            errs.append(f"{c.id}: {c.predicate.value} domain must be {dom.value}, got {src.entity_type.value}")
        if dst.entity_type not in rng:
            errs.append(f"{c.id}: {c.predicate.value} range must be {sorted(t.value for t in rng)}, got {dst.entity_type.value}")

    if c.predicate in NO_SELF_LOOP and c.subject_id == c.object_id:
        errs.append(f"{c.id}: self-loop not allowed for {c.predicate.value}")

    for q in REQUIRED_QUALIFIERS.get(c.predicate, ()):
        if q == "purpose" and c.purpose is None:
            errs.append(f"{c.id}: prerequisite requires 'purpose'")
        elif q == "scope" and c.scope is None:
            errs.append(f"{c.id}: prerequisite requires 'scope'")
        elif q == "origin" and c.origin is None:
            errs.append(f"{c.id}: prerequisite requires 'origin'")
        elif q in ("match", "alignment", "response_pattern") and q not in c.qualifiers:
            errs.append(f"{c.id}: {c.predicate.value} requires qualifier '{q}'")

    if c.predicate == RelationshipType.MAPS_TO:
        if c.subject_id in entities and c.object_id in entities:
            if entities[c.subject_id].framework_id == entities[c.object_id].framework_id:
                errs.append(f"{c.id}: mapsTo must connect items in different frameworks")
        if "match" in c.qualifiers:
            try:
                MatchQualifier(c.qualifiers["match"])
            except ValueError:
                errs.append(f"{c.id}: invalid match qualifier {c.qualifiers['match']!r}")

    if c.predicate == RelationshipType.ALIGNS_TO and "alignment" in c.qualifiers:
        try:
            AlignmentQualifier(c.qualifiers["alignment"])
        except ValueError:
            errs.append(f"{c.id}: invalid alignment qualifier {c.qualifiers['alignment']!r}")

    if c.predicate == RelationshipType.INDICATES and dst.entity_type == EntityType.KNOWLEDGE_COMPONENT:
        if "polarity" not in c.qualifiers:
            errs.append(f"{c.id}: indicates->KC requires 'polarity' qualifier")

    if c.predicate == RelationshipType.PREREQUISITE:
        errs.extend(validate_prerequisite_attributes(c, entities))
    return errs


def validate_prerequisite_attributes(c: Claim, entities: dict[str, EntityBase]) -> List[str]:
    errs: List[str] = []
    if c.purpose is None or c.scope is None or c.origin is None:
        return errs  # already reported
    if c.purpose == PrerequisitePurpose.UNDERSTAND:
        if c.origin != ClaimOrigin.ASSERTED:
            errs.append(f"{c.id}: UNDERSTAND prerequisite must be ASSERTED")
        if c.scope not in (PrerequisiteScope.ALL_RELEVANT_METHODS, PrerequisiteScope.SPECIFIC_TASK_MODEL):
            errs.append(f"{c.id}: UNDERSTAND permits only ALL_RELEVANT_METHODS or SPECIFIC_TASK_MODEL scope")
    else:  # EXECUTE
        if c.scope in (PrerequisiteScope.SPECIFIC_METHOD, PrerequisiteScope.SPECIFIC_TASK_MODEL):
            if c.origin != ClaimOrigin.DERIVED:
                errs.append(f"{c.id}: EXECUTE prerequisite with specific scope must be DERIVED")
            if not c.scope_ref:
                errs.append(f"{c.id}: specific-scope prerequisite requires scope_ref")
        # ALL scope may be ASSERTED or DERIVED.
    return errs


def validate_method_structure(store) -> List[str]:
    errs: List[str] = []
    methods = store.entities_of_type(EntityType.METHOD)
    tms = store.entities_of_type(EntityType.TASK_MODEL)
    items = store.entities_of_type(EntityType.ITEM)

    tm_method_claims = {}
    for c in store.claims_by_predicate(RelationshipType.HAS_METHOD):
        tm_method_claims.setdefault(c.subject_id, set()).add(c.object_id)

    # each Method belongs to exactly one TaskModel
    for m in methods:
        parents = [tm for tm, ms in tm_method_claims.items() if m.id in ms]
        if len(parents) != 1:
            errs.append(f"{m.id}: Method must belong to exactly one TaskModel (found {len(parents)})")
        if m.task_model_id is None:
            errs.append(f"{m.id}: Method missing task_model_id")
        elif parents and parents[0] != m.task_model_id:
            errs.append(f"{m.id}: task_model_id disagrees with hasMethod claims")
        reqs = store.method_required_kcs(m.id)
        if len(reqs) == 0:
            errs.append(f"{m.id}: Method must require at least one KC")

    # each TaskModel: >=1 target, >=1 method
    for tm in tms:
        if len(store.target_kcs_of_task_model(tm.id)) == 0:
            errs.append(f"{tm.id}: TaskModel must target at least one KC")
        if len(tm_method_claims.get(tm.id, set())) == 0:
            errs.append(f"{tm.id}: TaskModel must have at least one Method")

    # each Item belongs to exactly one TaskModel, carries no targets/requires
    item_ids = {i.id for i in items}
    for it in items:
        if it.task_model_id is None:
            errs.append(f"{it.id}: Item must belong to exactly one TaskModel")
    for c in store.claims.values():
        if c.predicate in (RelationshipType.TARGETS, RelationshipType.REQUIRES, RelationshipType.PREREQUISITE):
            if c.subject_id in item_ids:
                errs.append(f"{c.id}: Item may not originate {c.predicate.value} claims")
    return errs


def validate_kc_lifecycle(store) -> List[str]:
    errs: List[str] = []
    for kc in store.entities_of_type(EntityType.KNOWLEDGE_COMPONENT):
        if kc.status != ClaimStatus.PROPOSED and not store.targeting_task_models(kc.id):
            errs.append(f"{kc.id}: KC cannot leave PROPOSED without a targeting TaskModel")
    return errs


def validate_status_transition(
    claim: Claim,
    new_status: ClaimStatus,
    evidence_roles: Set[EvidenceRole],
    review_is_human: bool,
    has_rationale: bool = False,
) -> List[str]:
    errs: List[str] = []
    if not transition_allowed(claim.status, new_status):
        return [f"{claim.id}: illegal transition {claim.status.value} -> {new_status.value}"]
    if new_status != ClaimStatus.PROPOSED and not (evidence_roles or has_rationale):
        errs.append(f"{claim.id}: moving to {new_status.value} requires evidence or rationale")
    if new_status == ClaimStatus.ACCEPTED:
        admissible = ADMISSIBLE_ACCEPTANCE_BASES[claim.claim_type]
        if not (set(claim.acceptance_bases) & admissible):
            errs.append(f"{claim.id}: ACCEPTED requires an admissible acceptance basis")
        if not review_is_human:
            errs.append(f"{claim.id}: ACCEPTED requires a HUMAN review Activity")
        if evidence_roles and evidence_roles <= {EvidenceRole.AGENT_INFERENCE}:
            errs.append(f"{claim.id}: ACCEPTED impossible with only AGENT_INFERENCE support")
    return errs


def validate_agent_proposal(agent_kind: AgentKind, claim: Claim) -> List[str]:
    errs: List[str] = []
    if agent_kind == AgentKind.AI_AGENT:
        if claim.status != ClaimStatus.PROPOSED:
            errs.append(f"{claim.id}: agent proposals must enter as PROPOSED")
        if claim.created_by_activity is None:
            errs.append(f"{claim.id}: agent proposal needs an creating Activity")
    return errs


def validate_acyclicity(edges: List[tuple[str, str]]) -> bool:
    """Returns True if the graph is acyclic. Used for EXACT mapsTo, ALL-scope
    EXECUTE prerequisites, broader, and isChildOf."""
    from collections import defaultdict

    adj = defaultdict(list)
    nodes = set()
    for a, b in edges:
        adj[a].append(b)
        nodes.add(a)
        nodes.add(b)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in nodes}

    def dfs(n) -> bool:
        color[n] = GRAY
        for m in adj[n]:
            if color[m] == GRAY:
                return False
            if color[m] == WHITE and not dfs(m):
                return False
        color[n] = BLACK
        return True

    return all(dfs(n) for n in list(nodes) if color[n] == WHITE)


def validate_ischildof_tree(store, framework_entities) -> List[str]:
    errs: List[str] = []
    parents: dict[str, str] = {}
    for c in store.claims_by_predicate(RelationshipType.IS_CHILD_OF):
        if c.subject_id in parents:
            errs.append(f"{c.subject_id}: CurriculumItem has more than one parent")
        parents[c.subject_id] = c.object_id
        a, b = store.entities[c.subject_id], store.entities[c.object_id]
        if getattr(a, "framework_id", None) != getattr(b, "framework_id", None):
            errs.append(f"{c.id}: isChildOf must stay within one framework")
    edges = [(child, parent) for child, parent in parents.items()]
    if not validate_acyclicity(edges):
        errs.append("isChildOf contains a cycle")
    return errs


def validate_migration_record(m) -> List[str]:
    errs: List[str] = []
    if not m.legacy_ids:
        errs.append(f"{m.id}: migration record requires legacy_id(s)")
    if not m.migration_activity_id:
        errs.append(f"{m.id}: migration record requires its MIGRATION Activity")
    if not m.target_cdg_version:
        errs.append(f"{m.id}: migration record requires target CDG version")
    return errs


def run_store_validation(store) -> List[str]:
    errs: List[str] = []
    for c in store.claims.values():
        if c.predicate is not None:
            errs.extend(validate_relationship_claim(c, store.entities))
    errs.extend(validate_method_structure(store))
    errs.extend(validate_kc_lifecycle(store))
    for m in store.migrations.values():
        errs.extend(validate_migration_record(m))
    # EXECUTE prerequisites with scope ALL must be acyclic
    all_scope_exec = [
        (c.subject_id, c.object_id)
        for c in store.claims.values()
        if c.predicate == RelationshipType.PREREQUISITE
        and c.purpose == PrerequisitePurpose.EXECUTE
        and c.scope == PrerequisiteScope.ALL_RELEVANT_METHODS
    ]
    if not validate_acyclicity(all_scope_exec):
        errs.append("cycle among EXECUTE prerequisites with ALL scope")
    errs.extend(validate_ischildof_tree(store, None))
    return errs
