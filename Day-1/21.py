'''
Assignment 21: Strings – Observations from Retail Application-Guided Activity

Objective: Observe the need for features in the retail application scenario to correlate the application of Strings Problem Description: In the retail application, along with the earlier details included for Customer, the retail shop wants to keep track of customer name. Customer name should be between 3 and 20 characters.

developer:Aman Zadafiya
date & time: 10/12/2018 3:25 PM
'''
name=input("Enter Customer Name:")
if len(name)>=3 and len(name)<=20:
	print("Name is Valid")
else:
	print("Name Is Invalid,it's length should be between 3 to 20.")
