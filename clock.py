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
