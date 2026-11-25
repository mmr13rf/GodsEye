from layers.L3.threat_intel import ThreatIntel

def test_check_ip():
    ti = ThreatIntel(malicious_ips=["203.0.113.10"])
    assert ti.check_ip("203.0.113.10") is True
    assert ti.check_ip("8.8.8.8") is False

def test_analyze():
    ti = ThreatIntel(malicious_ips=["203.0.113.10"])
    result = ti.analyze({"src_ip": "203.0.113.10", "dest_ip": "8.8.8.8"})
    assert result["src_ip_malicious"] is True
    assert result["dest_ip_malicious"] is False
