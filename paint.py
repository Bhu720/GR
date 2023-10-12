from tkinter import *

root = Tk()

root.title("Paint Bhudev")

root.geometry("500x1500")

frame1 = Frame(root, height=100, width=1100, bg="red")
frame1.grid(row=0, column=0)

frame2 = Frame(root, height=500, width=1100, bg="yellow")
frame2.grid(row=0, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=8)

def paint():
    canvas.create_oval(100, 100, 120, 120, fill="black")
canvas.bind("<Button-1>", paint())


root.resizable(False, False)
root.mainloop()

