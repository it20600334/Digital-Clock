from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()

root.title("CLOCK")

def time():
    string = strftime('%H : %M : %S %p')
    lable.config(text=string)
    lable.after(1000, time())


lable = Label (root, font = ("DS-Digital", 80), background= "black", foreground= "aqua")
lable.pack(anchor='center')
time()

mainloop()




