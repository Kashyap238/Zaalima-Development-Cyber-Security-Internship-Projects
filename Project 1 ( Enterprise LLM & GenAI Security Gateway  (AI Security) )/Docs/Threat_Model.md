# Threat Model

## Threats Addressed

### 1. PII Leakage
Sensitive information such as emails, phone numbers, Aadhaar numbers, PAN cards, credit cards and IP addresses are detected and sanitized before processing.

### 2. Prompt Injection
The gateway identifies suspicious prompts attempting to bypass security controls or reveal protected instructions.

### 3. Unauthorized Access
API key authentication prevents unauthorized users from accessing the gateway.

### 4. Audit and Compliance
All analyzed requests are logged for future auditing and security investigations.

## Future Improvements

- Microsoft Presidio Integration
- PostgreSQL Logging
- Redis Rate Limiting
- Docker Deployment
- Kubernetes Deployment