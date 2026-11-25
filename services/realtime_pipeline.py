from typing import Any, Dict
import time
from layers.L5.waf_analysis import analyze
from layers.L9.response import Response
from layers.L10.monitoring import Monitoring


class RealTimePipeline:
    """Experimental real-time analysis pipeline. Defaults to monitor-only."""

    def __init__(self, enforce: bool = False, threshold: float = 0.6):
        self.enforce = bool(enforce)
        self.threshold = float(threshold)
        self.response = Response(enforce=self.enforce)
        self.monitoring = Monitoring()

    def process(self, event: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(event, dict):
            raise ValueError("event must be a dict")
        started = time.perf_counter()
        waf = analyze(event)
        score = waf["score"]
        is_attack = score >= self.threshold
        action = self.response.decide(is_attack, score)
        result = {
            "waf": waf,
            "is_attack": is_attack,
            "action": action,
            "latency_ms": round((time.perf_counter() - started) * 1000, 3),
            "mode": "enforce" if self.enforce else "monitor-only",
        }
        self.monitoring.record({"event": event, "result": result})
        return result
