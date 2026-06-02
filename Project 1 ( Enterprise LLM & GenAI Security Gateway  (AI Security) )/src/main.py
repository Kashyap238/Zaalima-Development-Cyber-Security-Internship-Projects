from security_gateway import SecurityGateway

gateway = SecurityGateway()

prompt = input("Enter Prompt: ")

findings = gateway.detect_pii(prompt)

sanitized = gateway.sanitize_prompt(prompt)

print("\n===== Security Analysis =====")

if findings:
    for item in findings:
        print("✓", item)
else:
    print("No sensitive data detected")

print("\n===== Sanitized Prompt =====")
print(sanitized)

gateway.save_log(prompt, sanitized, findings)

print("\nAudit log saved successfully.")