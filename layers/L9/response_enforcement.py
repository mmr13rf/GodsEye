from typing import Any, Dict

class ResponseEnforcement:
    def __init__(self, mode: str = "monitor"):
        if mode not in ("monitor", "enforce"):
            raise ValueError("mode must be 'monitor' or 'enforce'")
        self.mode = mode

    def respond(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(decision, dict):
            raise ValueError("decision must be a dict")
        is_threat = decision.get("is_threat", False)
        if not isinstance(is_threat, bool):
            raise ValueError("is_threat must be a bool")
        action = "block" if is_threat and self.mode == "enforce" else "monitor"
        return {"action": action, "mode": self.mode}
