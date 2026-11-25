from typing import Any, Dict

class DnsTlsEngine:
    def __init__(self, suspicious_domains: list = None):
        self.suspicious_domains = set(suspicious_domains or [])

    def evaluate(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(analysis, dict):
            raise ValueError("analysis must be a dict")
        dns_query = analysis.get("dns_query", "")
        tls_sni = analysis.get("tls_sni", "")
        is_suspicious = dns_query in self.suspicious_domains or tls_sni in self.suspicious_domains
        return {"is_suspicious": is_suspicious, "severity": "high" if is_suspicious else "low"}
