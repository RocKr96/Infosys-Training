# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 13:45:57 2018

@author: Aman Zadafiya
"""

from tkinter import Tk, Label, Button
class MyFirstGUI:
    def __init__(self, root):
        self.root = root
        root.title("GUI with Label and Button")
        self.label = Label(root, text="This is our first GUI!")
        self.label.pack()
        self.greet_button = Button(root, text="Greet", command=self.greet)
        self.greet_button.pack()
    def greet(self):
        print("Greetings!")
        root1=Tk()
        root1.title("Thank You")
        root1.button=Button(root,text="OK",command=self.master.withdraw())
        root1.button.pack()
        root1.mainloop()
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()