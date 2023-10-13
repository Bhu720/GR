from tkinter import *

def paint(event):
    x = event.x
    y = event.y
    canvas.create_oval(x, y, x + 20, y + 20, fill="black")

root = Tk()
root.title("Paint Bhudev")
root.geometry("1100x500")

frame1 = Frame(root, height=100, width=1100, bg="red")
frame1.grid(row=0, column=0)

frame2 = Frame(root, height=500, width=1100, bg="yellow")
frame2.grid(row=1, column=0)  # Changed row to 1

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)  # Changed column to 0

canvas.bind("<Button-1>", paint)

root.resizable(False, False)
root.mainloop()

