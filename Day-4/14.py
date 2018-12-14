# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:32:22 2018

@author: Aman Zadafiya
"""
import cx_Oracle 
con = cx_Oracle.connect("system/amanpz123@xe") 
cur = con.cursor() 
py_RetValue=cur.callfunc('sf_NoOfSupplier',cx_Oracle.NUMBER) 
print ("The total number of employees are ", py_RetValue)
con.commit() 
con.close() 