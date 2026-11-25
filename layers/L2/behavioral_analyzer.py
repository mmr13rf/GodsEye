from typing import Any, Dict, List
from collections import defaultdict, deque

class BehavioralAnalyzer:
    def __init__(self, window_size: int = 100):
        self.window_size = window_size
        self.history = defaultdict(deque)

    def analyze(self, event: Dict[str, Any]) -> Dict[str, Any]:
        src = event.get("src_ip") or "unknown"
        dest_port = event.get("dest_port") or 0
        self.history[src].append(dest_port)
        if len(self.history[src]) > self.window_size:
            self.history[src].popleft()
        unique_ports = len(set(self.history[src]))
        total = len(self.history[src])
        ratio = unique_ports / total if total else 0.0
        return {"src_ip": src, "unique_ports": unique_ports, "total_events": total, "port_diversity": ratio}
