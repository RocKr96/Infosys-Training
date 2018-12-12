# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:28:55 2018

@author: Aman Zadafiya
"""
class Customer:
    def __init__(self,customerid,teleno,customername):
        self.__customerid=customerid
        self.__customername=customername
        self.__telephoneno=teleno
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
telephoneno=[9201861311, 9201861321, 9201661311] 
custobj = Customer(1001, telephoneno, "Kevin") 
if(custobj.validatecustomername()): 
     print("Customer Id : ", custobj.getcustomerid()) 
     temp = custobj.gettelephoneno() 
     print("Telephone Nos : ", temp[0], ",", temp[1], ",", temp[2]) 
     print("Customer Name : ", custobj.getcustomername()) 
else: 
     print("Invalid customer name. Customer name must be between 3 and 20 characters")           