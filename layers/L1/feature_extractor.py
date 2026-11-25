from typing import Any, Dict, List

class FeatureExtractor:
    def extract(self, event: Dict[str, Any]) -> List[float]:
        features = []
        features.append(1.0 if event.get("protocol") == "tcp" else 0.0)
        features.append(1.0 if event.get("protocol") == "udp" else 0.0)
        features.append(float(event.get("src_port") or 0))
        features.append(float(event.get("dest_port") or 0))
        features.append(1.0 if event.get("event_type") == "alert" else 0.0)
        return features
