import re
from datetime import datetime

def sanitize_prompt(text):
    email_pattern = r'\S+@\S+'
    phone_pattern = r'\d{10}'

    text = re.sub(email_pattern, '[EMAIL]', text)
    text = re.sub(phone_pattern, '[PHONE]', text)

    return text

prompt = input("Enter Prompt: ")

sanitized = sanitize_prompt(prompt)

print("\nSanitized Prompt:")
print(sanitized)

with open("audit_log.txt", "a") as file:
    file.write(f"\n[{datetime.now()}]\n")
    file.write(f"Original: {prompt}\n")
    file.write(f"Sanitized: {sanitized}\n")
    file.write("-" * 50 + "\n")

print("\nLog saved successfully.")