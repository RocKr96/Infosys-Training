# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:11:28 2018

@author: Aman Zadafiya
"""
def fact(number):
    if number==0:
        return 1
    else:
        return number*fact(number-1)
n=input("Enter Number:")
while int(n)>0:
    print(fact(int(n)))
    n=input("Enter Number(0 for exit):")
print("Good Bye!!")