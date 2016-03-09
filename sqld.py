# Import data from CSV
import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    # Open the csv file and assgign it to a variable:
    employees = csv.reader(open("employees.csv", "rU"))
    # Create a new table employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    # Insert data from csv to db
    c.executemany("INSERT INTO employees(firstname, lastname) VALUES(?, ?)", employees)
