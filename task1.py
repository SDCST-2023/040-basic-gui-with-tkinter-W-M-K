#!python3
import tkinter as tk 
from tkinter.constants import RAISED

window = tk.Tk()
window.geometry("500x40")

box1 = tk.Entry(window,text="Entry", borderwidth=3,relief=RAISED)
label = tk.Label(window,text="X")
box2 = tk.Entry(window,text="Entry", borderwidth=3,relief=RAISED)
button = tk.Button(window,text="=")
box3 = tk.Entry(window,text="Answer", borderwidth=3,relief=RAISED)

box1.grid(row=1,column=1)
label.grid(row=1,column=2)
box2.grid(row=1,column=3)
button.grid(row=1,column=4)
box3.grid(row=1,column=5)
window.mainloop()
exit()