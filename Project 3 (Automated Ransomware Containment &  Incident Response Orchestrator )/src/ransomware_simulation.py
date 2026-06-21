from response_playbook import run_playbook
from forensic_playbook import run_forensic_playbook

def simulate_ransomware():

    print(
        "\n===== RANSOMWARE ATTACK SIMULATION =====\n"
    )

    print(
        "Ransomware detected on PC-001"
    )

    print(
        "\nLaunching Incident Response..."
    )

    run_playbook()

    run_forensic_playbook()

    print(
        "\nRansomware Successfully Contained"
    )

if __name__ == "__main__":
    simulate_ransomware()