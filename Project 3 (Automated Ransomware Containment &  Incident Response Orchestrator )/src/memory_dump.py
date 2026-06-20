import pandas as pd
import os

def collect_memory_dump():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Memory Dump Collection ===\n")

    for _, row in data.iterrows():

        if row["severity"] in [
            "High",
            "Critical"
        ]:

            print(
                f"Memory dump collected from {row['hostname']}"
            )

if __name__ == "__main__":
    collect_memory_dump()