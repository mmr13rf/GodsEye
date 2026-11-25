from typing import Any, Dict

class ResponseEnforcementEngine:
    def __init__(self, mode: str = "monitor"):
        if mode not in ("monitor", "enforce"):
            raise ValueError("mode must be 'monitor' or 'enforce'")
        self.mode = mode

    def evaluate(self, response: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(response, dict):
            raise ValueError("response must be a dict")
        action = response.get("action", "monitor")
        if action not in ("monitor", "block"):
            raise ValueError("action must be 'monitor' or 'block'")
        return {"final_action": action, "mode": self.mode}
