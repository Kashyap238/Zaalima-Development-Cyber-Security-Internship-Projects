import pandas as pd
import os
from alert_manager import raise_alert

def detect_brute_force():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    failed_logins = {}

    for _, row in data.iterrows():

        if row["event"] == "Failed Login":

            user = row["user"]

            failed_logins[user] = (
                failed_logins.get(user, 0) + 1
            )

            if failed_logins[user] >= 5:

                raise_alert(
                    user=user,
                    event="Brute Force Attack",
                    severity="High",
                    message=f"Brute Force Attack Detected: {user}"
                )

if __name__ == "__main__":
    detect_brute_force()