import pytest
from layers.L7.onnx_inference import OnnxInference

def test_infer_normal():
    i = OnnxInference(input_size=3)
    r = i.infer([0.1, 0.2, 0.3])
    assert r["score"] == pytest.approx(0.2)

def test_invalid_size():
    with pytest.raises(ValueError):
        OnnxInference(input_size=0)

def test_invalid_features_length():
    i = OnnxInference(input_size=2)
    with pytest.raises(ValueError):
        i.infer([0.1])

def test_invalid_feature_type():
    i = OnnxInference(input_size=2)
    with pytest.raises(ValueError):
        i.infer([0.1, "bad"])
