import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global image, img_label
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        img = ImageTk.PhotoImage(image)
        img_label.config(image=img)
        img_label.image = img

def save_image():
    if image:
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            image.save(save_path)

def edit_image():
    if image:

        image
        image = image.rotate(45)
        img = ImageTk.PhotoImage(image)
        img_label.config(image=img)
        img_label.image = img

app = tk.Tk()
app.title("Image Editor")

menu = tk.Menu(app)
app.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_image)
file_menu.add_command(label="Save", command=save_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Rotate", command=edit_image)

img_label = tk.Label(app)
img_label.pack()

image = None

app.mainloop()
