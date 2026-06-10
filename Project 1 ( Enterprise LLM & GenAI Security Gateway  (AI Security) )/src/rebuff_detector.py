import rebuff

def check_prompt(prompt):

    suspicious_keywords = [
        "ignore previous instructions",
        "reveal system prompt",
        "developer mode",
        "bypass security"
    ]

    for keyword in suspicious_keywords:
        if keyword in prompt.lower():
            return True

    return False