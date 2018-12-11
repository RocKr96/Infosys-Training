'''
Assignment 14: Control Structures - Guided Activity
Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem
Problem Description: Suppose the retail store management now wants to provide discount for all bill amounts as mentioned below.
	Customers can be considered to be valid, if their customer id is between 101 and 1000(both inclusive).
	For valid customers, discount must be provided as per the table given below:
	Bill Amount>=500 Discount % 10
Assume for all other cases, discount is 0%.

developer:Aman Zadafiya
date & time: 10/12/2018 2:45 PM
'''
bill_id = 103		#int
customer_id = 101	#int
bill_amount = 400.0	#float
print("Bill Id:%d" %bill_id)
print("Customer Id:%d" %customer_id)
if bill_amount>=500 or (bill_id>100 and bill_id<=1000):
	discount=10
else:
	discount=0
bill_amount=bill_amount-bill_amount*discount/100	
print("Bill Amount:Rs.%f" %bill_amount)

