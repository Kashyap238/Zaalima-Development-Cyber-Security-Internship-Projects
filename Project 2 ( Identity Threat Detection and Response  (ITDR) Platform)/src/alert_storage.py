import sqlite3

def save_alert(
    user,
    alert_type,
    risk_score
):

    conn = sqlite3.connect("itdr.db")

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