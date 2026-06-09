#security_gateway.py

import re
import sqlite3
from datetime import datetime

dashboard_stats = {
    "total_requests": 0,
    "pii_detections": 0,
    "prompt_injections": 0,
    "blocked_requests": 0
}

class SecurityGateway:

    def detect_pii(self, text):
        findings = []

        if re.search(r'\S+@\S+', text):
            findings.append("Email Detected")

        if re.search(r'\d{10}', text):
            findings.append("Phone Number Detected")

        if re.search(r'\b\d{16}\b', text):
            findings.append("Credit Card Detected")

        if re.search(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', text):
            findings.append("PAN Card Detected")

        if re.search(r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b', text):
            findings.append("Formatted Credit Card Detected")

        if re.search(r'\b\d{4}\s?\d{4}\s?\d{4}\b', text):
            findings.append("Aadhaar Detected")

        if re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text):
            findings.append("IP Address Detected")

        if findings:
            dashboard_stats["pii_detections"] += 1

        return findings

    def sanitize_prompt(self, text):
        text = re.sub(r'\S+@\S+', '[EMAIL]', text)
        text = re.sub(r'\d{10}', '[PHONE]', text)
        text = re.sub(r'\b\d{16}\b', '[CREDIT_CARD]', text)
        text = re.sub(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b','[PAN]',text)
        text = re.sub(r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b','[CREDIT_CARD]',text)
        text = re.sub(r'\b\d{4}\s?\d{4}\s?\d{4}\b','[AADHAAR]',text)
        text = re.sub(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b','[IP_ADDRESS]',text)
        return text

    def save_log(self, original, sanitized, findings):

        with open("audit_log.txt", "a") as file:

            file.write(f"\n[{datetime.now()}]\n")
            file.write(f"Original: {original}\n")
            file.write(f"Sanitized: {sanitized}\n")
            file.write(f"Findings: {findings}\n")
            file.write("-" * 50 + "\n")

    def detect_prompt_injection(self, text):

        suspicious_keywords = [
            "ignore previous instructions",
            "reveal passwords",
            "forget all instructions",
            "bypass security",
            "reveal system prompt",
            "developer mode",
            "show confidential data",
            "export database",
            "dump credentials",
            "leak customer records",
            "reveal api keys"
        ]

        findings = []

        text_lower = text.lower()

        for keyword in suspicious_keywords:
            if keyword in text_lower:
                findings.append("Prompt Injection Attempt Detected")

        if findings:
            dashboard_stats["prompt_injections"] += 1

        return findings
    
    def save_to_database(
        self,
        original,
        sanitized,
        findings
        ):

        conn = sqlite3.connect("security_logs.db")

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO audit_logs
            (
                original_prompt,
                sanitized_prompt,
                findings
            )
            VALUES (?, ?, ?)
            """,
            (
                original,
                sanitized,
            str(findings)
            )
        )

        conn.commit()
        conn.close()

    def detect_unsafe_response(self, text):

        blocked_keywords = [
            "malware",
            "ransomware",
            "keylogger",
            "steal passwords",
            "exploit code"
        ]

        findings = []

        text_lower = text.lower()

        for keyword in blocked_keywords:
            if keyword in text_lower:
                findings.append("Unsafe Response Detected")

        return findings