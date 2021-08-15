# importing tkinter module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

# creating tkinter window
top = tk.Tk()

# Progress bar widget
progress = Progressbar(top, orient=HORIZONTAL,
                       length=100, mode='determinate')


# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    top.update_idletasks()
    time.sleep(1)


progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(top, text='Start', command=bar).pack(pady=10)

# infinite loop
mainloop()