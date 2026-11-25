import pytest
from engines.D10.response_enforcement_engine import ResponseEnforcementEngine

def test_monitor_action():
    e = ResponseEnforcementEngine(mode="monitor")
    r = e.evaluate({"action": "monitor"})
    assert r["final_action"] == "monitor"

def test_block_action():
    e = ResponseEnforcementEngine(mode="enforce")
    r = e.evaluate({"action": "block"})
    assert r["final_action"] == "block"

def test_invalid_mode():
    with pytest.raises(ValueError):
        ResponseEnforcementEngine(mode="bad")

def test_invalid_action():
    e = ResponseEnforcementEngine()
    with pytest.raises(ValueError):
        e.evaluate({"action": "bad"})
