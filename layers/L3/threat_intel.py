from typing import Any, Dict, List

class ThreatIntel:
    def __init__(self, malicious_ips: List[str] = None):
        self.malicious_ips = set(malicious_ips or [])

    def check_ip(self, ip: str) -> bool:
        return ip in self.malicious_ips

    def analyze(self, event: Dict[str, Any]) -> Dict[str, Any]:
        src = event.get("src_ip") or ""
        dest = event.get("dest_ip") or ""
        return {
            "src_ip_malicious": self.check_ip(src),
            "dest_ip_malicious": self.check_ip(dest),
        }
