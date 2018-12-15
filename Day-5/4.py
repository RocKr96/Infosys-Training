# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:20:40 2018

@author: Aman Zadafiya
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="192.168.137.174",
  user="root",
  passwd="123",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)