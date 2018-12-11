'''
Assignment 12: Control Structures – Demo
Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem
Problem Description: The scenario discussed in Programming Fundamentals Assignment 5 is revisited here. Suppose the retail store management now wants to provide 2% discount for all bill amounts above Rs.500 and for all other bill amount, a discount of 1%.
developer:Aman Zadafiya
date & time: 10/12/2018 2:40 PM
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

