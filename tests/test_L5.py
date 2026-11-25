from layers.L5.waf_analyzer import WafAnalyzer

def test_analyze_http():
    analyzer = WafAnalyzer()
    event = {"http": {"method": "GET", "path": "/", "query": "id=1", "body": ""}}
    result = analyzer.analyze(event)
    assert result["method"] == "GET"
    assert result["query"] == "id=1"
