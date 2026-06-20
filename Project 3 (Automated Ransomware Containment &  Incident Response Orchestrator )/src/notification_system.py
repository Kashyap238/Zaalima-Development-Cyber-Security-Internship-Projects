import pandas as pd
import os

def send_notifications():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== IR Team Notifications ===\n")

    for _, row in data.iterrows():

        if row["severity"] in [
            "High",
            "Critical"
        ]:

            print(
                f"Alert sent to SOC Team "
                f"for {row['hostname']}"
            )

if __name__ == "__main__":
    send_notifications()