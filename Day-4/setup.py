# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:34:21 2018

@author: Aman Zadafiya
"""


from cx_Freeze import setup, Executable
setup(
      name="supplier_GUI",
      version="0.1",
      description="test",
      executables=[Executable("17.py")],
)