# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:05:24 2018

@author: Aman Zadafiya
"""

fileobj=open("abc.txt","w")
fileobj.write("hello")
print("File Name:",fileobj.name)
print("File status:",fileobj.closed)
fileobj.close()
fileobj=open("abc.txt","rb")
line=fileobj.read(5)
print("Read file data:",line)
fileobj.close()