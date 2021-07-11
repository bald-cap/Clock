import tkinter
from tkinter import Tk, Label
from time import strftime

tk = Tk()
tk.title("BIG BEN")
tk.configure(bg ="white")

frame = Label(tk, font=("Arial",30, "bold"), bg="grey", fg="white")
frame.grid(column = 1, row =1)

def update():
    time = strftime("%H: %M: %S %p")
    frame.configure(text= time)
    frame.after(80, update)

update()
tk.mainloop()


import tkinter
from tkinter import Label, Tk
from time import strftime
from PIL import ImageTk

tk =Tk()
root= tkinter.Tk()
tk.title("BIG BEN")
tk.configure(bg="white")

widget = tkinter.Canvas(root, width=600, height = 300)
widget.grid(columnspan=3)

widget= Label(widget, font=("Arial",30,"bold"), bg="gray", fg="white")
widget.grid(column=1, row =1)


def update():
    time = strftime("%H :%M :%S %pm")
    widget.configure(text = time)
    widget.after(80, update)

update()
tk.mainloop()