# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:08:33 2018

@author: Aman Zadafiya
"""

global max_size,elements,rear,front
size=5  
elements=[None]*size
rear=-1
front=0

def is_full():
    global size,elements,rear,front
    if(rear==size-1 ):
        return True
    return False

def is_empty():
    global size,elements,rear,front 
    if(front>rear):
        return True
    return False

def enqueue(data):
    global size,elements,rear,front
    if(is_full()):
        print("FULL")
    else:
         rear+=1
         elements[rear]=data
         print("inserted at front end ::",data)
 
def dequeue():
    global size,elements,rear,front
    if(is_empty()):
        print("empty")
    else:
        data=elements[front]
        front+=1
        print("rear end",data)
        return data

def display():
    global size,elements,rear,front
    print("elemnts in queue")    
dequeue() 
enqueue(20)
enqueue(23)
enqueue(78)
display()
dequeue()
display()
enqueue(78)
enqueue(8)