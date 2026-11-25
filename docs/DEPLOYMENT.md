# Deployment

## Requirements

- Linux with XDP/eBPF support
- Docker and Docker Compose
- Python 3.10+

## Run

```bash
make up
```

## Test

```bash
make test
```

## Notes

- XDP is monitor-only by default.
- Enforcement is gradual and only after validation.
- KPIs are targets, not guaranteed results.
