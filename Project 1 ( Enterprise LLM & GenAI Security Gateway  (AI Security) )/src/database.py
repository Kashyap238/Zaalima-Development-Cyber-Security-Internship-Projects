#database.py

import sqlite3

def create_database():

    conn = sqlite3.connect("security_logs.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_prompt TEXT,
        sanitized_prompt TEXT,
        findings TEXT
    )
    """)

    conn.commit()
    conn.close()