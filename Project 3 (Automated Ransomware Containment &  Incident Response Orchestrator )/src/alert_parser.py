import pandas as pd
import os

def parse_alerts():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Security Alerts ===\n")

    print(data)

if __name__ == "__main__":
    parse_alerts()