# Insert command with error handler
import sqlite3

connection = sqlite3.connect("new.db")
c = connection.cursor()

try:
    c.execute("INSERT INTO populations VALUES('New York', 'NY', 820000)")
    c.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
    connection.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

connection.close()