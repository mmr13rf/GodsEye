import pytest
from engines.D9.decision_fusion_engine import DecisionFusionEngine

def test_threat_detected():
    e = DecisionFusionEngine(threshold=0.5)
    r = e.evaluate({"score": 0.7})
    assert r["is_threat"] is True
    assert r["severity"] == "high"

def test_no_threat():
    e = DecisionFusionEngine(threshold=0.5)
    r = e.evaluate({"score": 0.3})
    assert r["is_threat"] is False
    assert r["severity"] == "low"

def test_invalid_threshold():
    with pytest.raises(ValueError):
        DecisionFusionEngine(threshold=1.5)

def test_invalid_fusion():
    e = DecisionFusionEngine()
    with pytest.raises(ValueError):
        e.evaluate("bad")
