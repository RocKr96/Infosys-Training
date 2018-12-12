# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 02:05:22 2018

@author: Aman Zadafiya
"""

class Base: 
     def __init__(self, v): 
          self.baseVar = v 
          print("Base Class init invoked") 
class Der(Base): 
     def __init__(self, v): 
          self.derVar=v 
          print("Derived class init invoked") 
     def display(self): 
          print("Base variable value: ", self.baseVar) 
          print("Derived variable value: ", self.derVar) 
d = Der(10) 
d.display() 