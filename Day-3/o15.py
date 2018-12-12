# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 01:35:41 2018

@author: Aman Zadafiya
"""

class Base: 
     def __init__(self): 
          print("Parent init invoked") 
class Derived(Base): 
     def __init__(self): 
          print("Derived init invoked") 
obj = Derived() 