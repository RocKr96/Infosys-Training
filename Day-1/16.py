'''
Assignment 16: Control Structures – Hands – on – Practice

Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem
Problem Description: Problem Description: Extend the program written for Assignment 15 to find the income tax to be paid (In Indian Rupees) and the total salary after the income tax deduction as per the details given in below table.
	Gross Salary (In Indian Rupees)	Income Tax percentage
	Below 5,000			NIL
	5,001 to 10,000			10%
	10,001 to 20,000		20%
	More than 20,000		30%

developer:Aman Zadafiya
date & time: 10/12/2018 3:05 PM
'''
emp_id = 1001			#int
basic_salary=15000.0		#float
allowances=6000.0		#float
print("Emp Id\t\t=",emp_id)
print("Salary\t\t=",basic_salary)
print("Allowances\t=",allowances)
gross_pay=basic_salary+allowances
print("Gross pay\t=",gross_pay)
if gross_pay>=20000:
	tax=30
elif gross_pay>10000:
	tax=20
elif gross_pay>5000:
	tax=10
else:
	tax=0.0
tax_amount=gross_pay*tax/100.0
print("Income Tax\t=",tax_amount)
net_pay=gross_pay-tax
print("Net Pay\t\t=",net_pay)
