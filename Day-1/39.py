# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:51:02 2018

@author: RocKr
"""

def baggage_check(amount):
    if amount>=0 and amount<=40:
        #print("baggage check is pass.")
        return True
    else:
        #print("baggagge check is not pass.")
        return False
def immigration_check(expiry):
    if expiry>=2001 and expiry<=2025:
        #print("Immigration check pass.")
        return True
    else:
        #print("Immigration check fail.")
        return False
def security(status):
    if status:
        #print("Security check pass.")
        return True
    else:
        #print("Security check fail.")
        return False
def traveller(ids,name,amount,expiry,status):
    traveller_id=ids
    traveller_name=name
    print("traveller id:",traveller_id)
    print("traveller_name:",traveller_name)
    if baggage_check(amount) and immigration_check(expiry) and security(status):
        print("Allow Traveller to fly.")
    else:
        print("Denied Traveller for re-checking")
traveller(101,"Aman",20,2015,True)
traveller(102,"MAHI",50,2013,True)
traveller(103,"KAli",35,2030,True)
traveller(104,"Goli",25,2015,False)