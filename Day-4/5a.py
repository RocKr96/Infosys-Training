# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:48:56 2018

@author: Aman Zadafiya
"""
import cx_Oracle
try:
    con=cx_Oracle.connect("system/amanpz123@xe")
    cur=con.cursor()
    supplierID='S1003'
    supplierName='Victor Electronics'
    suppliercontactno='115-265-4675'
    supplieremailid='victorelectronics@easy.com'
    cur.execute('INSERT INTO supplier VALUES (:1,:2,:3,:4)',(supplierID,supplierName,suppliercontactno,supplieremailid))
except Exception:
    print(Exception.with_traceback)
else:
    print("Operation successful")
finally:
    con.commit()
    con.close()