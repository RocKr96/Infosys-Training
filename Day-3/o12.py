# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:00:35 2018

@author: Aman Zadafiya
"""

class PrintDetails: 
     def printheader(self, c='*', no=1): 
          print(c * no) 
obj = PrintDetails() 
obj.printheader('#', 10) 
obj.printheader("Report") 
obj.printheader('#' ,10) 
obj.printheader()