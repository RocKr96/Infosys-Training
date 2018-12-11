# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:49:47 2018

@author: Aman Zadafiya
"""
list_size=3
s=[]
def push(s,item):
    if len(s)==list_size:
        print("Stack Overflow")
    else:
        s.append(item)
        print("pushed element",item,"to stack S")
        display_elements()
def pop():
    item=0
    print("Pop operation")
    if len(s)==0:
        print("Stack Underflow")
    else:
        item=s.pop()
        print("Element",item,"is popped")
def display_elements():
    if len(s)>0:
        print("Elements in Stack:",s)
    else:
        print("Stack is empty")
push(s,12)
push(s,4)
push(s,5)
push(s,3)
print(s.pop())
display_elements()
pop()
pop()
push(s,15)
pop()
pop()
pop()