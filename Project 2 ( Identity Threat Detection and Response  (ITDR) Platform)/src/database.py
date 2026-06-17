import sqlite3
from db_config import DB_PATH

def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        alert_type TEXT,
        risk_score INTEGER
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()