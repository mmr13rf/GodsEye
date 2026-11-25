from layers.L4.dns_tls_analyzer import DnsTlsAnalyzer

def test_analyze_dns_tls():
    analyzer = DnsTlsAnalyzer()
    event = {"dns": {"query": "example.com", "type": "A"}, "tls": {"sni": "example.com", "version": "TLS1.3"}}
    result = analyzer.analyze(event)
    assert result["dns_query"] == "example.com"
    assert result["tls_sni"] == "example.com"
