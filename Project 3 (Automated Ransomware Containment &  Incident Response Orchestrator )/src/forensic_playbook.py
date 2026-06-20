from memory_dump import collect_memory_dump
from forensic_collection import collect_forensics
from chain_of_custody import log_chain_of_custody

def run_forensic_playbook():

    print(
        "\n===== FORENSIC PLAYBOOK =====\n"
    )

    collect_memory_dump()

    collect_forensics()

    log_chain_of_custody()

    print(
        "\n===== FORENSIC COLLECTION COMPLETE ====="
    )

if __name__ == "__main__":
    run_forensic_playbook()