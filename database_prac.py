import sqlite3 #Getting tool you need

conn=sqlite3.connect('mydatabase.db') #opening Database 

cursor=conn.cursor() #picking up a pen
#######################################################
#if wanna use mySQL
#  1. Install and Start XAMPP
# Download and install XAMPP.

# Open XAMPP Control Panel.

# Start:

# ✅ Apache

# ✅ MySQL

# 2. Open phpMyAdmin (XAMPP's MySQL GUI)
# In your browser, go to:

# arduino
# Copy
# Edit
# http://localhost/phpmyadmin
# You’ll see the MySQL interface.

# Click "New" to create a new database (e.g., mydatabase).
#  3. Install MySQL Connector for Python
# Open terminal or command prompt and run:

# bash
# Copy
# Edit
# pip install mysql-connector-python

#  New (MySQL with XAMPP):
# import mysql.connector

# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',           # default XAMPP user
#     password='',           # default XAMPP password is empty
#     database='mydatabase'  # the database you created in phpMyAdmin
# )

# cursor = conn.cursor()
######################################################################

#CREATE TABLE
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')

#INSERT INTO TABLE
# cursor.execute("INSERT INTO users (username, age, email) VALUES ('Alice',30,'alice@example.com')")

# users=[
#     ('Bob',25,'bob@example.com'),
#     ('Charlie',35,'charlie@example.com')
# ]
# cursor.executemany("INSERT INTO users (username, age, email) VALUES (?, ?, ?)", users)

# conn.commit()
print("\n")
print("Unfiltered Data: \n")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(type(rows))
print(rows)
for row in rows:
    print(row)
print("\n")

print("Filtered Data: \n")
cursor.execute("SELECT * FROM users WHERE age > 30")
filter_rows = cursor.fetchall()
for row in filter_rows:
    print(row)

cursor.execute("UPDATE users SET age = 32 WHERE username = 'Alice'") 
cursor.execute("DELETE FROM users WHERE username = 'Bob'")
conn.commit()

