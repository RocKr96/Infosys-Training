# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:41:47 2018

@author: Aman Zadafiya
"""
import cx_Oracle
con=cx_Oracle.connect("system/amanpz123@xe")
cur=con.cursor()
try:
    cur.execute("""Select * from supplier""")
    print(cur.description)
    print()
    print(cur.rowcount)
    print(cur.fetchmany(2))
    print(cur.rowcount)
    print (cur.fetchall())
    print(cur.rowcount)
except Exception:
    print(Exception)
else:
    print("operation Successful")
finally:
    con.commit()
    con.close()