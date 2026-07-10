import json
import os

current_dir = os.path.dirname(__file__)

tracker_file = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_tracker.json"
)


def show_incident_status():

    if not os.path.exists(tracker_file):

        print("No Incident Found")
        return

    with open(tracker_file, "r") as file:

        data = json.load(file)

    print("\n======================================")
    print("      INCIDENT STATUS DASHBOARD")
    print("======================================\n")

    completed = 0

    for item in data:

        print(f"✔ {item['step']} : {item['status']}")

        if item["status"] == "Completed":
            completed += 1

    print("\n--------------------------------------")

    print(f"Completed Steps : {completed}")

    print(f"Total Steps     : {len(data)}")

    if completed == len(data):

        print("\nOverall Status  : SUCCESS")

    else:

        print("\nOverall Status  : IN PROGRESS")

    print("\n======================================")

if __name__ == "__main__":
    show_incident_status()