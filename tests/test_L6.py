import pytest
from layers.L6.cnn_lstm_analyzer import CnnLstmAnalyzer

def test_analyze_normal():
    a = CnnLstmAnalyzer()
    r = a.analyze([{"packet_size": 100}, {"packet_size": 200}])
    assert r["events"] == 2
    assert r["avg_packet_size"] == 150.0

def test_invalid_window():
    with pytest.raises(ValueError):
        CnnLstmAnalyzer(window_size=0)

def test_invalid_event():
    a = CnnLstmAnalyzer()
    with pytest.raises(ValueError):
        a.analyze(["bad"])

def test_negative_size():
    a = CnnLstmAnalyzer()
    with pytest.raises(ValueError):
        a.analyze([{"packet_size": -1}])
