# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:12:28 2018

@author: Aman Zadafiya
"""
import re
sentence='we are humans'
matched=re.match('(.*) (.*?) (.*)', sentence)
print(matched.groups())