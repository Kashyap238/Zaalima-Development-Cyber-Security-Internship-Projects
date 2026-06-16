import sqlite3

conn = sqlite3.connect("itdr.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM risk_scores"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()