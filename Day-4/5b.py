# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:53:25 2018

@author: Aman Zadafiya
"""

import cx_Oracle 
try:
    con=cx_Oracle.connect("system/amanpz123@xe") 
    cur=con.cursor() 
    supplierID=input("Enter the Supplier ID:") 
    supplierName=input("Enter the Supplier Name:") 
    suppliercontactno=input("Enter the Supplier Contact No.:") 
    supplieremailid=input("Enter the Supplier Email ID:") 
    bindVar={'paramsupID':supplierID,'paramsupName':supplierName,' paramsupcontact':suppliercontactno,'paramsupemail':supplieremailid} 
    cur.execute("""INSERT INTO supplier VALUES  (:paramsupID,:paramsupName,:paramsupcontact,:paramsupemail)""",bindVar) 
except Exception:
    print(Exception)
finally:
    con.commit() 
    con.close() 