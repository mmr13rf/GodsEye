import pytest
from engines.D2.anomaly_detector import AnomalyDetector

def test_detect_anomaly():
    detector = AnomalyDetector(threshold=0.5)
    result = detector.detect([1.0, 1.0, 1.0])
    assert result["is_anomaly"] is True

def test_invalid_threshold():
    with pytest.raises(ValueError):
        AnomalyDetector(threshold=2.0)
