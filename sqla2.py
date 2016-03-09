# Create a database for car

# Import the sqlite3 library
import sqlite3

# Connect to database car
conn = sqlite3.connect("cars.db")

# Get cursor object to execute SQL commands
cursor = conn.cursor()

# Create table inventory
cursor.executescript("""DROP TABLE IF EXISTS inventory;
    CREATE TABLE inventory
    (Manufacturer TEXT,
     Model TEXT,
     Quantity INT);""")

# Close database connection
conn.close()
