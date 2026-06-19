import pandas as pd
import os

def suspend_users():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== User Suspension ===\n")

    for _, row in data.iterrows():

        if row["severity"] == "Critical":

            print(
                f"User {row['user']} suspended"
            )

if __name__ == "__main__":
    suspend_users()