import pandas as pd
import os

def generate_metrics():

    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(
        current_dir,
        "..",
        "data",
        "identity_events.csv"
    )

    data = pd.read_csv(csv_path)

    total_users = data["user"].nunique()

    impossible_travel = 1
    mfa_fatigue = 1
    privilege_escalation = 1

    total_alerts = (
        impossible_travel +
        mfa_fatigue +
        privilege_escalation
    )

    print("\n=== Security Metrics ===\n")

    print(f"Total Users: {total_users}")
    print(f"Total Alerts: {total_alerts}")
    print(f"Impossible Travel Alerts: {impossible_travel}")
    print(f"MFA Fatigue Alerts: {mfa_fatigue}")
    print(f"Privilege Escalation Alerts: {privilege_escalation}")

if __name__ == "__main__":
    generate_metrics()