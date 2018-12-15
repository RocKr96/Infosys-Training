# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:54:26 2018

@author: Aman Zadafiya
"""
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
 ('Peter', 'Lowstreet 4'),
 ('Amy', 'Apple st 652'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('Betty', 'Green Grass 1'),
 ('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
 ('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38'),
 ('William', 'Central st 954'),
 ('Chuck', 'Main Road 989'),
 ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()
'''
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#print(mycursor.rowcount, "record was inserted.")