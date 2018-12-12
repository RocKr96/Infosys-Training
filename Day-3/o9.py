# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:20:21 2018

@author: Aman Zadafiya
"""

class Customer:
    def __init__(self):
        self.__customerid=0
        self.__customername=None
        self.__telephoneno=[]
    def setcustomerid(self,id):
        self.__customerid=id
    def setcustomername(self,name):
        self.__customername=name
    def settelephoneno(self,teleno):
        self.__telephoneno=teleno
    def getcustomerid(self):
        return self.__customerid
    def getcustomername(self):
        return self.__customername
    def gettelephoneno(self):
        return self.__telephoneno
    def validatecustomername(self):
        if len(self.__customername)>=3 and len(self.__customername)<=20:
            return True
        else:
            return False
custobj=Customer()
print("Customer id:",custobj.getcustomerid())
print("Telephone o:",custobj.gettelephoneno())
print("Customer name:",custobj.getcustomername())