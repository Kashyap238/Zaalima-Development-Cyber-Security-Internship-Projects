# API Endpoints Documentation

## Core Endpoints

### GET /

Returns gateway status.

### POST /analyze

Analyzes prompts for:

* PII Detection
* Presidio Detection
* Prompt Injection Detection

### POST /proxy

Routes prompts through the security gateway and mock LLM.

## Security Endpoints

### GET /health

Gateway health status.

### GET /compliance

Compliance monitoring information.

### GET /metrics

Security metrics and statistics.

### GET /dashboard

Current dashboard statistics.

### GET /dashboard/history

Historical dashboard information.

## Access Control

### GET /access

Role Based Access Control (RBAC) verification.

## Rate Limiting

### GET /rate_limit

Request rate limiting check.

## Logging

### GET /audit_logs

View audit logs.

### GET /export_logs

Export database audit logs.

## Response Security

### POST /check_response

Checks generated responses for unsafe content.
