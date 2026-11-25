from typing import Any, Dict

class WafAnalyzer:
    def analyze(self, event: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(event, dict):
            raise ValueError("event must be a dict")
        http = event.get("http", {}) or {}
        return {
            "method": http.get("method", ""),
            "path": http.get("path", ""),
            "query": http.get("query", ""),
            "body": http.get("body", ""),
        }
