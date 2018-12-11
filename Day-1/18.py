'''
Assignment 18: break statement - Demo
Objective: Given a real world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object oriented programming language (Python)
developer:Aman Zadafiya
date & time: 10/12/2018 3:15 PM
'''
sum_of_int=0
n=input("Enter Number:")
for i in range(1,int(n)+1):
	sum_of_int+=i
	if i==5:
		break;
print("Sum of First",i,"Integer is=",sum_of_int)

