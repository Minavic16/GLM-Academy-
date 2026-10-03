import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest

from cdg import *
from cdg.claims import Claim
from cdg.entities import (
    CurriculumFramework,
    CurriculumItem,
    Item,
    KnowledgeComponent,
    Method,
    Misconception,
    Subject,
    TaskModel,
)
from cdg.enums import *
from cdg.evidence import EvidenceItem
from cdg.migration import MigrationRecord
from cdg.provenance import Activity, Agent, Source
from cdg.store import CDGStore
from cdg.validation import *
from cdg.serialization import dumps_store, to_json  # noqa: F401


def make_store() -> CDGStore:
    s = CDGStore()
    s.add_agent(Agent(id="agent.human", kind=AgentKind.HUMAN, name="Reviewer"))
    s.add_agent(Agent(id="agent.ai", kind=AgentKind.AI_AGENT, name="ResearchAgent", model_or_version="glm-r1"))
    s.add_activity(Activity(id="act.extract", type=ActivityType.EXTRACTION, agent_id="agent.ai", time="2026-10-01T00:00:00Z"))
    s.add_activity(Activity(id="act.review", type=ActivityType.REVIEW, agent_id="agent.human", time="2026-10-02T00:00:00Z"))
    s.add_source(Source(id="src.jamb", title="JAMB UTME Maths Syllabus", identifier_or_url="https://…", publisher="JAMB", source_type=SourceType.SYLLABUS, tier="primary"))

    s.add_entity(Subject(id="subj.math", label="Mathematics"))
    fw = CurriculumFramework(id="fw.jamb.maths", label="JAMB UTME Mathematics", publisher="JAMB")
    s.add_entity(fw)
    ci1 = CurriculumItem(id="ci.1", framework_id="fw.jamb.maths", verbatim_text="Number bases", label="Number bases")
    s.add_entity(ci1)
    s.add_entity(KnowledgeComponent(id="kc.place_value", label="Place value", subject="Mathematics"))
    s.add_entity(KnowledgeComponent(id="kc.base_numerals", label="Base-b numerals", subject="Mathematics"))
    s.add_entity(TaskModel(id="tm.1", label="Convert bases"))
    s.add_entity(Method(id="m.1", label="Repeated division", task_model_id="tm.1"))
    s.add_entity(Item(id="it.1", task_model_id="tm.1", stem="Convert 25 to base 2", options=["11001", "10011"], key="11001"))
    s.add_entity(Misconception(id="mis.1", label="Confuses base with exponent"))
    return s
