import sqlite3
from db_config import DB_PATH

def save_alert(
    user,
    alert_type,
    risk_score
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO alerts(
            user,
            alert_type,
            risk_score
        )
        VALUES (?, ?, ?)
        """,
        (
            user,
            alert_type,
            risk_score
        )
    )

    conn.commit()
    conn.close()