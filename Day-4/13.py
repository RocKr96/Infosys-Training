# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:20:54 2018

@author: Aman Zadafiya
"""
import cx_Oracle 
con = cx_Oracle.connect("system/amanpz123@xe") 
cur = con.cursor() 
py_Out=cur.var(cx_Oracle.NUMBER) 
cur.callproc('sp_Check_SupplierID',['S1001',py_Out]) 
OutValue=py_Out.getvalue() 
if OutValue==0: 
    print ("Supplier does not exist") 
else:  
    print ("Supplier Exist") 
con.commit() 
con.close() 