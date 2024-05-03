import psycopg2
from db.connect_db import *

#get connection from connect_db.py
conn = connect()

# Create a cursor object
cur = conn.cursor()

# Create a new table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE
    )
""")

# Create a new table
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        price TEXT NOT NULL
    )
""")

# Insert some data into the table
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("John Doe", "john@example.com"))
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Jane Smith", "jane@example.com"))

cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Bread", "$4.99"))
cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Steak", "$15.99"))
conn.commit()