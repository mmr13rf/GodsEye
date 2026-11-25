import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engines.D6.waf_engine import WafEngine


def make(req):
    base = {"method": "GET", "path": "/", "query": "", "headers": {}, "body": ""}
    base.update(req)
    return base


def test_waf_detects_common_web_attacks():
    engine = WafEngine()
    cases = [
        ({"query": "id=1 UNION SELECT * FROM users"}, True),
        ({"query": "q=<script>alert(1)</script>"}, True),
        ({"path": "/download?file=../../etc/passwd"}, True),
        ({"query": "cmd=; cat /etc/passwd"}, True),
        ({"query": "url=http://169.254.169.254/latest/meta-data/"}, True),
        ({"query": "filter=*)(|(objectClass=*)"}, True),
        ({"body": "<!DOCTYPE foo [<!ENTITY xxe SYSTEM \"file:///etc/passwd\">]>"}, True),
        ({"body": "{{7*7}}"}, True),
        ({"query": "next=https://evil.example.com"}, True),
    ]
    for request, expected in cases:
        result = engine.evaluate(make(request))
        assert result["is_attack"] is expected, (request, result)


def test_waf_no_false_positive_on_benign():
    engine = WafEngine()
    result = engine.evaluate(make({"query": "page=2"}))
    assert result["is_attack"] is False
    assert result["score"] == 0.0


def test_waf_defaults_to_monitor():
    engine = WafEngine()
    result = engine.evaluate(make({"query": "id=1 UNION SELECT * FROM users"}))
    assert result["action"] == "monitor"


def test_waf_url_encoded_attack():
    engine = WafEngine()
    result = engine.evaluate(make({"query": "id=1%20UNION%20SELECT%20*%20FROM%20users"}))
    assert result["is_attack"] is True
