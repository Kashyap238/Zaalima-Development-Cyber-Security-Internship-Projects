from fastapi import FastAPI

app = FastAPI()

dashboard_stats = {
    "impossible_travel": 1,
    "mfa_fatigue": 1,
    "privilege_escalation": 1,
    "total_alerts": 3
}

@app.get("/")
def home():

    return {
        "message": "ITDR Platform Running"
    }

@app.get("/dashboard")
def dashboard():

    return dashboard_stats

@app.get("/alerts")
def alerts():

    return {
        "alerts": [
            "Impossible Travel Detected",
            "MFA Fatigue Attack",
            "Privilege Escalation"
        ]
    }

@app.get("/blast_radius")
def blast_radius():

    return {
        "user": "admin",
        "resources": [
            "Production AWS",
            "Domain Controllers",
            "Security Dashboard"
        ]
    }