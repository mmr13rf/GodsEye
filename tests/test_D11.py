import pytest
from engines.D11.monitoring_feedback_engine import MonitoringFeedbackEngine

def test_healthy_status():
    e = MonitoringFeedbackEngine(alert_threshold=0.2)
    r = e.evaluate({"alert_rate": 0.1})
    assert r["status"] == "healthy"

def test_critical_status():
    e = MonitoringFeedbackEngine(alert_threshold=0.2)
    r = e.evaluate({"alert_rate": 0.5})
    assert r["status"] == "critical"

def test_invalid_threshold():
    with pytest.raises(ValueError):
        MonitoringFeedbackEngine(alert_threshold=1.5)

def test_invalid_summary():
    e = MonitoringFeedbackEngine()
    with pytest.raises(ValueError):
        e.evaluate("bad")
