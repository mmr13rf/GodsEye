from typing import Any, Dict, Iterable
import re
from urllib.parse import unquote_plus

DEFAULT_PATTERNS = {
    "sql_injection": [r"union\s+select", r"or\s+1\s*=\s*1", r"sleep\s*\(", r"benchmark\s*\(", r"select\s+.*\s+from\s+", r"insert\s+into\s+", r"update\s+.*\s+set\s+", r"delete\s+from\s+"],
    "xss": [r"<\s*script", r"javascript\s*:", r"on\w+\s*=", r"<\s*img[^>]*\bonerror\s*="],
    "path_traversal": [r"(\.\./)+", r"%2e%2e(?:%2f|/)", r"\.\.(?:/|%2f)"],
    "command_injection": [r"[;|`]\s*(?:cat|ls|id|whoami|wget|curl)\b", r"\$\((?:cat|ls|id|whoami)\s", r"`(?:cat|ls|id|whoami)\s"],
    "ssrf": [r"https?://(?:169\.254\.169\.254|localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])", r"file://", r"gopher://"],
    "ldap_injection": [r"\*\)\s*\(\|", r"\)\s*\(&", r"\*\)\s*\("],
    "xml_injection": [r"<\s*!doctype", r"<\s*entity", r"<!\[cdata\["],
    "template_injection": [r"\{\{.*?\}\}", r"\{%.*?%\}", r"\$\{.*?\}"],
    "open_redirect": [r"https?://(?:[^\s/]+\.)+[a-z]{2,}", r"//[^/\s]+\.[a-z]{2,}"],
}

CATEGORY_WEIGHT = 0.75


def _normalize(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, dict):
        value = " ".join(f"{k}:{v}" for k, v in value.items())
    text = str(value)
    text = unquote_plus(text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def _scan(text: str, patterns: Iterable[str]) -> list:
    return [p for p in patterns if re.search(p, text)]


def analyze(request: Dict[str, Any], patterns: Dict[str, list] = None) -> Dict[str, Any]:
    if not isinstance(request, dict):
        raise ValueError("request must be a dict")
    patterns = patterns or DEFAULT_PATTERNS
    fields = {
        "method": request.get("method", ""),
        "path": request.get("path", ""),
        "query": request.get("query", ""),
        "headers": request.get("headers", {}),
        "body": request.get("body", ""),
    }
    matched = []
    score = 0.0
    for category, pats in patterns.items():
        hits = []
        for field, value in fields.items():
            normalized = _normalize(value)
            hits.extend(f"{field}:{h}" for h in _scan(normalized, pats))
        if hits:
            matched.append({"category": category, "hits": hits})
            score += CATEGORY_WEIGHT
    score = min(score, 1.0)
    severity = "low" if score < .3 else "medium" if score < .6 else "high" if score < .85 else "critical"
    return {
        "score": round(score, 3),
        "matched_rules": matched,
        "severity": severity,
        "recommended_action": "monitor" if score < .6 else "review",
    }
