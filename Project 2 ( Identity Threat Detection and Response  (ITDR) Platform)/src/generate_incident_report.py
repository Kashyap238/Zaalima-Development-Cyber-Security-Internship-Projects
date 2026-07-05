import json
import os

current_dir = os.path.dirname(__file__)

timeline_path = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_timeline.json"
)

report_path = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_report.json"
)


def generate_report():

    if not os.path.exists(timeline_path):
        print("No incidents found.")
        return

    with open(timeline_path, "r") as file:
        incidents = json.load(file)

    report = {
        "total_incidents": len(incidents),
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0,
        "incidents": incidents
    }

    for incident in incidents:

        severity = incident["severity"].lower()

        if severity in report:
            report[severity] += 1

    with open(report_path, "w") as file:
        json.dump(report, file, indent=4)

    print("Incident Report Generated Successfully")


if __name__ == "__main__":
    generate_report()