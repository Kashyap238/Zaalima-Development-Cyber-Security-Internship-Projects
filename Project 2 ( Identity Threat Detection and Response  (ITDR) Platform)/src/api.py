from fastapi import FastAPI
from risk_engine import get_risk_scores
from high_risk_engine import get_high_risk_users
import sqlite3
from db_config import DB_PATH
from critical_accounts_engine import get_critical_accounts
from platform_info import platform_info
from anomaly_engine import get_anomalies

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


@app.get("/risk_scores")
def risk_scores():

    return get_risk_scores()


@app.get("/high_risk_users")
def high_risk_users():

    return get_high_risk_users()


@app.get("/stored_alerts")
def stored_alerts():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM alerts"
    )

    rows = cursor.fetchall()

    conn.close()

    return {
        "alerts": rows
    }


@app.get("/risk_scores_db")
def risk_scores_db():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT user, risk_score FROM risk_scores"
    )

    rows = cursor.fetchall()

    conn.close()

    return {
        "risk_scores": rows
    }


@app.get("/soc_dashboard")
def soc_dashboard():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM alerts"
    )
    total_alerts = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM risk_scores WHERE risk_score >= 50"
    )
    high_risk_users = cursor.fetchone()[0]

    cursor.execute(
        "SELECT MAX(risk_score) FROM risk_scores"
    )
    highest_risk = cursor.fetchone()[0]

    conn.close()

    return {
        "total_alerts": total_alerts,
        "high_risk_users": high_risk_users,
        "highest_risk_score": highest_risk,
        "platform_status": "Active"
    }


@app.get("/critical_accounts")
def critical_accounts():

    return {
        "critical_accounts":
        get_critical_accounts()
    }

@app.get("/platform_info")
def get_platform_info():

    return platform_info()

@app.get("/anomalies")
def anomalies():

    return {
        "anomalies":
        get_anomalies()
    }

@app.get("/report")
def report():

    return {
        "platform_status": "Active",
        "high_risk_users": len(get_high_risk_users()),
        "critical_accounts": len(get_critical_accounts()),
        "anomalies": len(get_anomalies())
    }