# PostgreSQL Integration

## Purpose

PostgreSQL can be used for enterprise-grade audit log storage.

## Current Implementation

The project currently uses SQLite for local development and testing.

## Production Migration Plan

1. Install PostgreSQL Server
2. Create security_logs database
3. Replace sqlite3 connection with psycopg2
4. Store audit logs in PostgreSQL
5. Connect dashboard to PostgreSQL

## Benefits

- Scalable storage
- Concurrent access
- Enterprise compliance support
- Better performance for large audit datasets