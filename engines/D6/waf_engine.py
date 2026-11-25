from typing import Any, Dict

class WafEngine:
    def __init__(self, attack_patterns: list = None):
        self.attack_patterns = attack_patterns or []

    def evaluate(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(analysis, dict):
            raise ValueError("analysis must be a dict")
        text = " ".join(str(v) for v in analysis.values())
        is_attack = any(p.lower() in text.lower() for p in self.attack_patterns)
        return {"is_attack": is_attack, "severity": "high" if is_attack else "low"}
