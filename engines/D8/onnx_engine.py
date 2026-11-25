from typing import Any, Dict

class OnnxEngine:
    def __init__(self, threshold: float = 0.5):
        if not isinstance(threshold, (int, float)) or not (0 <= threshold <= 1):
            raise ValueError("threshold must be between 0 and 1")
        self.threshold = float(threshold)

    def evaluate(self, inference: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(inference, dict):
            raise ValueError("inference must be a dict")
        score = inference.get("score", 0.0)
        if not isinstance(score, (int, float)) or not (0 <= score <= 1):
            raise ValueError("score must be between 0 and 1")
        is_threat = score >= self.threshold
        return {"is_threat": is_threat, "severity": "high" if is_threat else "low"}
