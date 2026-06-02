import re

text = input("Enter prompt: ")

email_pattern = r'\S+@\S+'
phone_pattern = r'\d{10}'

text = re.sub(email_pattern, '[EMAIL]', text)
text = re.sub(phone_pattern, '[PHONE]', text)

print("\nSanitized Prompt:")
print(text)