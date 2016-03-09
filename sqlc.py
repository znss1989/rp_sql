import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    # Insert multiple records using a tuple
    cities = [
        ('Boston', 'MA', 600000),
        ('Chicago', 'IL', 270000),
        ('Houston', 'TX', 210000),
        ('Phoenix', 'AZ', 150000)
    ]

    # Insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)