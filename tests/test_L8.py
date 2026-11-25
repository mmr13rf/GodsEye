import pytest
from layers.L8.decision_fusion import DecisionFusion

def test_fuse_normal():
    f = DecisionFusion()
    r = f.fuse([{"engine": "rule", "score": 0.2}, {"engine": "ml", "score": 0.4}])
    assert r["score"] == pytest.approx(0.3)

def test_invalid_results():
    f = DecisionFusion()
    with pytest.raises(ValueError):
        f.fuse("bad")

def test_invalid_score():
    f = DecisionFusion()
    with pytest.raises(ValueError):
        f.fuse([{"engine": "rule", "score": 2.0}])

def test_zero_weight():
    f = DecisionFusion(weights={"rule": 0.0})
    with pytest.raises(ValueError):
        f.fuse([{"engine": "rule", "score": 0.5}])
