# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:16:53 2018

@author: Aman Zadafiya
"""

class Customer:
    def setcustomerid(self,customerid):
        self.customerid=customerid
    def settelephoneno(self,teleno):
        self.telephoneno=teleno
    def getcustomerid(self):
        return self.customerid
    def gettelephoneno(self):
        return self.telephoneno
custobj=Customer()
custobj.setcustomerid(100)
custobj.settelephoneno(9685458965)
print("Customer id:",custobj.getcustomerid())
print("Telephone o:",custobj.gettelephoneno())