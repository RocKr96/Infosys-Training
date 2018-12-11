'''
Assignment 20: Iteration Control Structure – Debugging - Guided Activity

Objective: Given a real world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object oriented programming language (Python)
Problem Description: The code given below is written to display all the even numbers between 50 and 80 (both inclusive). Debug the program to get the correct output.

developer:Aman Zadafiya
date & time: 10/12/2018 3:20 PM
'''
print("Even numbers between 50 to 80.")
for i in range(50,81):
	if i%2==0:
		print(i)
print("Using While loop.")
while i>=50:
	if i%2==0:
		print(i)
	i-=2
