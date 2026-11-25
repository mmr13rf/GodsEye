import pytest
from layers.L9.response_enforcement import ResponseEnforcement

def test_monitor_mode():
    r = ResponseEnforcement(mode="monitor")
    result = r.respond({"is_threat": True})
    assert result["action"] == "monitor"

def test_enforce_mode():
    r = ResponseEnforcement(mode="enforce")
    result = r.respond({"is_threat": True})
    assert result["action"] == "block"

def test_invalid_mode():
    with pytest.raises(ValueError):
        ResponseEnforcement(mode="bad")

def test_invalid_decision():
    r = ResponseEnforcement()
    with pytest.raises(ValueError):
        r.respond("bad")
