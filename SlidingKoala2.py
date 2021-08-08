from tkinter import *
from tkinter import filedialog
import tkinter as tk
import time
from time import sleep
from all_temp_logger import main
# from Sensor_test import sens_test
# from VEML6070 import
# from VEML7700 import
# from TSL2591 import
# from all_light_reader import
import os

# to add matplotlib in central space see below
# https://www.youtube.com/watch?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&v=JQ7QP5rPvjU&feature=youtu.be


# splash screen params #
WIDTH = 1024
HEIGHT = 600
xVelocity = 0
yVelocity = 1.6  # 1.6 ideal #

# framework for app, all other parts added to this #
root = tk.Tk()
window = Tk()
top = Toplevel()
root.resizable(False, False)
top.attributes("-topmost", True)  # sets as topmost screen --> hides the dodgy pop ups I can't get rid of... #

canvas = Canvas(top, width=WIDTH, height=HEIGHT, bg='orange')
canvas.pack()

# planning to make 'sliding' appear one letter at a time as KL slides down --> basic timer + 8 versions of cylinder#.png
background_photo = PhotoImage(file='cylinder3.png')
background = canvas.create_image(400, 512, image=background_photo, anchor='center')

photo_image = PhotoImage(file='KL3.png')
my_image = canvas.create_image(427, 200, image=photo_image, anchor='center')

image_width = photo_image.width()
image_height = photo_image.height()

start_time = time.time()
seconds = 1  # 12 second = full bounce #

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

while True:
    # creates run script function for any buttons that need it
    def runscript(args):
        if args == 1:  # all temp
            os.system(main())


    #    if args == 2:                   # reactor internal temp
    #        os.system(main())
    #    if args == 3:                   # lamp temp
    #        os.system(main())
    #    if args == 4:                   # bottle temp
    #        os.system(main())
    #    if args == 5:                   # all light sensors
    #        os.system(main())
    #    if args == 6:                   # v6070
    #        os.system(main())
    #    if args == 7:                   # v7700
    #        os.system(main())
    #    if args == 8:                   # tsl2591
    #        os.system(main())
    #    if args == 9:                   # basic sensor test
    #        os.system(sens_test())

    # creating function for add custom code button #
    def addCode():
        filename = filedialog.askopenfilename(initialdir="/", title="Select .py file",
                                              filetypes=[("Python files", '*.py')])


    def exec_program():
        program1 = filedialog.askopenfilename(initialdir="/", title="Select .exe file",
                                              filetypes=[("Executable", '*.exe')])
        os.system(program1)


    # creating function for all temp logger button #
    # def run_full_temp_logger():
    # tl1.myfunc()

    root.attributes("-topmost", True)  # sets as topmost screen --> hides the dodgy pop ups I can't get rid of... #

    # Main app canvases #
    canvas1 = tk.Canvas(root, height=600, width=1024, bg="#ecd2fe")
    canvas1.pack()

    # bottom credits bar
    canvas2 = tk.Canvas(root, height=20, width=1024, bg="grey")
    canvas2.pack()
    canvas2.create_text(125, 12, fill="white", font="Times 10 italic bold",
                        text="Support: sghwest@student.liverpool.ac.uk")
    canvas2.create_text(925, 10, fill="orange", font="Times 11 italic bold", text="A Sliding Koala Labs System")

    # canvas3a = tk.Canvas(root, height=20, width=1024, highlightthickness=0, bg="#ecd2fe")
    # canvas3a.place(relx=0, rely=0.04)
    # canvas3a.create_text(55, 10, fill="black", font="Times 11 italic", text="Main programs:")

    canvas3 = tk.Canvas(root, height=20, width=1024, bg="white", highlightbackground="black")
    canvas3.place(relx=0, rely=0.25)
    canvas3.create_text(958, 10, fill="black", font="Times 12 bold", text="Full System Halt!")
    canvas3.create_text(75, 10, fill="black", font="Times 12 bold", text="Fully autonomous")

    canvas4a = tk.Canvas(root, height=20, width=1024, highlightthickness=0, bg="#ecd2fe")
    canvas4a.place(relx=0, rely=0.35)
    canvas4a.create_text(880, 10, fill="black", font="Times 11 bold italic", text="Temperature loggers:")
    canvas4a.create_text(150, 10, fill="black", font="Times 11 bold italic", text="Light loggers:")

    canvas4b = tk.Canvas(root, height=20, width=1024, highlightthickness=0, bg="#ecd2fe")
    canvas4b.place(relx=0, rely=0.6)

    # utility bar banner
    canvas4 = tk.Canvas(root, height=20, width=1024, bg="white")
    canvas4.place(relx=0, rely=0.85)
    canvas4.create_text(32, 12, fill="black", font="Times 11", text="Utilities:")

    # central graph
    graph1 = PhotoImage(file="graph_small.png")  # to be replaced with matplotlib live plot eventually
    canvas6 = tk.Canvas(root, height=279, width=404, bg="green")
    canvas6.place(relx=0.31, rely=0.35)
    canvas6.create_image(4, 4, image=graph1, anchor=NW)

    # top image / pseudo progress bar
    canvas7 = tk.Canvas(root, height=75, width=750, bg="green")
    canvas7.place(relx=0.138, rely=0.09)
    canvas7.create_text(375, 40, fill="orange", font="Times 16 italic bold",
                        text="Cutesy animated koala gif/progress bar"
                             " coming when/if I cba...")

    # top bar/frame params #
    frame = tk.Frame(root, bg="gray")
    frame.place(relwidth=1, relheight=0.04)
    # frame2= tk.Frame(root, bg="gray")
    # frame2.place(relwidth=1, relheight=0.03, rely=0.97)

    # HALT button
    photo = PhotoImage(file="stopsign100x100.png")
    B1 = tk.Button(canvas1, text="Full System HALT", relief="raised", bg="white", fg="red", image=photo,
                   activebackground="black", activeforeground="black", width=100, height=100)
    B1.place(x=905, y=40)

    # RUN button
    BigShinyButton = tk.Button(root, text="GO!", font="Times 25 bold", padx=10, pady=22, fg="black", bg="red",
                               relief="raised", activebackground="Blue", activeforeground="green", )
    BigShinyButton.place(x=20, y=42)

    # custom code button
    openFile = tk.Button(canvas1, text="Import custom code...", padx=10, pady=5, fg="black", bg="yellow",
                         relief="sunken",
                         command=addCode)
    openFile.place(x=615, y=565)

    # launch Thonny IDE button --> facilitate code edit
    openFile = tk.Button(canvas1, text="Launch Thonny IDE...", padx=10, pady=5, fg="black", bg="yellow",
                         relief="sunken")
    openFile.place(x=50, y=565)

    # open terminal button --> facilitate code edit
    openFile = tk.Button(canvas1, text="Launch Terminal...", padx=15, pady=5, fg="black", bg="yellow", relief="sunken")
    openFile.place(x=240, y=565)

    # run sensor test button
    st_button = tk.Button(root, text="Run sensor test...", padx=20, pady=5, fg="black", bg="yellow", relief="sunken",
                          activebackground="white", activeforeground="black", command=lambda: runscript(9))
    st_button.place(x=425, y=565)

    # show README.txt button
    readme_button = tk.Button(root, text="Show README...", padx=25, pady=5, fg="black", bg="yellow", relief="sunken",
                              activebackground="white", activeforeground="black")
    readme_button.place(x=810, y=565)

    # About system button
    def open_Rme():
        top1 = Toplevel()
        top1.geometry("300x500")
        top1.title("toplevel")
        top1.attributes("-topmost", True)
        l2 = Label(top1, text="System information", font="Helvetica 16 bold underline")
        l2.pack()
        l3 = Label(top1, text="\nThis system was designed and brought to fruition by Harvey West during his 2021"
                              " summer internship. Dr Konstantin Luzyanin acting as project supervisor, was a "
                              "continuous source of inspiration, advice, and passionate encouragement, who was never"
                              " afraid to throw his creative spanner in the works. Stephen Moss's door was always open"
                              " for stimulating and productive conversation, facilitating many changes to 'the plan',"
                              " without which, this project would not have succeeded! \n\nWith special thanks to"
                              " Professor Berry and the University of Liverpool's Department of Chemistry for"
                              " generously providing the funding for this project \n\nI wish the best of luck to "
                              "whomever is brave enough to develop this system further... \n\n\nʕ•ᴥ•ʔ",
                   font="Helvetica 10", wraplength=280)
        l3.pack()

    about_sys_button = tk.Button(root, relief="raised", activebackground="black", activeforeground="white",
                                 bitmap="info", command=open_Rme)
    about_sys_button.place(x=1000, y=570)

    # temp loggers

    # run all_temp_logger.py button
    atl_button = tk.Button(root, text="Full system...", font="Times 13 bold", padx=75, pady=6, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(1))
    atl_button.place(x=750, y=260)

    # run internal_reactor.py button
    ril_button = tk.Button(root, text="Reactor internal...", font="Times 13 bold", padx=57, pady=6, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(2))
    ril_button.place(x=750, y=320)

    # run lamp_temp.py button
    ltl_button = tk.Button(root, text="Lamp...", font="Times 13 bold", padx=98, pady=6, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(3))
    ltl_button.place(x=750, y=380)

    # run bottle_temp.py button
    btl_button = tk.Button(root, text="Reagent bottles...", font="Times 13 bold", padx=62, pady=6, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(4))
    btl_button.place(x=750, y=440)

    # light loggers

    # run all_light_logger.py button
    all_button = tk.Button(root, text="All sensors...", font="Times 13 bold", padx=77, pady=6, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                           command=lambda: runscript(5))
    all_button.place(x=20, y=260)

    # run VEML6070.py button
    v6070_button = tk.Button(root, text="VEML6070...", font="Times 13 bold", padx=75, pady=6, fg="black",
                             bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                             command=lambda: runscript(6))
    v6070_button.place(x=20, y=320)

    # run VEML7700.py button
    v7700_button = tk.Button(root, text="VEML7700...", font="Times 13 bold", padx=75, pady=6, fg="black",
                             bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                             command=lambda: runscript(7))
    v7700_button.place(x=20, y=380)

    # run TSL2591.py button
    tsl_button = tk.Button(root, text="TSL2591...", font="Times 13 bold", padx=85, pady=6, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                           command=lambda: runscript(8))
    tsl_button.place(x=20, y=440)

    window.destroy()
    root.mainloop()
