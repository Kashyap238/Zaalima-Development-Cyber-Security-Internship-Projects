import json
import os

current_dir = os.path.dirname(__file__)

tracker_file = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_tracker.json"
)


def generate_summary():

    if not os.path.exists(tracker_file):

        print("No Incident Data Found")
        return

    with open(tracker_file, "r") as file:

        data = json.load(file)

    print("\n======================================")
    print("        INCIDENT SUMMARY")
    print("======================================\n")

    print(f"Incident ID : IR-001")

    completed = 0

    for item in data:

        print(
            f"{item['step']} : {item['status']}"
        )

        if item["status"] == "Completed":
            completed += 1

    print("\n--------------------------------------")

    print(f"Completed Steps : {completed}")

    print(f"Total Steps     : {len(data)}")

    if completed == len(data):

        print("Overall Status  : SUCCESS")

    else:

        print("Overall Status  : IN PROGRESS")

    print("\n======================================")

if __name__ == "__main__":
    generate_summary()