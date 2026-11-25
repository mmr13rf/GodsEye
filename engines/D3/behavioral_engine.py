from typing import Any, Dict

class BehavioralEngine:
    def __init__(self, port_diversity_threshold: float = 0.8):
        if not 0.0 <= port_diversity_threshold <= 1.0:
            raise ValueError("threshold must be between 0 and 1")
        self.threshold = port_diversity_threshold

    def evaluate(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(analysis, dict):
            raise ValueError("analysis must be a dict")
        score = analysis.get("port_diversity", 0.0)
        is_suspicious = score >= self.threshold
        return {"score": score, "is_suspicious": is_suspicious}
