# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:35:12 2018

@author: Aman Zadafiya
"""

import cx_Oracle
con=cx_Oracle.connect("system/amanpz123@xe")
cur=con.cursor()
try:
    cur.execute("""UPDATE supplier SET supplieremailid='batse@easy.com' where supplierid='S1002'""")
    cur.execute("""delete from supplier where supplierid='S1003'""")
except Exception:
    print(Exception)
else:
    print("Updation Successful")
finally:
    con.commit()
    con.close()
