import pytest
from engines.D7.cnn_lstm_engine import CnnLstmEngine

def test_anomaly_detected():
    e = CnnLstmEngine(threshold=100)
    r = e.evaluate({"avg_packet_size": 200})
    assert r["is_anomaly"] is True
    assert r["severity"] == "high"

def test_no_anomaly():
    e = CnnLstmEngine(threshold=100)
    r = e.evaluate({"avg_packet_size": 50})
    assert r["is_anomaly"] is False
    assert r["severity"] == "low"

def test_invalid_threshold():
    with pytest.raises(ValueError):
        CnnLstmEngine(threshold=0)

def test_invalid_analysis():
    e = CnnLstmEngine()
    with pytest.raises(ValueError):
        e.evaluate("bad")
