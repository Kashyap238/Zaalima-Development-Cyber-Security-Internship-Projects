import pandas as pd
import os

def get_risk_scores():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    risk_scores = {}

    users = {}

    for _, row in data.iterrows():

        user = row["user"]

        if user not in risk_scores:
            risk_scores[user] = 0

        location = row["location"]

        if user not in users:
            users[user] = location

        elif users[user] != location:
            risk_scores[user] += 50

    mfa_counts = {}

    for _, row in data.iterrows():

        if row["event"] == "MFA Request":

            user = row["user"]

            mfa_counts[user] = mfa_counts.get(user, 0) + 1

            if mfa_counts[user] >= 3:
                risk_scores[user] += 30

    for _, row in data.iterrows():

        if row["event"] == "Privilege Escalation":
            risk_scores[row["user"]] += 80

    return risk_scores