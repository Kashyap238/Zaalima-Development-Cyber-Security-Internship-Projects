#orchestrator.py

from response_playbook import run_playbook
from forensic_playbook import run_forensic_playbook
from ticketing_system import generate_tickets
from notification_system import send_notifications

def run_orchestrator():

    print(
        "\n===== RANSOMWARE IR ORCHESTRATOR =====\n"
    )

    run_playbook()

    run_forensic_playbook()

    generate_tickets()

    send_notifications()

    print(
        "\n===== INCIDENT RESPONSE COMPLETE ====="
    )

if __name__ == "__main__":
    run_orchestrator()