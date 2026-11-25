import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.realtime_pipeline import RealTimePipeline
from engines.D7.cnn_lstm_engine import CnnLstmEngine
from engines.D8.onnx_engine import OnnxEngine


def test_realtime_pipeline_monitor_only():
    pipeline = RealTimePipeline()
    event = {"method": "GET", "path": "/", "query": "id=1 UNION SELECT * FROM users", "headers": {}, "body": ""}
    result = pipeline.process(event)
    assert result["is_attack"] is True
    assert result["action"] == "monitor"
    assert result["mode"] == "monitor-only"


def test_realtime_pipeline_block_with_enforce():
    pipeline = RealTimePipeline(enforce=True)
    event = {"method": "GET", "path": "/", "query": "id=1 UNION SELECT * FROM users", "headers": {}, "body": ""}
    result = pipeline.process(event)
    assert result["action"] == "block"


def test_cnn_lstm_safe_fallback():
    engine = CnnLstmEngine()
    result = engine.run({})
    assert result["action"] == "monitor"


def test_onnx_safe_fallback():
    engine = OnnxEngine()
    result = engine.run({})
    assert result["action"] == "monitor"
