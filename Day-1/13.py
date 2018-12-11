'''
Assignment 13: Control Structures – Demo
Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem
Problem Description: Suppose the retail store management now wants to provide discount for all bill amounts as mentioned below.
developer:Aman Zadafiya
date & time: 10/12/2018 2:40 PM
'''
bill_id = 1001		#int
customer_id = 101	#int
bill_amount = 1000.0	#float
print("Bill Id:%d" %bill_id)
print("Customer Id:%d" %customer_id)
if bill_amount>=1000:
	discount=5
elif bill_amount>=500:
	discount=2
else:
	discount=1
bill_amount=bill_amount-bill_amount*discount/100	
print("Bill Amount:Rs.%f" %bill_amount)

