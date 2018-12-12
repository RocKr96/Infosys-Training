# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 01:59:24 2018

@author: Aman Zadafiya
"""

class Base: 
     def __init__(self, v): 
          self.baseVar = v 
          self.var=0 
          print("Base Class init invoked") 
class Der(Base): 
     def __init__(self, v): 
          super().__init__(v) 
          self.derVar=v 
          self.var=0 
          print("Derived class init invoked") 
     def display(self): 
          print("Base variable value: ", self.baseVar) 
          print("Derived variable value: ", self.derVar) 
     def useOfSuper(self): 
          self.var=15 
          print("Base Variable Value -> ", Base.var) 
          print("Derived Variable Value -> ", self.var) 
d = Der(10) 
d.display() 
d.useOfSuper() 