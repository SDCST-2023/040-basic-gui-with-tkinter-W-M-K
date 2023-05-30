#!python3
import tkinter as tk
from tkinter import LEFT, RIGHT

window = tk.Tk()

dog = tk.PhotoImage(file="dog.png")
dogtag = tk.Label(window, image = dog)
label1 = tk.Label(window,text="Pochacco!")
label2 = tk.Label(window,text="A cuddly little puppy!\n From the same creators who brought you Keropi and Kero Kero")

dogtag.grid(row=1,column=1)
label1.grid(row=1,column=2)
label2.grid(row=2,column=1, columnspan=2)

window.mainloop()
exit()