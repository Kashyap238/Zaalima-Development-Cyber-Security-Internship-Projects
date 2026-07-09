#forensic_playbook.py

from memory_dump import collect_memory_dump
from forensic_collection import collect_forensics
from chain_of_custody import log_chain_of_custody
from incident_tracker import log_step

def run_forensic_playbook():

    print(
        "\n===== FORENSIC PLAYBOOK =====\n"
    )

    collect_memory_dump()

    log_step(
        "Memory Dump",
        "Completed"
    )

    collect_forensics()

    log_step(
        "Forensic Collection",
        "Completed"
    )

    log_chain_of_custody()

    log_step(
        "Chain of Custody",
        "Completed"
    )

    print(
        "\n===== FORENSIC COLLECTION COMPLETE ====="
    )

if __name__ == "__main__":
    run_forensic_playbook()