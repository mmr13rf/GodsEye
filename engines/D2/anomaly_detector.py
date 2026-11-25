from typing import Any, Dict, List

class AnomalyDetector:
    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold

    def detect(self, features: List[float]) -> Dict[str, Any]:
        score = sum(features) / len(features) if features else 0.0
        is_anomaly = score >= self.threshold
        return {"score": score, "is_anomaly": is_anomaly}
