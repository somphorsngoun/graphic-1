import tkinter as tk
import random


def doOnClick_1(event):
    print("class B")
def doOnClick_2(event):
    print("class C")


# Create an empty window
root = tk.Tk()
root.geometry("600x400")

canvas = tk.Canvas(root)
oval = canvas.create_oval(50, 50, 300, 300, fill="#F39118", tags="myTag")
canvas.tag_bind("myTag", "<Button-1>", doOnClick_1)
canvas.tag_bind("myTag", "<Button-3>", doOnClick_2)# Bind the click



canvas.pack(expand=True, fill='both')
root.mainloop()