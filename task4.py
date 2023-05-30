#!python3
import tkinter as tk
from tkinter import LEFT, RIGHT

window = tk.Tk()
window.geometry("350x150")

dog = tk.PhotoImage(file="dog.png")
dogtag = tk.Label(window, image = dog)
label1 = tk.Label(window,text="Pochacco!")
label2 = tk.Label(window,text="A cuddly little puppy!\n From the same creators who brought you Keropi and Kero Kero")

dogtag.place(x = 120, y = 0)
label1.place(x = 200, y = 40)
label2.place(x = 0, y = 100)

window.mainloop()
exit()