import pandas as pd
import os

def calculate_blast_radius(user):

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_graph.csv"
    )

    data = pd.read_csv(csv_path)

    resources = 0

    first_level = data[
        data["source"] == user
    ]

    for _, row in first_level.iterrows():

        group = row["target"]

        second_level = data[
            data["source"] == group
        ]

        resources += len(second_level)

    print(
        f"{user} Blast Radius Score: {resources}"
    )

if __name__ == "__main__":

    calculate_blast_radius("admin")