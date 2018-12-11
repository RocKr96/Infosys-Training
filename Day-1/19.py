'''
Assignment 19: continue statement - Demo
Objective: Given a real world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object oriented programming language (Python)
developer:Aman Zadafiya
date & time: 10/12/2018 3:20 PM
'''
sum_of_int=0
n=input("Enter Number:")
for i in range(1,int(n)+1):
	if i==5:
		continue;
	sum_of_int+=i
print("Sum of First",i,"Integer (except 5th integer) is=",sum_of_int)

