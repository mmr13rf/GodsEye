from typing import Any, Dict, List

class OnnxInference:
    def __init__(self, input_size: int = 10):
        if not isinstance(input_size, int) or input_size <= 0:
            raise ValueError("input_size must be a positive int")
        self.input_size = input_size

    def infer(self, features: List[float]) -> Dict[str, Any]:
        if not isinstance(features, list):
            raise ValueError("features must be a list")
        if len(features) != self.input_size:
            raise ValueError(f"features must have length {self.input_size}")
        for f in features:
            if not isinstance(f, (int, float)):
                raise ValueError("each feature must be a number")
        score = sum(features) / len(features)
        return {"score": score}
