<<<<<<< HEAD
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
=======
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
>>>>>>> d92f3fe72fe75051ec9c5fbec6414ee191fb5570
