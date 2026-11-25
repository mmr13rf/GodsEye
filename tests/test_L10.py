import pytest
from layers.L10.monitoring_feedback import MonitoringFeedback

def test_record_and_summary():
    m = MonitoringFeedback()
    m.record({"is_threat": True, "action": "block"})
    m.record({"is_threat": False, "action": "monitor"})
    s = m.summary()
    assert s["events"] == 2
    assert s["alerts"] == 1
    assert s["blocks"] == 1
    assert s["alert_rate"] == 0.5
    assert s["block_rate"] == 0.5

def test_invalid_event():
    m = MonitoringFeedback()
    with pytest.raises(ValueError):
        m.record("bad")

def test_empty_summary():
    m = MonitoringFeedback()
    s = m.summary()
    assert s["events"] == 0
    assert s["alert_rate"] == 0.0
