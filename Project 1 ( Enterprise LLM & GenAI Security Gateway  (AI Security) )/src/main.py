from security_gateway import SecurityGateway

gateway = SecurityGateway()

while True:

    print("\n===== Enterprise LLM Security Gateway =====")
    print("1. Analyze Prompt")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        prompt = input("\nEnter Prompt: ")

        findings = gateway.detect_pii(prompt)

        prompt_findings = gateway.detect_prompt_injection(prompt)

        findings.extend(prompt_findings)

        sanitized = gateway.sanitize_prompt(prompt)

        print("\n===== Security Analysis =====")

        if findings:
            for item in findings:
                print("✓", item)
        else:
            print("No security issues detected")

        print("\n===== Sanitized Prompt =====")
        print(sanitized)

        gateway.save_log(prompt, sanitized, findings)

        print("\nAudit log saved successfully.")

    elif choice == "2":
        print("Exiting Security Gateway...")
        break

    else:
        print("Invalid Choice")