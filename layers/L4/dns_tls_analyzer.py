from typing import Any, Dict

class DnsTlsAnalyzer:
    def analyze(self, event: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(event, dict):
            raise ValueError("event must be a dict")
        dns = event.get("dns", {}) or {}
        tls = event.get("tls", {}) or {}
        return {
            "dns_query": dns.get("query", ""),
            "dns_type": dns.get("type", ""),
            "tls_sni": tls.get("sni", ""),
            "tls_version": tls.get("version", ""),
        }
