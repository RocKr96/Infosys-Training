# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:22:14 2018

@author: Aman Zadafiya
"""

import cx_Oracle
con=cx_Oracle.connect("system/amanpz123@xe")
cur=con.cursor()
try:
    
    cur.execute("""CREATE TABLE supplier(
            supplierid VARCHAR2(6) PRIMARY KEY,
            suppliername VARCHAR2(30),
            suppliercontactno varchar2(15),
            supplieremailid VARCHAR2(30))
            """)
except Exception:
    print(Exception)
finally:
    con.commit()
    con.close()