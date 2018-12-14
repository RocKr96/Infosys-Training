# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:31:38 2018

@author: Aman Zadafiya
"""

import cx_Oracle
con=cx_Oracle.connect("system/amanpz123@xe")
cur=con.cursor()
try:
    cur.execute("""INSERT INTO supplier VALUES ('S1005','Giant Store','203-237-2079', 'rachel1@easy.com')""")
    cur.execute("""INSERT INTO supplier VALUES ('S1006','EBATs','115-340-2345','ebats@easy.com')""")
    cur.execute("""INSERT INTO supplier VALUES ('S1007','Shop Zilla','203-123-3456', 'shopzilla@easy.com')""")
    cur.execute("""INSERT INTO supplier VALUES ('S1008','VV Electronics','115-340-6756', 'vvelectronics@easy.com')""")
except Exception:
    print(Exception)
else:
    print("Operation Successful")
finally:
    con.commit()
    con.close()
