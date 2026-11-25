from typing import Any, Dict

class MonitoringFeedbackEngine:
    def __init__(self, alert_threshold: float = 0.2):
        if not isinstance(alert_threshold, (int, float)) or not (0 <= alert_threshold <= 1):
            raise ValueError("alert_threshold must be between 0 and 1")
        self.alert_threshold = float(alert_threshold)

    def evaluate(self, summary: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(summary, dict):
            raise ValueError("summary must be a dict")
        alert_rate = summary.get("alert_rate", 0.0)
        if not isinstance(alert_rate, (int, float)) or not (0 <= alert_rate <= 1):
            raise ValueError("alert_rate must be between 0 and 1")
        status = "critical" if alert_rate > self.alert_threshold else "healthy"
        return {"status": status, "alert_rate": alert_rate}
