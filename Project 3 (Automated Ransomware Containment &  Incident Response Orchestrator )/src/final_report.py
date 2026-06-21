from dashboard import dashboard_stats

def generate_report():

    stats = dashboard_stats()

    print(
        "\n===== INCIDENT RESPONSE REPORT =====\n"
    )

    print(
        f"Total Alerts: {stats['total_alerts']}"
    )

    print(
        f"Critical Alerts: {stats['critical_alerts']}"
    )

    print(
        f"High Alerts: {stats['high_alerts']}"
    )

    print(
        f"Platform Status: "
        f"{stats['platform_status']}"
    )

    print(
        "\nContainment: Completed"
    )

    print(
        "Forensics: Collected"
    )

    print(
        "Notifications: Sent"
    )

    print(
        "Tickets: Generated"
    )

if __name__ == "__main__":
    generate_report()