# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 11:56:40 2018

@author: Aman Zadafiya
"""

import cx_Oracle 
con = cx_Oracle.connect("system/amanpz123@xe") 
cur = con.cursor() 
sup_ID ='S1012'
sup_Name ='Gems Stores' 
sup_Contact='123-789-456' 
sup_Email='gemsstores@gmail.com' 
cur.callproc ('sp_Add_Supplier' , [ sup_ID,sup_Name , sup_Contact,sup_Email]) 
con.commit() 
con.close() 