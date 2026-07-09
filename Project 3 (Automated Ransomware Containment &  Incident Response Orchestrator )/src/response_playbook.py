#response_playbook.py

from containment_engine import contain_hosts
from user_suspension import suspend_users
from session_revocation import revoke_sessions
from incident_tracker import log_step

def run_playbook():

    print(
        "\n===== INCIDENT RESPONSE PLAYBOOK =====\n"
    )

    contain_hosts()

    log_step(
        "Host Isolation",
        "Completed"
    )
    

    suspend_users()

    log_step(
        "User Suspension",
        "Completed"
    )

    revoke_sessions()

    log_step(
        "Session Revocation",
        "Completed"
    )

    print(
        "\n===== PLAYBOOK COMPLETE ====="
    )

if __name__ == "__main__":
    run_playbook()