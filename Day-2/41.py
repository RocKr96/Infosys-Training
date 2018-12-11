# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:30:18 2018

@author: Aman Zadafiya
"""

def is_palindrom(string):
    S=string.split()
    S=''.join(S)
    if len(S)==1 or len(S)==0:
        return True
    else:
        if S[0]==S[-1] and is_palindrom(S[1:-1]):
            return True
        else:
            return False
string=input("Enter String :")
if is_palindrom(string):
    print("String is Palindrome.")
else:
    print("String is not palindrome.")