from tkinter import *
from tkinter import filedialog
import tkinter as tk
import time
from time import sleep
import os

# splash screen params #
WIDTH = 800
HEIGHT = 1024
xVelocity = 0
yVelocity = 1.6 # 1.6 ideal #

# framework for SScreen, all other parts added to this #
root = tk.Tk()
window = Tk()
top = Toplevel()
root.resizable(False, False)
top.attributes("-topmost", True)  # sets as topmost screen --> hides the dodgy pop ups I can't get rid of... #

canvas = Canvas(top, width=WIDTH, height=HEIGHT, bg='orange')
canvas.pack()

background_photo = PhotoImage(file='cylinder3.png')
background = canvas.create_image(400, 512, image=background_photo, anchor='center')

photo_image = PhotoImage(file='KL3.png')
my_image = canvas.create_image(427, 200, image=photo_image, anchor='center')

image_width = photo_image.width()
image_height = photo_image.height()

start_time = time.time()
seconds = 6  # 12 second = full bounce #

while True:
    coordinates = canvas.coords(my_image)
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > seconds:
        sleep(1)
        top.destroy()
        break


# assigning function to add custom code button #
def addCode():
    filename = filedialog.askopenfilename(initialdir="/", title="Select .py file", filetypes=[("Python files", '*.py')])


root.attributes("-topmost", True)  # sets as topmost screen --> hides the dodgy pop ups I can't get rid of... #

# Main app canvases #
canvas1 = tk.Canvas(root, height=800, width=700, bg="#ecd2fe")
canvas1.pack()

canvas2 = tk.Canvas(root, height=20, width=700, bg="grey")
canvas2.pack()
canvas2.create_text(600, 10, fill="white", font="Times 11 italic bold", text="A Sliding Koala Labs System")

canvas3 = tk.Canvas(root, height=20, width=700, bg="white")
canvas3.place(relx=0, rely=0.20)
canvas3.create_text(628, 10, fill="black", font="Times 12 bold", text="Full System Halt!")

# top bar/frame params #
frame = tk.Frame(root, bg="gray")
frame.place(relwidth=1, relheight=0.04)
# frame2= tk.Frame(root, bg="gray")
# frame2.place(relwidth=1, relheight=0.03, rely=0.97)

openFile = tk.Button(canvas1, text="Import custom code...", padx=10, pady=5, fg="black", bg="yellow", relief="raised",
                     command=addCode)
openFile.place(x=550, y=730)

photo = PhotoImage(file="C:\\Python trials\\stopsign100x100.png")
B1 = tk.Button(canvas1, text="Full System HALT", relief="raised", bg="white", fg="red", image=photo,
               activebackground="black", activeforeground="black", width=100, height=100)
B1.place(x=575, y=50)

BigShinyButton = tk.Button(root, text="GO!", font="Times 45 bold", padx=75, pady=75, fg="black", bg="Green",
                           relief="raised", activebackground="Blue", activeforeground="yellow",)
BigShinyButton.place(x=210, y=300)

window.destroy()
root.mainloop()