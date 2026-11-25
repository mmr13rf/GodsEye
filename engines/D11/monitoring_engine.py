from typing import Any, Dict
from layers.L10.monitoring import Monitoring


class MonitoringEngine:
    """Monitoring engine for real-time validation and testing."""

    def __init__(self):
        self.monitoring = Monitoring()

    def run(self, event: Dict[str, Any]) -> Dict[str, Any]:
        return self.monitoring.record(event)

    def stats(self) -> Dict[str, int]:
        return self.monitoring.stats()
