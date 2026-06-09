# Redis Rate Limiting Design

Current Prototype:
- Python in-memory rate limiter

Production Upgrade:
- Redis based request counting

Benefits:
- Distributed rate limiting
- Shared counters
- Better scalability
- Cloud deployment support

Future Flow:

User Request
      ↓
Redis Counter Check
      ↓
Allow / Block
      ↓
LLM Gateway