from typing import Any, Dict

class ThreatIntelEngine:
    def evaluate(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(analysis, dict):
            raise ValueError("analysis must be a dict")
        is_threat = analysis.get("src_ip_malicious", False) or analysis.get("dest_ip_malicious", False)
        return {"is_threat": is_threat, "severity": "high" if is_threat else "low"}
