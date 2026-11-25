from engines.D4.threat_intel_engine import ThreatIntelEngine

def test_threat_detected():
    engine = ThreatIntelEngine()
    result = engine.evaluate({"src_ip_malicious": True, "dest_ip_malicious": False})
    assert result["is_threat"] is True
    assert result["severity"] == "high"

def test_no_threat():
    engine = ThreatIntelEngine()
    result = engine.evaluate({"src_ip_malicious": False, "dest_ip_malicious": False})
    assert result["is_threat"] is False
    assert result["severity"] == "low"
