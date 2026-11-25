from typing import Any, Dict, Optional
from layers.L6.cnn_lstm import CnnLstmAnalyzer


class CnnLstmEngine:
    """Optional CNN-LSTM engine. Falls back safely when unavailable."""

    def __init__(self, model_path: Optional[str] = None):
        self.analyzer = CnnLstmAnalyzer(model_path=model_path)

    def run(self, event: Dict[str, Any]) -> Dict[str, Any]:
        return self.analyzer.analyze(event)
