from fastapi import FastAPI

app = FastAPI(title="GodsEye Dashboard")

@app.get("/health")
def health():
    return {"status": "ok", "mode": "monitor_only"}

@app.get("/alerts")
def alerts():
    return {"alerts": []}
