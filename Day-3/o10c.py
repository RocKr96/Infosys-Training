# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:58:44 2018

@author: Aman Zadafiya
"""

class Customer: 
     counter = 1000 
     def __init__(self): 
          Customer.counter = Customer.counter+1 
          self.__customerid=Customer.counter 
     def setcustomerid(self, cid): 
          self.__customerid=cid 
     def getcustomerid(self): 
          return self.__customerid 
     @staticmethod    
     def display(): 
          print("Demo on using Instance, Class and Static Methods.") 
     @classmethod 
     def totalcustomers(cls): 
          return Customer.counter-1000 
Customer.display()  
objcust = Customer() 
print("Customer Id: ", objcust.getcustomerid()) 
objcust2 = Customer() 
print("Customer Id: ", objcust2.getcustomerid()) 
print("Total Customers: ", Customer.totalcustomers())