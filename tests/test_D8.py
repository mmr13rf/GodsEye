import pytest
from engines.D8.onnx_engine import OnnxEngine

def test_threat_detected():
    e = OnnxEngine(threshold=0.5)
    r = e.evaluate({"score": 0.7})
    assert r["is_threat"] is True
    assert r["severity"] == "high"

def test_no_threat():
    e = OnnxEngine(threshold=0.5)
    r = e.evaluate({"score": 0.3})
    assert r["is_threat"] is False
    assert r["severity"] == "low"

def test_invalid_threshold():
    with pytest.raises(ValueError):
        OnnxEngine(threshold=1.5)

def test_invalid_score():
    e = OnnxEngine()
    with pytest.raises(ValueError):
        e.evaluate({"score": 2.0})
