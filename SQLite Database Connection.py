import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY,
name TEXT
)
""")

conn.commit()
conn.close()