import sqlite3

def create_risk_table():

    conn = sqlite3.connect("itdr.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS risk_scores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        risk_score INTEGER
    )
    """)

    conn.commit()
    conn.close()

def save_risk_score(
    user,
    score
):

    conn = sqlite3.connect("itdr.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO risk_scores(
            user,
            risk_score
        )
        VALUES (?, ?)
        """,
        (
            user,
            score
        )
    )

    conn.commit()
    conn.close()