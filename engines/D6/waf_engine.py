from typing import Any, Dict
from layers.L5.waf_analysis import analyze


class WafEngine:
    def __init__(self, threshold: float = 0.6, enforce: bool = False):
        self.threshold = float(threshold)
        self.enforce = bool(enforce)

    def evaluate(self, request: Dict[str, Any]) -> Dict[str, Any]:
        result = analyze(request)
        score = result["score"]
        is_attack = score >= self.threshold
        action = "block" if is_attack and self.enforce else "monitor"
        return {**result, "is_attack": is_attack, "action": action}
