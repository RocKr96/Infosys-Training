'''
Assignment 5: Programming constructs in Python - Demo
Objective: Given a real world problem, be able to identify the variables and operators required to solve the problem and implement it using a high level programming language like Python.
developer:Aman Zadafiya
date & time: 10/12/2018 2:05 PM
'''
bill_id = 1001		#int
customer_id = 101	#int
bill_amount = 400.0	#float
print("Bill Id:%d" %bill_id)
print("Customer Id:%d" %customer_id)
if bill_amount>500:
	bill_amount=bill_amount-bill_amount*2/100
else:
	bill_amount=bill_amount-bill_amount*1/100	
print("Bill Amount:Rs.%f" %bill_amount)

