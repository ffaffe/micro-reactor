# importing tkinter module
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL,
                       length=100, mode='determinate')


# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)


progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(root, text='Start', command=bar).pack(pady=10)

# infinite loop
mainloop()