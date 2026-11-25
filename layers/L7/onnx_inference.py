from typing import Any, Dict, Optional


class OnnxInference:
    """Optional ONNX inference component. Requires a valid ONNX model."""

    def __init__(self, model_path: Optional[str] = None):
        self.model_path = model_path
        self.available = False
        try:
            import onnxruntime
            self.available = True
        except Exception:
            self.available = False

    def infer(self, event: Dict[str, Any]) -> Dict[str, Any]:
        if not self.available:
            return {"available": False, "score": 0.0, "action": "monitor"}
        if not self.model_path:
            return {"available": True, "model": False, "score": 0.0, "action": "monitor"}
        raise RuntimeError("ONNX inference requires a valid ONNX model and validation")
