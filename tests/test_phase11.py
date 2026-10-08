import json, subprocess, os

def test_subject_identity_preserved_roundtrip():
    from examples.wave2_batches import build_graph_v29
    from cdg.serialization import dumps_store
    s = build_graph_v29()
    # every KC carries a subject attribute; Mathematics is explicit
    subjects = {e.subject for e in s.entities.values()}
    assert "Mathematics" in subjects
    blob = dumps_store(s)
    assert '"subject": "Mathematics"' in blob

def test_cross_subject_prerequisite_validates():
    from cdg.validation import validate_relationship_claim
    from cdg.claims import Claim
    from cdg.enums import RelationshipType, ClaimType, PrerequisitePurpose, PrerequisiteScope, ClaimOrigin, ClaimStatus
    from conftest import make_store
    s = make_store()
    # add a physics KC
    from cdg.entities import KnowledgeComponent
    s.add_entity(KnowledgeComponent(id="kc.newtons_second_law", label="Newton's second law", subject="Physics"))
    c = Claim(id="cl.xsub", predicate=RelationshipType.PREREQUISITE, subject_id="kc.place_value",
              object_id="kc.newtons_second_law", claim_type=ClaimType.DEPENDENCY,
              purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
              origin=ClaimOrigin.ASSERTED, created_by_activity="act.extract")
    assert validate_relationship_claim(c, s.entities) == []

def test_viz_deterministic():
    import hashlib
    def sha(p):
        return hashlib.sha256(open(p, 'rb').read()).hexdigest()
    a = sha('docs/visualizations/mathematics_full.svg')
    subprocess.run(['python3', 'tools/generate_cdg_visualization.py'], check=True, cwd=os.path.dirname(os.path.dirname(__file__)))
    b = sha('docs/visualizations/mathematics_full.svg')
    assert a == b

def test_viz_node_edge_resolution():
    import json
    data = json.load(open('examples/math_cdg_v2.json'))
    ids = {e['id'] for e in data['entities']}
    svg = open('docs/visualizations/mathematics_full.svg').read()
    for i in ids:
        assert f'<g class="node" data-id="{i}"' in svg, i
    # every canonical claim appears as an SVG edge with its predicate in the title
    for c in data['claims']:
        if c['predicate'] and c['object_id'] in ids:
            assert f'({c["id"]})' in svg


def test_viz_clickable_cards_and_details():
    import json
    data = json.load(open('examples/math_cdg_v2.json'))
    html = open('docs/visualizations/mathematics_full.html').read()
    # every node is a clickable card
    ids = {e['id'] for e in data['entities']}
    for i in ids:
        assert f"cdgSelect('{i}', event)" in html, i
    # connections and prerequisites survive into the interactive payload
    assert 'purpose' in html and 'scope' in html and 'origin' in html
    assert 'legacy_id' in html and 'excerpt' in html
    assert 'other' in html and 'predicate' in html


def test_mathematics_backward_compatibility():
    from examples.wave2_batches import build_graph_v29
    from cdg.validation import run_store_validation
    assert run_store_validation(build_graph_v29()) == []
