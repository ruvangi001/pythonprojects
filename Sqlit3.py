import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#create table in triple quotes
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

#inserting data in double quotes
cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",("Ruvangi",25))
cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",("Krishna",30))

conn.commit()

#retrive the data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())