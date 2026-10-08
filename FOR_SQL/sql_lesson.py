import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (name text, age INT);")

cursor.execute("INSERT INTO users  (name, age) VALUES (?, ?);", ('fedor', 19))
cursor.execute("SELECT * FROM users;")
connection.commit()

cursor.execute("SELECT * FROM users WHERE age = ?;", (19,))
data = cursor.fetchall()
print(data)

cursor.execute("DELETE FROM users WHERE age = ?;", (19,))
connection.commit()
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
print(data)