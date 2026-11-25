from typing import Any, Dict, List

class MonitoringFeedback:
    def __init__(self):
        self.metrics = {"events": 0, "alerts": 0, "blocks": 0}

    def record(self, event: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(event, dict):
            raise ValueError("event must be a dict")
        self.metrics["events"] += 1
        if event.get("is_threat", False):
            self.metrics["alerts"] += 1
        if event.get("action", "") == "block":
            self.metrics["blocks"] += 1
        return dict(self.metrics)

    def summary(self) -> Dict[str, Any]:
        events = self.metrics["events"]
        alerts = self.metrics["alerts"]
        blocks = self.metrics["blocks"]
        alert_rate = alerts / events if events else 0.0
        block_rate = blocks / events if events else 0.0
        return {"events": events, "alerts": alerts, "blocks": blocks, "alert_rate": alert_rate, "block_rate": block_rate}
