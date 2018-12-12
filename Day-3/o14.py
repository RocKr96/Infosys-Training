# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:15:30 2018

@author: Aman Zadafiya
"""

class Customer: 
     def setcustomerid(self, id): 
          self.__customerid = id 
     def setcustomername(self, name): 
          self.__customername=name 
     def getcustomerid(self): 
          return self.__customerid 
     def getcustomername(self): 
          return self.__customername 
class RegularCustomer(Customer): 
     def setdiscount(self, dis): 
          self.__discount=dis 
     def getdiscount(self): 
          return self.__discount 
class PrivilegedCustomer(Customer): 
     def setmemcardtype(self, card): 
          self.__memcardtype=card 
     def getmemcardtype(self): 
          return self.__memcardtype 
objr = RegularCustomer() 
objr.setcustomerid(1001) 
objr.setcustomername('Ram') 
objr.setdiscount(10.0) 
print("Regular Customer Details") 
print("Customer Id: ", objr.getcustomerid()) 
print("Customer Name: ", objr.getcustomername()) 
print("Discount Eligible: ", objr.getdiscount()) 
print("*********") 
objp = PrivilegedCustomer() 
objp.setcustomerid(1002) 
objp.setcustomername("Seetha") 
objp.setmemcardtype("Gold") 
print("Regular Customer Details") 
print("Customer Id: ", objp.getcustomerid()) 
print("Customer Name: ", objp.getcustomername()) 
print("Discount Eligible: ", objp.getmemcardtype())