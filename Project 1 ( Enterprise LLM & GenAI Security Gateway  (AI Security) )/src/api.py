#api.py

from fastapi import FastAPI
from security_gateway import SecurityGateway
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
API_KEY = "zaalimasecurity123"
gateway = SecurityGateway()

USER_ROLES = {
    "security_team": "admin",
    "developer_team": "developer",
    "intern_team": "viewer"
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

    return {
        "original": prompt,
        "sanitized": sanitized,
        "findings": findings
    }