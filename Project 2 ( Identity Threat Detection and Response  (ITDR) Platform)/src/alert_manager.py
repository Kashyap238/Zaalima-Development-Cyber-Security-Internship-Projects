from incident_timeline import log_incident

try:
    from alert_storage import save_alert
except ImportError:
    save_alert = None


def raise_alert(user, event, severity, message):

    print(message)

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