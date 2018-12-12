# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:11:10 2018

@author: Aman Zadafiya
"""

class Customer:
    def setcustomerid(self,id):
        self.__customerid=id
    def settelephoneno(self,teleno):
        self.__telephoneno=teleno
    def getcustomerid(self):
        return self.__customerid
    def gettelephoneno(self):
        return self.__telephoneno
custobj=Customer()
custobj.setcustomerid(100)
custobj.settelephoneno(9685458965)
print("Customer id:",custobj.getcustomerid())
print("Telephone o:",custobj.gettelephoneno())