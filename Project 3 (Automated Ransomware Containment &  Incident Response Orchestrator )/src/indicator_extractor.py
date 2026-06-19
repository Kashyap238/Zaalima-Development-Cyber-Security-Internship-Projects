import pandas as pd
import os

def extract_indicators():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Extracted Indicators ===\n")

    for _, row in data.iterrows():

        print(
            f"Hostname: {row['hostname']}"
        )

        print(
            f"IP: {row['ip']}"
        )

        print(
            f"User: {row['user']}"
        )

        print(
            f"Threat: {row['threat']}"
        )
        
        print(
            f"Process Hash: {row['process_hash']}"
        )

        print("-" * 40)

if __name__ == "__main__":
    extract_indicators()