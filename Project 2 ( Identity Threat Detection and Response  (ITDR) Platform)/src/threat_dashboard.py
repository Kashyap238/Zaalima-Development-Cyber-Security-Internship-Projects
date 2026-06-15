import pandas as pd
import os

def generate_alerts():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    alerts = []

    users = {}

    for _, row in data.iterrows():

        user = row["user"]
        location = row["location"]

        if user not in users:
            users[user] = location

        elif users[user] != location:
            alerts.append(
                f"Impossible Travel Detected: {user}"
            )

    mfa_counts = {}

    for _, row in data.iterrows():

        if row["event"] == "MFA Request":

            user = row["user"]

            mfa_counts[user] = (
                mfa_counts.get(user, 0) + 1
            )

            if mfa_counts[user] >= 3:

                alerts.append(
                    f"MFA Fatigue Attack: {user}"
                )

    for _, row in data.iterrows():

        if row["event"] == "Privilege Escalation":

            alerts.append(
                f"Privilege Escalation: {row['user']}"
            )

    print("\n=== ITDR Threat Dashboard ===\n")

    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    generate_alerts()