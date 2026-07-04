#impossible_travel_detecttion

import pandas as pd
import os
from incident_timeline import log_incident

def detect_impossible_travel():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    users = {}

    for _, row in data.iterrows():

        user = row["user"]
        location = row["location"]

        if user not in users:
            users[user] = location

        elif users[user] != location:

            print(
                f"Impossible Travel Detected: "
                f"{user} logged in from "
                f"{users[user]} and {location}"
            )

            log_incident(
                user=user,
                event="Impossible Travel",
                severity="High"
            )

if __name__ == "__main__":
    detect_impossible_travel()