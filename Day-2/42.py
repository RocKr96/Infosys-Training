# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:36:05 2018

@author: Aman Zadafiya
"""

def reverse_str(string):
    if len(string)<=1:
        return string
    else:
        return reverse_str(string[1:])+string[0]
string=input("Enter String :")
print("reverse string of",string,"is:",reverse_str(string))