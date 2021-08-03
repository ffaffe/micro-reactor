import tkinter as tk
from itertools import count, cycle
from tkinter import *
import os
import time

# Splash screen #

# Initial framework of app, all other parts attached to this #
root = Tk()
root.resizable(False, False)

# take a .jpg picture you like, add text with a program like PhotoFiltre
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = "C:\\Python trials\\cat.gif"
# assert os.path.exists(image_file)
# use Tkinter's PhotoImage for .gif files

frameCnt = 12
frames = [PhotoImage(file='C:\\Python trials\\cat.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]


def update(ind):
    frame2 = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame2)
    root.after(1, update, ind)


label = Label(root)
label.pack()
root.after(0, update, 0)

image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=800, width=700, bg="white")
# canvas.create_image(image=image)

# show the splash screen for 5000 milliseconds then destroy
root.after(3000, root.destroy)


# framework of app, all other parts added to this #
root = tk.Tk()
root.resizable(False, False)


# assigning function to add custom code button #
def addCode():
    filename = filedialog.askopenfilename(initialdir="/", title="Select .py file", filetypes=[("Python files", '*.py')])


# background params #
canvas = tk.Canvas(root, height=800, width=700, bg="#ecd2fe")
canvas.pack()

canvas2 = tk.Canvas(root, height=20, width=700, bg="grey")
canvas2.pack()
canvas2.create_text(600, 10, fill="white", font="Times 11 italic bold", text="A Sliding Koala Labs System")

canvas3 = tk.Canvas(root, height=20, width=700, bg="white")
canvas3.place(relx=0, rely=0.20)
canvas3.create_text(628, 10, fill="black", font="Times 12 bold", text="Full System Halt!")

# top bar/frame params #
frame = tk.Frame(root, bg="gray")
frame.place(relwidth=1, relheight=0.04)

openFile = tk.Button(root, text="Import custom code...", padx=10, pady=5, fg="black", bg="yellow", relief="raised",
                     command=addCode)
openFile.place(x=550, y=730)

photo1 = tk.PhotoImage(file="C:\\Python trials\\stopsign100x100.png")
B1 = tk.Button(canvas, text="Full System HALT", relief="raised", bg="white", fg="red", image=photo1,
               activebackground="black", activeforeground="black", width=100, height=100)
B1.place(x=575, y=50)

root.mainloop()
