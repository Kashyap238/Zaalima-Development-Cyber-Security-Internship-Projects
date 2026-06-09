# Deployment Architecture

User
  ↓

FastAPI Security Gateway
  ↓

Security Filters
  ↓

Audit Logging
  ↓

LLM Service

Components:

- Authentication Layer
- Rate Limiting Layer
- PII Detection Layer
- Prompt Injection Detection Layer
- Response Safety Layer
- Logging Layer