import pytest
from engines.D1.rule_engine import RuleEngine

def test_rule_match():
    engine = RuleEngine()
    event = {"src_ip": "203.0.113.10"}
    hits = engine.evaluate(event)
    assert hits[0]["rule_id"] == "R001"

def test_invalid_event():
    engine = RuleEngine()
    with pytest.raises(ValueError):
        engine.evaluate("invalid")
