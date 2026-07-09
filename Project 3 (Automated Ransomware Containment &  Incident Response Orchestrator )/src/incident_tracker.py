import json
import os
from datetime import datetime

current_dir = os.path.dirname(__file__)

tracker_file = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_tracker.json"
)


def log_step(step, status):

    if os.path.exists(tracker_file):

        with open(tracker_file, "r") as file:
            data = json.load(file)

    else:

        data = []

    data.append({

        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "step": step,

        "status": status

    })

    with open(tracker_file, "w") as file:

        json.dump(data, file, indent=4)