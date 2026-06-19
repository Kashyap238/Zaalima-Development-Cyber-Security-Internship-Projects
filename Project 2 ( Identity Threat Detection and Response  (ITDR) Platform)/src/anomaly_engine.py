import pandas as pd
import os

from sklearn.ensemble import IsolationForest

def get_anomalies():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    data["event_id"] = range(
        len(data)
    )

    X = data[["event_id"]]

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    predictions = model.fit_predict(X)

    data["anomaly"] = predictions

    anomalies = data[
        data["anomaly"] == -1
    ]

    return anomalies[
        ["user", "event"]
    ].to_dict(
        orient="records"
    )