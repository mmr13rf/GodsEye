from dataclasses import dataclass, field
from typing import Any, Dict
import time, uuid

@dataclass
class TelemetryEvent:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)
    source: str = "suricata"
    raw: Dict[str, Any] = field(default_factory=dict)

class TelemetryCollector:
    def collect(self, raw: Dict[str, Any]) -> TelemetryEvent:
        if not isinstance(raw, dict):
            raise ValueError("raw must be a dict")
        return TelemetryEvent(raw=raw)
