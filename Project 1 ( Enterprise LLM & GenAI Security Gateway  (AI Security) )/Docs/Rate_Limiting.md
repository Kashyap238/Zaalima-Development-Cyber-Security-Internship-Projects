# Rate Limiting

## Objective
Prevent API abuse and excessive requests from users.

## Implementation

A basic rate limiting mechanism was implemented using a Python dictionary.

Each user is tracked based on their username.

After 5 requests:

Status: Blocked

Message:
Rate Limit Exceeded

## Benefits

- Prevents brute force attempts
- Prevents API abuse
- Improves service availability
- Demonstrates security gateway controls