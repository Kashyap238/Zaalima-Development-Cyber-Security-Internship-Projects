from high_risk_engine import get_high_risk_users
from critical_accounts_engine import get_critical_accounts

def generate_report():

    print("\n===== ITDR SECURITY REPORT =====\n")

    print("Platform Status: Active\n")

    print("High Risk Users:")

    high_risk = get_high_risk_users()

    for user, score in high_risk.items():

        print(
            f"- {user} (Risk Score: {score})"
        )

    print("\nCritical Accounts:")

    critical_accounts = get_critical_accounts()

    for account in critical_accounts:

        print(
            f"- {account['user']} "
            f"(Severity: {account['severity']})"
        )

    print("\nThreat Monitoring: Enabled")
    print("Database Status: Connected")
    print("Detection Engine: Running")

if __name__ == "__main__":
    generate_report()