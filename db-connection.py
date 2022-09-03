#python -m pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE python_db")

mydbs = mycursor.execute('SHOW DATABASES')

# print(mydbs)
for i in mycursor:
    print(i)