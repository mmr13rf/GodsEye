import pytest
from engines.D3.behavioral_engine import BehavioralEngine

def test_behavioral_engine():
    engine = BehavioralEngine(threshold=0.5)
    result = engine.evaluate({"port_diversity": 0.8})
    assert result["is_suspicious"] is True

def test_invalid_threshold():
    with pytest.raises(ValueError):
        BehavioralEngine(threshold=2.0)
