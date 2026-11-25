from typing import Any, Dict, List

class CnnLstmAnalyzer:
    def __init__(self, window_size: int = 10):
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("window_size must be a positive int")
        self.window_size = window_size

    def analyze(self, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not isinstance(events, list):
            raise ValueError("events must be a list")
        if len(events) == 0:
            return {"window_size": self.window_size, "events": 0, "avg_packet_size": 0.0}
        sizes = []
        for e in events:
            if not isinstance(e, dict):
                raise ValueError("each event must be a dict")
            size = e.get("packet_size", 0)
            if not isinstance(size, (int, float)) or size < 0:
                raise ValueError("packet_size must be a non-negative number")
            sizes.append(float(size))
        return {"window_size": self.window_size, "events": len(events), "avg_packet_size": sum(sizes)/len(sizes)}
