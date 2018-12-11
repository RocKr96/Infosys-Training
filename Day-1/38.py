# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:39:23 2018

@author: Aman Zadafiya
"""
def compare(phoenix_to_slc,phoenix_to_tamba):
    if phoenix_to_slc>phoenix_to_tamba:
        print("SLC is far from phoenix compare to tamba,florida")
    elif phoenix_to_slc<phoenix_to_tamba:
        print("Tamba,florida is far from phoenix compare to SLC")
    else:
        print("both distance are eqquevalent.")
compare(150,150)