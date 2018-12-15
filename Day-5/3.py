# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:11:06 2018

@author: Aman Zadafiya
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="192.168.29.150",
  user="ce1",
  passwd="ce1",
  database="test"
)
mycursor = mydb.cursor()
#mycursor.execute("SHOW DATABASES")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM viva")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)