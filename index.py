import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Main Window")

img = ImageTk.PhotoImage(Image.open("Tank-PNG-Pic-Background.png").resize((150,150)))
tk.Label(root, image=img).pack()

def show_msg():
    messagebox.showinginfo("Hello", "This is a messagebox!")

def open_top():
    top = tk.Toplevel(root)
    top.title("Top Window")
    tk.Label(top, text="This is a Top Window").pack()

tk.Button(root, text="Show Message", command=show_msg).pack()
tk.Button(root, text="Open Top Window", command=open_top).pack()

root.mainloop()