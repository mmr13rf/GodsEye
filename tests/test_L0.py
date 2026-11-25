from layers.L0.telemetry import TelemetryCollector
from layers.L0.normalizer import Normalizer

def test_normalize_event():
    collector = TelemetryCollector()
    normalizer = Normalizer()
    event = collector.collect({"event_type": "alert", "src_ip": "1.1.1.1", "protocol": "TCP"})
    normalized = normalizer.normalize(event)
    assert normalized["protocol"] == "tcp"
    assert normalized["src_ip"] == "1.1.1.1"
