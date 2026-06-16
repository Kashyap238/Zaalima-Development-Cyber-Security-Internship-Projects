from risk_engine import get_risk_scores
import pandas as pd
import os

def get_blast_radius(user):

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

    return resources

def detect_critical_accounts():

    risk_scores = get_risk_scores()

    print("\n=== Critical Accounts ===\n")

    for user, risk in risk_scores.items():

        blast_radius = get_blast_radius(user)

        severity = risk + (blast_radius * 20)

        if severity >= 70:

            print(
                f"{user} | "
                f"Risk={risk} | "
                f"Blast Radius={blast_radius} | "
                f"Severity={severity}"
            )

if __name__ == "__main__":

    detect_critical_accounts()