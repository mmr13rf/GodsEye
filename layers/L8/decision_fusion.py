from typing import Any, Dict, List

class DecisionFusion:
    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights or {}

    def fuse(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not isinstance(results, list):
            raise ValueError("results must be a list")
        if len(results) == 0:
            return {"score": 0.0}
        total = 0.0
        weight_sum = 0.0
        for r in results:
            if not isinstance(r, dict):
                raise ValueError("each result must be a dict")
            score = r.get("score", 0.0)
            if not isinstance(score, (int, float)) or not (0 <= score <= 1):
                raise ValueError("score must be between 0 and 1")
            w = self.weights.get(r.get("engine", "default"), 1.0)
            if not isinstance(w, (int, float)) or w < 0:
                raise ValueError("weight must be a non-negative number")
            total += score * w
            weight_sum += w
        if weight_sum == 0:
            raise ValueError("total weight must be positive")
        return {"score": total / weight_sum}
