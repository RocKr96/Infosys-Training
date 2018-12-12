# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:09:47 2018

@author: Aman Zadafiya
"""
try:
    fileobj=open("abc.txt","w")
    fileobj.write("world")
    fileobj.read(10)
    print("File Name:",fileobj.name)
    print("File status:",fileobj.closed)
except IOError:
    print("Can't Read/Write file.")
finally:
    print("operation done.")
    fileobj.close()