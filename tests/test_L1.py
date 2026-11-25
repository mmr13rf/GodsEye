from layers.L1.feature_extractor import FeatureExtractor

def test_extract_features():
    extractor = FeatureExtractor()
    event = {"protocol": "tcp", "src_port": 1234, "dest_port": 22, "event_type": "alert"}
    features = extractor.extract(event)
    assert features[0] == 1.0
    assert features[3] == 22.0
