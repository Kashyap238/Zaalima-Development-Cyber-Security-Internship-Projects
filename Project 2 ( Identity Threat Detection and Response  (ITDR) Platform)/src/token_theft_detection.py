import pandas as pd
import os

def detect_token_theft():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    token_events = data[
        data["event"] == "Token Used"
    ]

    users = token_events["user"].unique()

    for user in users:

        user_events = token_events[
            token_events["user"] == user
        ]

        locations = set(
            user_events["location"]
        )

        if len(locations) > 1:

            print(
                f"Possible Token Theft Detected: {user}"
            )

if __name__ == "__main__":
    detect_token_theft()