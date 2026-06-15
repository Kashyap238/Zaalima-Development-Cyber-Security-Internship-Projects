import pandas as pd
import os

def calculate_blast_radius(user):

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_relationships.csv"
    )

    data = pd.read_csv(csv_path)

    impacted = data[data["user"] == user]

    print(f"\nCompromised User: {user}")
    print("\nPotential Blast Radius:\n")

    for _, row in impacted.iterrows():

        print(
            f"- Access to {row['resource']}"
        )

if __name__ == "__main__":

    calculate_blast_radius("admin")