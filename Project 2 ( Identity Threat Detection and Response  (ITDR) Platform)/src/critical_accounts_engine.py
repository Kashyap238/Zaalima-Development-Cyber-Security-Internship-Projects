from risk_engine import get_risk_scores
import pandas as pd
import os

def get_critical_accounts():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_graph.csv"
    )

    data = pd.read_csv(csv_path)

    risk_scores = get_risk_scores()

    critical_accounts = []

    for user, risk in risk_scores.items():

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

        severity = risk + (resources * 20)

        if severity >= 70:

            critical_accounts.append(
                {
                    "user": user,
                    "risk_score": risk,
                    "blast_radius": resources,
                    "severity": severity
                }
            )

    return critical_accounts