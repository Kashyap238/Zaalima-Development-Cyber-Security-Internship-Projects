import pandas as pd
import os

def generate_tickets():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    print("\n=== Incident Tickets ===\n")

    ticket_id = 1000

    for _, row in data.iterrows():

        if row["severity"] in [
            "High",
            "Critical"
        ]:

            print(
                f"INC-{ticket_id} | "
                f"{row['hostname']} | "
                f"{row['threat']}"
            )

            ticket_id += 1

if __name__ == "__main__":
    generate_tickets()