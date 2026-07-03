import json
import os
from datetime import datetime

TIMELINE_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "logs",
    "incident_timeline.json"
)


def log_incident(user, event, severity):

    incident = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "event": event,
        "severity": severity
    }

    if os.path.exists(TIMELINE_FILE):
        with open(TIMELINE_FILE, "r") as file:
            try:
                data = json.load(file)
            except:
                data = []
    else:
        data = []

    data.append(incident)

    with open(TIMELINE_FILE, "w") as file:
        json.dump(data, file, indent=4)

    return incident