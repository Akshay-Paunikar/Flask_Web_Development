import sqlite3

import io
%cd "E:\CodeWithHarry\Flask_Step_by_Step\Flask_SQLLite"

conn = sqlite3.connect('database.db')
print ("created database successfully")

conn.execute('CREATE TABLE STUDENTS(name VARCHAR(50), gender VARCHAR(10), city VARCHAR(50), zipcode INTEGER)')
print("Table Created Successfully")

conn.close()