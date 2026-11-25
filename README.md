# GodsEye

GodsEye یک IDS/IPS لبه‌محور و خودآموز است که با XDP/eBPF، Suricata، CNN-LSTM، ONNX Runtime و FastAPI ساخته می‌شود.

## وضعیت فعلی

- [x] L0 Telemetry & Normalization
- [x] L1 Feature Extraction
- [x] L2 Behavioral Analysis
- [x] L3 Threat Intelligence
- [x] L4 DNS/TLS Analysis
- [x] L5 WAF Analysis
- [x] L6 CNN-LSTM Analysis
- [x] L7 ONNX Inference
- [x] D1 Rule Engine
- [x] D2 Anomaly Detection
- [x] D3 Behavioral Engine
- [x] D4 Threat Intel Engine
- [x] D5 DNS/TLS Engine
- [x] D6 WAF Engine
- [x] D7 CNN-LSTM Engine
- [x] D8 ONNX Engine
- [x] تست‌های پایه
- [x] اعتبارسنجی ورودی

## اجرا

```bash
make up
```

## تست

```bash
make test
```

## KPIها

- p99 پردازش < 50ms
- p99 تصمیم < 5ms
- کاهش هشدار 80٪ نسبت به baseline
- حداکثر 20 هشدار در 100 رویداد

این اهداف هستند، نه نتایج تضمین‌شده.
