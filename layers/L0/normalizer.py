from typing import Any, Dict
from .telemetry import TelemetryEvent

class Normalizer:
    def normalize(self, event: TelemetryEvent) -> Dict[str, Any]:
        raw = event.raw
        return {
            "event_id": event.event_id,
            "timestamp": event.timestamp,
            "source": event.source,
            "event_type": raw.get("event_type", "unknown"),
            "src_ip": raw.get("src_ip"),
            "src_port": raw.get("src_port"),
            "dest_ip": raw.get("dest_ip"),
            "dest_port": raw.get("dest_port"),
            "protocol": raw.get("protocol", "unknown").lower(),
            "alert": raw.get("alert", {}),
            "flow": raw.get("flow", {}),
            "http": raw.get("http", {}),
            "dns": raw.get("dns", {}),
            "tls": raw.get("tls", {}),
        }
