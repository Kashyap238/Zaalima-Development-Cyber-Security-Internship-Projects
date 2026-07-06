import pandas as pd
import os

from risk_engine import get_risk_scores

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

    impossible_travel_count = 0
    mfa_fatigue_count = 0
    privilege_count = 0

    for _, row in data.iterrows():

        user = row["user"]
        location = row["location"]

        if user not in users:
            users[user] = location

        elif users[user] != location:

            alerts.append(
                f"Impossible Travel Detected: {user}"
            )

            impossible_travel_count += 1

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

                mfa_fatigue_count += 1

    for _, row in data.iterrows():

        if row["event"] == "Privilege Escalation":

            alerts.append(
                f"Privilege Escalation: {row['user']}"
            )

            privilege_count += 1

    risk_scores = get_risk_scores()

    highest_user = max(
        risk_scores,
        key=risk_scores.get
    )

    highest_score = risk_scores[highest_user]

    print("\n======================================")
    print("         ITDR SOC DASHBOARD")
    print("======================================\n")

    print(f"Total Users              : {len(risk_scores)}")
    print(f"Total Alerts             : {len(alerts)}")

    print("\nAttack Summary")

    print(f"Impossible Travel        : {impossible_travel_count}")
    print(f"MFA Fatigue              : {mfa_fatigue_count}")
    print(f"Privilege Escalation     : {privilege_count}")

    print("\nHighest Risk User")

    print(f"User                     : {highest_user}")
    print(f"Risk Score               : {highest_score}")

    print("\nCurrent Alerts")

    for alert in alerts:
        print(f"- {alert}")

    print("\n======================================")

if __name__ == "__main__":
    generate_alerts()