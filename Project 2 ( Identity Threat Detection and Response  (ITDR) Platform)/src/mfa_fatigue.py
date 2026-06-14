import pandas as pd
import os

def detect_mfa_fatigue():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    counts = {}

    for _, row in data.iterrows():

        if row["event"] == "MFA Request":

            user = row["user"]

            counts[user] = counts.get(user, 0) + 1

            if counts[user] >= 3:

                print(
                    f"MFA Fatigue Attack Suspected: {user}"
                )

if __name__ == "__main__":
    detect_mfa_fatigue()