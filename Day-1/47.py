# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:01:57 2018

@author: Aman Zadafiya
"""
s=[]
def display_elements():
    if len(s)>0:
        print("Elements in Stack:",s)
    else:
        print("Stack is empty")
s.append(10)
s.append(30)
s.append(45)
s.append(15)
s.append(35)
print(s.pop(-2))
print(s.pop(-2))