from random import *
from mysql.connector import *

conn = connect(
    host='localhost',
    user='root',
    password='Huzefalegend786',
    database='employeedb'
)
cur = conn.cursor()

serial = int(random()*10000)
