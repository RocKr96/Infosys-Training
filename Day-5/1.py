# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:13:40 2018

@author: Aman Zadafiya
"""
import mysql.connector
import MySQLdb
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")