from typing import Any, Dict, Optional
from layers.L7.onnx_inference import OnnxInference


class OnnxEngine:
    """Optional ONNX engine. Falls back safely when unavailable."""

    def __init__(self, model_path: Optional[str] = None):
        self.inference = OnnxInference(model_path=model_path)

    def run(self, event: Dict[str, Any]) -> Dict[str, Any]:
        return self.inference.infer(event)
