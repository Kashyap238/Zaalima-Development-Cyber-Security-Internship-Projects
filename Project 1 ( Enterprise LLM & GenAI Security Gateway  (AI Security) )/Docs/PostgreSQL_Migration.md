# PostgreSQL Migration Plan

Current Prototype:
- SQLite Database
- Audit Log Storage
- Security Event Logging

Production Upgrade Plan:
- Replace SQLite with PostgreSQL
- Store audit logs centrally
- Support multi-user access
- Improve scalability

Future Schema:

audit_logs
-----------
id
timestamp
original_prompt
sanitized_prompt
findings

Benefits:
- Better performance
- Enterprise scalability
- Centralized compliance logging