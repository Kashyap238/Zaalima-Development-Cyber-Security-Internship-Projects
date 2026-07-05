from incident_timeline import log_incident

try:
    from alert_storage import save_alert
except ImportError:
    save_alert = None

from risk_engine import get_risk_scores


def get_severity(score):

    if score <= 30:
        return "Low"

    elif score <= 60:
        return "Medium"

    elif score <= 80:
        return "High"

    else:
        return "Critical"


def raise_alert(user, event, message):

    risk_scores = get_risk_scores()

    score = risk_scores.get(user, 0)

    severity = get_severity(score)

    print(f"[{severity}] {message}")

    log_incident(
        user=user,
        event=event,
        severity=severity
    )

    if save_alert:
        try:
            save_alert(user, event, severity)
        except Exception:
            pass