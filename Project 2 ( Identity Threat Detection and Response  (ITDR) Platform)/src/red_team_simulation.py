from impossible_travel import detect_impossible_travel
from mfa_fatigue import detect_mfa_fatigue
from privilege_escalation import detect_privilege_escalation
from brute_force_detection import detect_brute_force
from password_spraying import detect_password_spraying
from token_theft_detection import detect_token_theft

def run_red_team_simulation():

    print("\n===== RED TEAM SIMULATION =====\n")

    print("Simulating Impossible Travel...")
    detect_impossible_travel()

    print("\nSimulating MFA Fatigue...")
    detect_mfa_fatigue()

    print("\nSimulating Privilege Escalation...")
    detect_privilege_escalation()

    print("\nSimulating Brute Force...")
    detect_brute_force()

    print("\nSimulating Password Spraying...")
    detect_password_spraying()

    print("\nSimulating Token Theft...")
    detect_token_theft()

    print("\n===== SIMULATION COMPLETE =====")

if __name__ == "__main__":
    run_red_team_simulation()