from typing import Any, Dict


class Response:
    """Response component. Block is disabled unless enforce=True."""

    def __init__(self, enforce: bool = False):
        self.enforce = bool(enforce)

    def decide(self, is_attack: bool, score: float) -> str:
        if is_attack and self.enforce:
            return "block"
        return "monitor"

    def execute(self, action: str, context: Dict[str, Any]) -> Dict[str, Any]:
        if action not in {"monitor", "block"}:
            raise ValueError("invalid action")
        return {"action": action, "context": context, "executed": True}
