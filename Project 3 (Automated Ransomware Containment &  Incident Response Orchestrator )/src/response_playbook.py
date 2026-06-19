from containment_engine import contain_hosts
from user_suspension import suspend_users
from session_revocation import revoke_sessions

def run_playbook():

    print(
        "\n===== INCIDENT RESPONSE PLAYBOOK =====\n"
    )

    contain_hosts()

    suspend_users()

    revoke_sessions()

    print(
        "\n===== PLAYBOOK COMPLETE ====="
    )

if __name__ == "__main__":
    run_playbook()