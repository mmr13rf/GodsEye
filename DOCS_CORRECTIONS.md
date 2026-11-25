# Corrections and limitations

- WAF now analyzes explicit HTTP fields rather than serializing the entire analysis dictionary.
- WAF returns score, matched rules, severity, and a recommended action.
- WAF defaults to monitor-only; blocking requires explicit `enforce=True`.
- URL decoding and whitespace normalization are applied before pattern matching.
- Covered rule categories include SQL injection, XSS, path traversal, command injection, SSRF, LDAP injection, XML/XXE injection, template injection, and open redirects.
- These are heuristic rules, not a guarantee of complete web attack coverage.
- Accuracy claims require a representative, labeled, held-out dataset and real-traffic validation.
