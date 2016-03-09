import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    inventory = [
        ('Ford', 'T-1', 2000),
        ('Hondas', 'B-1', 1280),
        ('Ford', 'T-2', 4000),
        ('Ford', 'T-3', 3600),
        ('Hondas', 'B-2', 2900)
    ]
    c.executemany("INSERT INTO inventory(Manufacturer, Model, Quantity) VALUES(?, ?, ?)", inventory)