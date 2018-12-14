# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:30:01 2018

@author: Aman Zadafiya
"""

import cx_Oracle 
from tkinter import Tk,Label,Entry,Button
master = Tk() 
master.title("Easy Shop Retail Application") 
Label(master, text="Supplier ID:").grid(row=0) 
Label(master, text="Supplier Name:").grid(row=1)
Label(master, text="Supplier Contact No:").grid(row=2) 
Label(master, text="Supplier Email ID").grid(row=3)
e1 = Entry(master) 
e2 = Entry(master)
e3 = Entry(master) 
e4 = Entry(master) 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1) 
e3.grid(row=2, column=1) 
e4.grid(row=3, column=1) 
def fetchrecord(): 
   con=cx_Oracle.connect("system/amanpz123@xe") 
   cur=con.cursor() 
   supplierID=e1.get() 
   supplierName=e2.get() 
   suppliercontactno=e3.get() 
   supplieremailid=e4.get() 
   cur.execute('INSERT INTO supplier VALUES (:1,:2,:3,:4)',(supplierID,supplierName,suppliercontactno,supplieremailid)) 
   cur.execute('select * from supplier') 
   print(cur.fetchall()) 
   con.commit() 
   con.close() 
Button(master, text='Add', command=fetchrecord).grid(row=4, column=0, sticky='w', pady=4) 
master.mainloop( )