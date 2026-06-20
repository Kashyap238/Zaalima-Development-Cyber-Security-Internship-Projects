from fastapi import FastAPI
from dashboard import dashboard_stats

app = FastAPI()

@app.get("/")
def home():

    return {
        "message":
        "Ransomware IR Orchestrator Running"
    }

@app.get("/dashboard")
def dashboard():

    return dashboard_stats()

@app.get("/containment_status")
def containment_status():

    return {
        "status": "Completed"
    }

@app.get("/forensic_status")
def forensic_status():

    return {
        "status": "Evidence Collected"
    }

@app.get("/incident_response_status")
def incident_response_status():

    return {
        "status":
        "Playbook Executed Successfully"
    }

