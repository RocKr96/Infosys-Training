'''
Assignment 17: Iteration Control Structures - Guided Activity
Objective: Given a real world problem, implement the logic and solve the problem using appropriate constructs (sequential, selection, iteration) using an object oriented programming language (Python)
developer:Aman Zadafiya
date & time: 10/12/2018 3:10 PM
'''
sum_of_int=0
n=input("Enter Number:")
for i in range(1,int(n)+1):
	sum_of_int+=i
print("Sum of First",n,"Integer is=",sum_of_int)

print("\nCalculate Intrest amount Using while.")
amount = 100.0
interest = 0.0
months = 1
while months < 6:
	interest = amount * 0.2
	amount = amount + interest
	months += 1
print(amount)

