import pandas as pd
import os

def detect_password_spraying():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    failed_users = set()

    for _, row in data.iterrows():

        if row["event"] == "Failed Login":

            failed_users.add(
                row["user"]
            )

    if len(failed_users) >= 5:

        print(
            "Password Spraying Attack Detected"
        )

if __name__ == "__main__":
    detect_password_spraying()