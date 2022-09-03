import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

mycursor = db_conn.cursor();

sql = "UPDATE test SET name = 'soomro' where id > 4 limit 5"

mycursor.execute(sql)

db_conn.commit()

print(mycursor.rowcount, ' rows affected')