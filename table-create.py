import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

my_cursor = mydb.cursor(buffered=True)

mytables = my_cursor.execute('SHOW TABLES')

# for x in mytables:
    # if(i == 'users'):
    # print(x)
        # my_cursor.execute("DROP TABLE users")

        

# my_cursor.execute("CREATE TABLE test (id int(11), name varchar(255), address varchar(255), contact varchar(255), email_address varchar(255), password varchar(255), uesr_type tinyint(2)) ")

# my_cursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREAMENT ")

# my_cursor.execute('INSERT INTO test VALUES( 1, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2 )')

query = 'INSERT INTO test (id, name, address, contact, email_address, password, uesr_type) VALUES(%s, %s, %s, %s, %s, %s, %s)'
val = [
        (1, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2 ),
        (2, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (3, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (4, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (5, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (6, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (7, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (8, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2),
        (9, "sarmad", "rt", 23232323, "sarm@d.com", "s$r%TD@!", 2)
    ]
    
my_cursor.executemany(query, val)

print(my_cursor.rowcount , ' rows inserted')
mydb.commit()