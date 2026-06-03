# Enterprise LLM & GenAI Security Gateway

## Project Objective

Develop a secure gateway that sits between users and LLMs to prevent sensitive data leakage and prompt injection attacks.

---

## Features Implemented

### 1. FastAPI Gateway
- Created REST API using FastAPI
- Swagger documentation available

### 2. Authentication
- API Key verification
- Unauthorized requests blocked

### 3. PII Detection
- Email Detection
- Phone Number Detection
- Credit Card Detection

### 4. Data Redaction
- Sensitive information replaced with placeholders

### 5. Prompt Injection Detection
- Detects:
  - Ignore previous instructions
  - Reveal system prompt
  - Bypass security
  - Developer mode

### 6. Audit Logging
- Logs:
  - Timestamp
  - Original Prompt
  - Sanitized Prompt
  - Security Findings

---

## Current Status

Week 1:
- Gateway Setup
- Routing
- Authentication
- Logging

Week 2:
- PII Detection
- Data Redaction

Week 3:
- Prompt Injection Detection (Initial Prototype)

---

## Next Steps

- Microsoft Presidio Integration
- Redis Rate Limiting
- PostgreSQL Audit Database
- Dashboard Development
- Docker Deployment