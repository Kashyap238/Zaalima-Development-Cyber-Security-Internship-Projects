import re
from datetime import datetime

def detect_pii(text):
    findings = []

    if re.search(r'\S+@\S+', text):
        findings.append("Email Detected")

    if re.search(r'\d{10}', text):
        findings.append("Phone Number Detected")

    return findings

def sanitize_prompt(text):
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)
    text = re.sub(r'\d{10}', '[PHONE]', text)
    return text

prompt = input("Enter Prompt: ")

findings = detect_pii(prompt)
sanitized = sanitize_prompt(prompt)

print("\n=== Security Analysis ===")

if findings:
    for item in findings:
        print("✓", item)
else:
    print("No sensitive data found")

print("\n=== Sanitized Prompt ===")
print(sanitized)

with open("audit_log.txt", "a") as file:
    file.write(f"\n[{datetime.now()}]\n")
    file.write(f"Original: {prompt}\n")
    file.write(f"Sanitized: {sanitized}\n")
    file.write(f"Findings: {findings}\n")
    file.write("-" * 50 + "\n")

print("\nAudit log saved successfully.")