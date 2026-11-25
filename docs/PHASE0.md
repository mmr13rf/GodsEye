# Phase 0

Phase 0 creates the base monitor-only stack.

- XDP program passes all packets.
- Suricata runs in monitor mode.
- FastAPI dashboard exposes /health and /alerts.
- Docker Compose starts the services.

Next phases add the 10 layers and decision engines.
