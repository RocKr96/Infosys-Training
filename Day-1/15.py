'''
Assignment 15: Control Structures – Hands – on – Practice

Objective: Given a real world problem be able to understand the need for control structures and operators to implement the logic and solve the problem
Problem Description: The finance department of a company wants to calculate the monthly net pay of one of its employee by finding the income tax to be paid (in Indian Rupees) and the net salary after the income tax deduction. The employee should pay income tax if his monthly gross salary is more than Rs. 10,000 (Indian Rupees) and the percentage of income tax should be considered as 20% of the gross salary. Display the employee id, basic salary, allowances, gross pay, income tax and net pay.

developer:Aman Zadafiya
date & time: 10/12/2018 2:50 PM
'''
emp_id = 1001			#int
basic_salary=15000.0		#float
allowances=6000.0		#float
print("Emp Id\t\t=",emp_id)
print("Salary\t\t=",basic_salary)
print("Allowances\t=",allowances)
gross_pay=basic_salary+allowances
print("Gross pay\t=",gross_pay)
if gross_pay>=10000:
	tax=gross_pay*20/100.0
else:
	tax=0.0
print("Income Tax\t=",tax)
net_pay=gross_pay-tax
print("Net Pay\t\t=",net_pay)
