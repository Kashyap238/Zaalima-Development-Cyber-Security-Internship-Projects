import pandas as pd
import os

def dashboard_stats():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "alerts.csv"
    )

    data = pd.read_csv(csv_path)

    total_alerts = len(data)

    critical_alerts = len(
        data[data["severity"] == "Critical"]
    )

    high_alerts = len(
        data[data["severity"] == "High"]
    )

    return {
        "total_alerts": total_alerts,
        "critical_alerts": critical_alerts,
        "high_alerts": high_alerts,
        "platform_status": "Active"
    }

if __name__ == "__main__":

    print(
        dashboard_stats()
    )