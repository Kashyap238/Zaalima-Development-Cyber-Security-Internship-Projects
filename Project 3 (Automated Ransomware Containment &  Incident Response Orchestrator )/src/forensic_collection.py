import pandas as pd
import os

def collect_forensics():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Forensic Collection ===\n")

    for _, row in data.iterrows():

        if row["severity"] in [
            "High",
            "Critical"
        ]:

            print(
                f"KAPE artifacts collected from {row['hostname']}"
            )

if __name__ == "__main__":
    collect_forensics()