from typing import Any, Dict
from layers.L9.response import Response


class ResponseEngine:
    """Operational response engine. Defaults to monitor-only."""

    def __init__(self, enforce: bool = False):
        self.response = Response(enforce=enforce)

    def run(self, is_attack: bool, score: float, context: Dict[str, Any]) -> Dict[str, Any]:
        action = self.response.decide(is_attack, score)
        return self.response.execute(action, context)
