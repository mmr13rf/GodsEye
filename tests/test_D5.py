from engines.D5.dns_tls_engine import DnsTlsEngine

def test_suspicious_domain():
    engine = DnsTlsEngine(suspicious_domains=["bad.com"])
    result = engine.evaluate({"dns_query": "bad.com", "tls_sni": ""})
    assert result["is_suspicious"] is True
    assert result["severity"] == "high"

def test_normal_domain():
    engine = DnsTlsEngine(suspicious_domains=["bad.com"])
    result = engine.evaluate({"dns_query": "example.com", "tls_sni": "example.com"})
    assert result["is_suspicious"] is False
    assert result["severity"] == "low"
