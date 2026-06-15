import pandas as pd
import os

def detect_privilege_escalation():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    for _, row in data.iterrows():

        if row["event"] == "Privilege Escalation":

            print(
                f"Privilege Escalation Detected: "
                f"{row['user']}"
            )

if __name__ == "__main__":
    detect_privilege_escalation()