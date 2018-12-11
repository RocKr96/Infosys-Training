'''
Assignment 31: Lists – Hands - on - Practice

Objective: Given a List of elements representing a computational problem, be able to access elements in different ways using an object oriented language (Python) using an IDE
Problem Description: Write a Python program to generate first ‘n’ Fibonacci numbers. Store the generated Fibonacci numbers in a list and display it.
	Sample input: Enter n 5
	Sample Output: List: [0, 1, 1, 2, 3]
developer:Aman Zadafiya
date & time: 11/12/2018 12:25 PM
'''
n=input("Enter n:")
a1=1
a2=1
lis=[]
temp=1
while temp<=int(n):
	if temp<=2:
		lis.append(1)
	else:
		temp1=a2
		a2=a1+a2
		a1=temp1
		lis.append(a2)
	temp=temp+1
print(lis)