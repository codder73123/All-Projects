'''tkinter module tutorial'''
from tkinter import *
root = Tk()
root.geometry("800x400")
root.title("Gui tutorial")
root.config(bg="red")

a = Label(text="My name is ____")
a.pack()
root.mainloop()