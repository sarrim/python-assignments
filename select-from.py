import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

mycursor = mydb.cursor()

sql = 'SELECT * FROM test WHERE address = %s '
whr = ('rt', )

mycursor.execute(sql,whr)


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
