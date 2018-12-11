'''
Assignment 32: Lists – Hands - on - Practice

Objective: Given a List of elements representing a computational problem, be able to access elements in different ways using an object oriented language (Python) using an IDE
Problem Description: Write a Python program to generate first ‘n’ Fibonacci numbers. Store the generated Fibonacci numbers in a list and display it.
	Sample input: Enter n 5
	Sample Output: List: [0, 1, 1, 2, 3]
developer:Aman Zadafiya
date & time: 11/12/2018 12:35 PM
'''
currancy=[4,3,2,5,6,4,7,8]
for i in range(0,len(currancy)):
	for j in range(0,len(currancy)-1):
		if(currancy[j]<currancy[j+1]):
			currancy[j],currancy[j+1]=currancy[j+1],currancy[j]
print(currancy)