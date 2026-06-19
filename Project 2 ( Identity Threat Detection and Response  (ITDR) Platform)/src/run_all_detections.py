from impossible_travel import detect_impossible_travel
from mfa_fatigue import detect_mfa_fatigue
from privilege_escalation import detect_privilege_escalation
from brute_force_detection import detect_brute_force
from password_spraying import detect_password_spraying
from token_theft_detection import detect_token_theft

print("\n===== ITDR Detection Engine =====\n")

print("Running Impossible Travel Detection...")
detect_impossible_travel()

print("\nRunning MFA Fatigue Detection...")
detect_mfa_fatigue()

print("\nRunning Privilege Escalation Detection...")
detect_privilege_escalation()

print("\nRunning Brute Force Detection...")
detect_brute_force()

print("\nRunning Password Spraying Detection...")
detect_password_spraying()

print("\n===== Detection Complete =====")

print("\nRunning Token Theft Detection...")
detect_token_theft()