import json
import os

current_dir = os.path.dirname(__file__)

tracker_file = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_tracker.json"
)


def response_metrics():

    if not os.path.exists(tracker_file):
        print("No Incident Data Found")
        return

    with open(tracker_file, "r") as file:
        data = json.load(file)

    total_steps = len(data)

    completed = 0

    for item in data:

        if item["status"] == "Completed":
            completed += 1

    failed = total_steps - completed

    success_rate = (
        completed / total_steps * 100
    ) if total_steps else 0

    print("\n======================================")
    print("      RESPONSE METRICS")
    print("======================================\n")

    print(f"Total Response Steps : {total_steps}")
    print(f"Completed Steps      : {completed}")
    print(f"Failed Steps         : {failed}")
    print(f"Success Rate         : {success_rate:.2f}%")

    print("\n======================================")

if __name__ == "__main__":
    response_metrics()