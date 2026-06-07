#api.py

from fastapi import FastAPI
from security_gateway import SecurityGateway
from fastapi import FastAPI, Header, HTTPException
from database import create_database

app = FastAPI()
create_database()
API_KEY = "zaalimasecurity123"
gateway = SecurityGateway()
request_counter = {}

USER_ROLES = {
    "security_team": "admin",
    "developer_team": "developer",
    "intern_team": "viewer"
}

@app.get("/")
def home():
    return {"message": "Enterprise LLM Security Gateway Running"}

@app.post("/analyze")
def analyze(
    prompt: str,
    x_api_key: str = Header(None)
):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    findings = gateway.detect_pii(prompt)

    findings.extend(
        gateway.detect_prompt_injection(prompt)
    )

    sanitized = gateway.sanitize_prompt(prompt)

    gateway.save_log(
        prompt,
        sanitized,
        findings
    )

    gateway.save_to_database(
        prompt,
        sanitized,
        findings
    )

    return {
        "original": prompt,
        "sanitized": sanitized,
        "findings": findings
    }

@app.get("/access")
def check_access(
    team: str,
    x_api_key: str = Header(None)
):

    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    role = USER_ROLES.get(team)

    if not role:
        return {
            "status": "Access Denied"
        }

    return {
        "team": team,
        "role": role,
        "status": "Access Granted"
    }

@app.get("/rate_limit")
def rate_limit(user: str):

    if user not in request_counter:
        request_counter[user] = 0

    request_counter[user] += 1

    if request_counter[user] > 5:
        return {
            "status": "Blocked",
            "message": "Rate Limit Exceeded"
        }

    return {
        "status": "Allowed",
        "request_count": request_counter[user]
    }

dashboard_stats = {
    "total_requests": 57,
    "pii_detections": 14,
    "prompt_injections": 5,
    "blocked_requests": 7
}

@app.get("/dashboard")
def dashboard():

    return dashboard_stats