"""Batch 011 — Number foundations: fractions/decimals/percentages."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch10_simultaneous_lq import build_graph_v10
from examples._batchkit import accept, ev

B_REVIEW = "act.batch11.review"
B_INTERP = "act.batch11.interpret"


def build_graph_v11() -> CDGStore:
    s = build_graph_v10()
    s.add_activity(Activity(id="act.batch11.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T20:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T20:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T21:00:00Z",
                            rationale="Human review of number-foundations batch."))
    if "SRC.NMAP.2008" not in s.sources:
        s.add_source(Source(id="SRC.NMAP.2008", title="The National Mathematics Advisory Panel Foundational Skills Report (2008)",
                            identifier_or_url="legacy:SRC.NMAP.2008", publisher="NMAP",
                            source_type=SourceType.PAPER, tier="reference"))
    for kid, label, definition, legacy, status in [
        ("kc.fraction_decimal_operations", "Operations on fractions and decimals",
         "Add, subtract, multiply and divide fractions and decimals.", "MATH.NUM.FRACTION_DECIMAL_OPERATIONS", ClaimStatus.ACCEPTED),
        ("kc.percentage_concept", "Percentages",
         "Interpret and compute with percentages; percentage change.", "MATH.NUM.PERCENTAGE_CONCEPT", ClaimStatus.ACCEPTED),
    ]:
        k = KnowledgeComponent(id=kid, label=label, definition=definition, subject="Mathematics",
                               status=status, legacy_ids=[legacy], created_by_activity=B_INTERP,
                               cdg_version="v0.2.0")
        k.reviewed_by_activity = B_REVIEW
        s.add_entity(k)
    tmF = TaskModel(id="tm.fraction_decimal_operations", label="Perform operations on fractions/decimals",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmF.reviewed_by_activity = B_REVIEW
    mF = Method(id="m.convert_common_denominator", label="Convert to common denominator and operate",
                task_model_id=tmF.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mF.reviewed_by_activity = B_REVIEW
    tmP = TaskModel(id="tm.percentage_problems", label="Solve percentage problems",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmP.reviewed_by_activity = B_REVIEW
    mP = Method(id="m.percent_as_fraction", label="Write percent as a fraction/decimal and multiply",
                task_model_id=tmP.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mP.reviewed_by_activity = B_REVIEW
    for e in (tmF, mF, tmP, mP): s.add_entity(e)
    it = Item(id="it.mcq.percentage", label="MCQ: percentage", task_model_id=tmP.id,
              stem="Express 45 out of 60 as a percentage", options=["75%", "60%", "45%", "15%"],
              key="75%", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T20:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm11F.target", RelationshipType.TARGETS, tmF.id, "kc.fraction_decimal_operations",
        ClaimType.ASSESSMENT_DESIGN, "targets fraction/decimal operations", ASSESS)
    add("cl.tm11P.target", RelationshipType.TARGETS, tmP.id, "kc.percentage_concept",
        ClaimType.ASSESSMENT_DESIGN, "targets percentages", ASSESS)
    add("cl.tm11F.m1", RelationshipType.HAS_METHOD, tmF.id, mF.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm11P.m1", RelationshipType.HAS_METHOD, tmP.id, mP.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.req11F.int", RelationshipType.REQUIRES, mF.id, "kc.integer_arithmetic",
        ClaimType.DEPENDENCY, "fraction ops require integer arithmetic", DEP)
    add("cl.req11P.frac", RelationshipType.REQUIRES, mP.id, "kc.fraction_decimal_operations",
        ClaimType.DEPENDENCY, "percent problems require fraction ops", DEP)
    add("cl.req11P.int", RelationshipType.REQUIRES, mP.id, "kc.integer_arithmetic",
        ClaimType.DEPENDENCY, "percent problems require integer arithmetic", DEP)
    add("cl.pre11.frac_pct", RelationshipType.PREREQUISITE, "kc.fraction_decimal_operations",
        "kc.percentage_concept", ClaimType.DEPENDENCY, "EXECUTE, whole TM", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tmP.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre11.int_frac", RelationshipType.PREREQUISITE, "kc.integer_arithmetic",
        "kc.fraction_decimal_operations", ClaimType.DEPENDENCY, "EXECUTE, whole TM", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tmF.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b11.tF", "cl.tm11F.target", "SRC.NMAP.2008", "E0019",
                      "Fractions (including decimals, percent, and negative fractions).", True, B_INTERP))
    s.add_evidence(ev("ev.b11.tP", "cl.tm11P.target", "SRC.JAMB.UTME.MATH", "E0020",
                      "Fractions, decimals and percentages are grouped in one topic.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.mF", "cl.tm11F.m1", "SRC.NMAP.2008", "E0019", "Operations on fractions.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.mP", "cl.tm11P.m1", "SRC.JAMB.UTME.MATH", "E0020", "Percent as fraction.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.r1", "cl.req11F.int", "SRC.NMAP.2008", "E0019", "Built on whole-number arithmetic.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.r2", "cl.req11P.frac", "SRC.JAMB.UTME.MATH", "E0020", "Percent as fraction/decimal.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.r3", "cl.req11P.int", "SRC.NMAP.2008", "E0019", "Requires integer arithmetic.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.p1", "cl.pre11.frac_pct", "SRC.JAMB.UTME.MATH", "E0019", "Fractions precede percentages.", True, B_INTERP))
    s.add_evidence(ev("ev.b11.p2", "cl.pre11.int_frac", "SRC.NMAP.2008", "E0019", "Whole numbers precede fraction ops.", True, B_INTERP))
    return s
