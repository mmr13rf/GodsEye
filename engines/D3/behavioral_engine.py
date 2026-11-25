from typing import Any, Dict

class BehavioralEngine:
    def __init__(self, port_diversity_threshold: float = 0.8):
        self.threshold = port_diversity_threshold

    def evaluate(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        score = analysis.get("port_diversity", 0.0)
        is_suspicious = score >= self.threshold
        return {"score": score, "is_suspicious": is_suspicious}
