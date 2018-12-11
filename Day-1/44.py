# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:19:08 2018

@author: Aman Zadafiya
"""

item_price=[1050,2200,8575,485,234,150,399]
def max_price(item_price):
    print("Price of costliest item in store is:",max(item_price))
def avg_price(item_price):
    total_price=0
    for i in item_price:
        total_price+=i
    average_price=total_price/len(item_price)
    print("Average price of items is:",average_price)
def sorted_price(item_price):
    item_price.sort(reverse=False)
    print("Ite price in increasing order:",item_price)
max_price(item_price)
avg_price(item_price)
sorted_price(item_price)