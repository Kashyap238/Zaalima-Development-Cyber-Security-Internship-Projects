import pandas as pd
import os

def map_identity_graph(user):

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_graph.csv"
    )

    data = pd.read_csv(csv_path)

    print(f"\nIdentity Graph for {user}\n")

    first_level = data[
        data["source"] == user
    ]

    for _, row in first_level.iterrows():

        group = row["target"]

        print(
            f"{user} -> {group}"
        )

        second_level = data[
            data["source"] == group
        ]

        for _, item in second_level.iterrows():

            print(
                f"{group} -> {item['target']}"
            )

if __name__ == "__main__":

    map_identity_graph("admin")