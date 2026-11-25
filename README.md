# GodsEye

GodsEye یک IDS/IPS لبه‌محور و خودآموز است که با XDP/eBPF، Suricata، CNN-LSTM، ONNX Runtime و FastAPI ساخته می‌شود.

## وضعیت فاز ۱

- [x] L0 Telemetry & Normalization
- [x] D1 Rule Engine
- [x] تست‌های پایه

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
