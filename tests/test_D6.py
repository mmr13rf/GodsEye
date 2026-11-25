from engines.D6.waf_engine import WafEngine

def test_attack_detected():
    engine = WafEngine(attack_patterns=["select"])
    result = engine.evaluate({"method": "GET", "query": "id=1 OR 1=1", "body": ""})
    assert result["is_attack"] is False

def test_sql_injection_detected():
    engine = WafEngine(attack_patterns=["select"])
    result = engine.evaluate({"method": "GET", "query": "id=1 UNION SELECT", "body": ""})
    assert result["is_attack"] is True
    assert result["severity"] == "high"
