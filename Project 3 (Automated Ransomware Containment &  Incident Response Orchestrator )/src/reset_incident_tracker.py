import os

current_dir = os.path.dirname(__file__)

tracker_file = os.path.join(
    current_dir,
    "..",
    "logs",
    "incident_tracker.json"
)

with open(tracker_file, "w") as file:
    file.write("[]")

print("Incident Tracker Reset")