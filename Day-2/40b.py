# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:20:46 2018

@author: Aman Zadafiya
"""

def fibo(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibo(number-1)+fibo(number-2)
n=input("Enter Number:")
while int(n)>0:
    print(fibo(int(n)-1))
    n=input("Enter Number(0 for exit):")
print("Good Bye!!")