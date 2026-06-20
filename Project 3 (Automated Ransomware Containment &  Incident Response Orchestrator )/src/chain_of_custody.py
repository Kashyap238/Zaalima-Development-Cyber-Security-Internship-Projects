import pandas as pd
import os
from datetime import datetime

def log_chain_of_custody():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Chain of Custody Log ===\n")

    for _, row in data.iterrows():

        if row["severity"] in [
            "High",
            "Critical"
        ]:

            print(
                f"{datetime.now()} | "
                f"{row['hostname']} | "
                f"Memory Dump Collected"
            )

            print(
                f"{datetime.now()} | "
                f"{row['hostname']} | "
                f"Forensic Artifacts Collected"
            )

if __name__ == "__main__":
    log_chain_of_custody()