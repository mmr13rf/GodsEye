from typing import Any, Dict, List

class AnomalyDetector:
    def __init__(self, threshold: float = 0.8):
        if not 0.0 <= threshold <= 1.0:
            raise ValueError("threshold must be between 0 and 1")
        self.threshold = threshold

    def detect(self, features: List[float]) -> Dict[str, Any]:
        if not isinstance(features, list):
            raise ValueError("features must be a list")
        score = sum(features) / len(features) if features else 0.0
        is_anomaly = score >= self.threshold
        return {"score": score, "is_anomaly": is_anomaly}
