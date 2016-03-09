# Insert command
import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York City', 'MY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 8000000)")

# Commit to changes
conn.commit()

conn.close()
