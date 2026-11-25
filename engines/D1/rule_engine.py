from typing import Any, Dict, List
import yaml, os

class RuleEngine:
    def __init__(self, rules_path: str = None):
        base = os.path.dirname(__file__)
        self.rules_path = rules_path or os.path.join(base, "rules.yaml")
        with open(self.rules_path) as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict) or "rules" not in data:
            raise ValueError("invalid rules file")
        self.rules = data["rules"]

    def evaluate(self, event: Dict[str, Any]) -> List[Dict[str, Any]]:
        if not isinstance(event, dict):
            raise ValueError("event must be a dict")
        hits = []
        for rule in self.rules:
            if self._match(rule, event):
                hits.append({"rule_id": rule["id"], "severity": rule["severity"], "action": rule["action"]})
        return hits

    def _match(self, rule: Dict[str, Any], event: Dict[str, Any]) -> bool:
        cond = rule["when"]
        for key, expected in cond.items():
            actual = event
            for part in key.split("."):
                if not isinstance(actual, dict) or part not in actual:
                    return False
                actual = actual[part]
            if actual != expected:
                return False
        return True
