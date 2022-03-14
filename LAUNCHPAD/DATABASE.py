from mysql.connector import *

con = connect(
    host='localhost',
    user='root',
    password='Huzefalegend786',
    database='employeedb'
)

cur = con.cursor()

# cur.execute('CREATE DATABASE employeedb')

cur.execute('''
    CREATE TABLE employee(
        Serial int,
        First_Name varchar(255),
        Last_Name varchar(255),
        Date_Of_Birth date,
        From_ varchar(255),
        Username varchar(255),
        Password varchar(255)
    )
''')
