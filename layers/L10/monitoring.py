from typing import Any, Dict, List
import time


class Monitoring:
    """In-memory monitoring component for validation and testing."""

    def __init__(self, max_events: int = 10000):
        self.events: List[Dict[str, Any]] = []
        self.max_events = int(max_events)

    def record(self, event: Dict[str, Any]) -> Dict[str, Any]:
        entry = {"timestamp": time.time(), "data": event}
        self.events.append(entry)
        if len(self.events) > self.max_events:
            self.events.pop(0)
        return entry

    def stats(self) -> Dict[str, int]:
        return {"events": len(self.events)}
