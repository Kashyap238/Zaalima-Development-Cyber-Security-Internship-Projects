import sqlite3

def create_database():

    conn = sqlite3.connect("itdr.db")

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