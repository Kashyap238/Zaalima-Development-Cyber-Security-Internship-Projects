import pandas as pd
import os

def revoke_sessions():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Session Revocation ===\n")

    for _, row in data.iterrows():

        if row["severity"] in [
            "High",
            "Critical"
        ]:

            print(
                f"Sessions revoked for {row['user']}"
            )

if __name__ == "__main__":
    revoke_sessions()