from typing import Any, Dict

class CnnLstmEngine:
    def __init__(self, threshold: float = 1000.0):
        if not isinstance(threshold, (int, float)) or threshold <= 0:
            raise ValueError("threshold must be a positive number")
        self.threshold = float(threshold)

    def evaluate(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(analysis, dict):
            raise ValueError("analysis must be a dict")
        avg = analysis.get("avg_packet_size", 0.0)
        if not isinstance(avg, (int, float)) or avg < 0:
            raise ValueError("avg_packet_size must be a non-negative number")
        is_anomaly = avg > self.threshold
        return {"is_anomaly": is_anomaly, "severity": "high" if is_anomaly else "low"}
