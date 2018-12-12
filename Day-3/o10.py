# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:31:38 2018

@author: Aman Zadafiya
"""

class Customer: 
     def __init__(self, cid=1000): 
          self.__customerid=cid+1 
     def setcustomerid(self, cid): 
          self.__customerid=cid 
     def getcustomerid(self): 
          return self.__customerid 
     def totalcustomers(self): 
          return 0 
objcust = Customer() 
print("Customer Id: ", objcust.getcustomerid()) 
objcust2 = Customer() 
print("Customer Id: ", objcust2.getcustomerid()) 