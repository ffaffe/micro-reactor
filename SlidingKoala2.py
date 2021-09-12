from tkinter import *
from tkinter import filedialog
import tkinter as tk
# from tkinter.ttk import *
import time
from time import sleep
from all_temp_logger import main
from ril import main1
from PIL import Image
import PIL
# from PIL import ImageTk, Image      # pip3 install Pillow
# from Sensor_test import sens_test
# from VEML6070 import
# from VEML7700 import
# from TSL2591 import
# from all_light_reader import
from precon_input import precon_inp
import os
import glob

# making created/inputted variables globally accessible --> success!
# precon entries
global e_ri
global e_rb1
global e_ifr
# final entries
global e_ri_f
global e_rb1_f
global e_ifr_f

# defining temp sensors being used and creating temp values
# considering removing direct read and replacing with csv read
# ts_psu = "/sys/bus/w1/devices/28-00000bc6e47d/w1_slave"
# ts_ri = "/sys/bus/w1/devices/28-00000bc6e47d/w1_slave"
# ts_lamp = "/sys/bus/w1/devices/28-00000bc6e47d/w1_slave"

# f = open(ts_psu, "r")
# data = f.read()
# f.close()
# (discard, sep, reading) = data.partition(' t=')
# t_psu = float(reading) / 1000.0

# f = open(ri_psu, "r")
# data = f.read()
# f.close()
# (discard, sep, reading) = data.partition(' t=')
# t_ri = float(reading) / 1000.0

# f = open(ts_lamp, "r")
# data = f.read()
# f.close()
# (discard, sep, reading) = data.partition(' t=')
# t_lamp = float(reading) / 1000.0

# test values below
t_psu = 1
t_ri = 1
t_lamp = 1
t_rb1 = 1


# t_ri != e_ri and t_rb1 != e_rb1:

# to add matplotlib in central space see below
# https://www.youtube.com/watch?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&v=JQ7QP5rPvjU&feature=youtu.be


# splash screen params #
WIDTH = 1366
HEIGHT = 768
xVelocity = 0
yVelocity = 1  # 1 ideal #

# framework for app, all other parts added to this #
root = tk.Tk()
window = Tk()
top = Toplevel()
root.resizable(False, False)
top.attributes("-topmost", True)  # sets as topmost screen --> hides the dodgy pop ups I can't get rid of... #

canvas = Canvas(top, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

# planning to make 'sliding' appear one letter at a time as KL slides down --> basic timer + 8 versions of cylinder#.png
background_photo = PhotoImage(file='gif_1.gif')
# PIL.Image.new(mode="RGB", size=(WIDTH, HEIGHT))
background = canvas.create_image(0, 0, image=background_photo, anchor=NW)
# background_photo.seek(6)
# background_photo.show()

# with Image.open("gif_1.gif") as background_photo:
#   background_photo.seek(1)

#  try:
#     while 1:
#        background_photo.seek(background_photo.tell()+1)
# except EOFError:
#      pass

photo_image = PhotoImage(file='KL3.png')
my_image = canvas.create_image(150, 150, image=photo_image, anchor='center')
image_width = photo_image.width()
image_height = photo_image.height()

start_time = time.time()
seconds = 0.5  # 12 second = full bounce #

while True:
    coordinates = canvas.coords(my_image)
    # if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
    #    xVelocity = -xVelocity
    # if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
    #    yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)
    current_time = time.time()
    elapsed_time = current_time - start_time
    #  if 1 < elapsed_time < 2:
    #     photo_image = PhotoImage(file='bg1_s.png')
    #    canvas.move(my_image, xVelocity, yVelocity)
    #      window.update()
    if elapsed_time > seconds:
        sleep(1)
        top.destroy()
        break

# temperature warnings --> set values below for safety
while True:
    if t_psu >= 80:
        temp_warn1 = Toplevel(bg='red', bd=20)
        temp_warn1.geometry("1000x200+0+0")
        temp_warn1.title("Temperature warning")
        temp_warn1.attributes("-topmost", True)
        temp_warn_psu1 = Label(temp_warn1, text='''*** Warning ***''',
                               font="Helvetica 40 bold underline")
        temp_warn_psu1.place(x=300, y=0)
        temp_warn_psu2 = Label(temp_warn1, text='''Abnormal temperature detected in:''',
                               font="Helvetica 27 bold")
        temp_warn_psu2.place(x=175, y=65)
        temp_warn_psu3 = Label(temp_warn1, text='''Power supply unit (>80 \u2070C)''',
                               font="Helvetica 27 bold ")
        temp_warn_psu3.place(x=250, y=110)

    if t_ri >= 100:
        temp_warn1 = Toplevel(bg='red', bd=20)
        temp_warn1.geometry("1000x200+0+0")
        temp_warn1.title("Temperature warning")
        temp_warn1.attributes("-topmost", True)
        temp_warn_psu1 = Label(temp_warn1, text='''*** Warning ***''',
                               font="Helvetica 40 bold underline")
        temp_warn_psu1.place(x=300, y=0)
        temp_warn_psu2 = Label(temp_warn1, text='''Abnormal temperature detected in:''',
                               font="Helvetica 27 bold")
        temp_warn_psu2.place(x=175, y=65)
        temp_warn_psu3 = Label(temp_warn1, text='''Reactor internal (>100 \u2070C)''',
                               font="Helvetica 27 bold ")
        temp_warn_psu3.place(x=255, y=110)

    if t_lamp >= 80:
        temp_warn1 = Toplevel(bg='red', bd=20)
        temp_warn1.geometry("1000x200+0+0")
        temp_warn1.title("Temperature warning")
        temp_warn1.attributes("-topmost", True)
        temp_warn_psu1 = Label(temp_warn1, text='''*** Warning ***''',
                               font="Helvetica 40 bold underline")
        temp_warn_psu1.place(x=300, y=0)
        temp_warn_psu2 = Label(temp_warn1, text='''Abnormal temperature detected in:''',
                               font="Helvetica 27 bold")
        temp_warn_psu2.place(x=175, y=65)
        temp_warn_psu3 = Label(temp_warn1, text='''Lamp (>80 \u2070C)''',
                               font="Helvetica 27 bold ")
        temp_warn_psu3.place(x=350, y=110)


    # creates run script function for any buttons that need it
    def runscript(args):
        if args == 1:  # all temp
            os.system(main())
        if args == 2:  # reactor internal temp
            os.system(main1())


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

    # creating function for buttons #
    def addCode():
        filename = filedialog.askopenfilename(initialdir="/", title="Select .py file",
                                              filetypes=[("Python files", '*.py')])


    def exec_program():
        program1 = filedialog.askopenfilename(initialdir="/", title="Select .exe file",
                                              filetypes=[("Executable", '*.exe')])
        os.system(program1)

    # manual mode screens/funtions
    def manual_mode():
        man_mode_scr = Toplevel(bg="#E8FFFF")
        man_mode_scr.geometry("1366x768+0+0")
        man_mode_scr.title("Manual reactor control...")
        man_mode_scr.attributes("-topmost", True)

        ri_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=120,
                         highlightbackground="green", highlightcolor="red", label="Internal reactor temperature",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        ri_slide.place(x=25, y=25)

        rb1_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=100,
                         highlightbackground="green", highlightcolor="red", label="Reagent bottle 1 temperature",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        rb1_slide.place(x=25, y=175)

        rb2_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=100,
                         highlightbackground="green", highlightcolor="red", label="Reagent bottle 2 temperature",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        rb2_slide.place(x=25, y=325)

        rb3_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=100,
                         highlightbackground="green", highlightcolor="red", label="Reagent bottle 3 temperature",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        rb3_slide.place(x=25, y=475)

        lamp_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=1,
                         highlightbackground="green", highlightcolor="red", label="Lamp",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=150, tickinterval=1, troughcolor="Blue")
        lamp_slide.place(x=770, y=25)

        fr1_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=100,
                         highlightbackground="green", highlightcolor="red", label="Flow rate 1",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        fr1_slide.place(x=770, y=175)

        fr2_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=100,
                         highlightbackground="green", highlightcolor="red", label="Flow rate 2",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        fr2_slide.place(x=770, y=325)

        fr3_slide = Scale(man_mode_scr, bg="black", bd=10, digits=5, font="Helvetica 16", fg="white", from_=0, to_=100,
                         highlightbackground="green", highlightcolor="red", label="Flow rate 3",
                         length=550, width=10, orient=HORIZONTAL, relief=SUNKEN, repeatdelay=400, resolution=1,
                         sliderlength=50, tickinterval=20, troughcolor="green")
        fr3_slide.place(x=770, y=475)



















    # first full auto function --> precondition window/input/setup
    def open_precon_window():
        def print_e1e2():
            global e_ri  # creating global variables from entries
            global e_rb1
            global e_ifr
            e_ri = entry1.get()
            e_rb1 = entry2.get()
            e_ifr = entry3.get()
            sleep(0.5)
            confirm_splash = Toplevel()
            confirm_splash.geometry("1366x768+0+0")
            confirm_splash.title("Preconditioning confirmation...")
            confirm_splash.attributes("-topmost", True)
            confirm_splash_l1 = Label(confirm_splash, text="Please review the provided inputs summarised below."
                                                           " \n\n\n\n\n\n\n\n\n\n\nIn the event of errors, please"
                                                           " close this window, return to the app home screen and"
                                                           " restart the program.",
                                      font="Helvetica 20 bold")
            confirm_splash_l1.place(x=0, y=25)
            confirm_splash_l2a = Label(confirm_splash, text="Temperature(s) (\u2070C):", font="Helvetica 18 underline",
                                       justify=CENTER)
            confirm_splash_l2a.place(x=550, y=100)
            confirm_splash_l2 = Label(confirm_splash, text="\nReactor internal = {} "
                                                           "\nReagent bottle 1 = {} ".format(e_ri, e_rb1),
                                      font="Helvetica 16", justify=CENTER)
            confirm_splash_l2.place(x=600, y=130)
            confirm_splash_l2b = Label(confirm_splash, text="Flow rate(s) (m\u00B3s\u207B\u00B9):",
                                       font="Helvetica 18 underline", justify=CENTER)
            confirm_splash_l2b.place(x=550, y=250)
            confirm_splash_l2e = Label(confirm_splash, text="\nInitial flow rate = {}".format(e_ifr),
                                       font="Helvetica 16", justify=CENTER)
            confirm_splash_l2e.place(x=600, y=280)

            confirm_splash_l3 = Label(confirm_splash, text="-- WARNING --\nDespite the 'fully autonomous' label of this"
                                                           " program and the device it controls, it is NOT intended for"
                                                           " unsupervised operation. \nFurthermore, please ensure all"
                                                           " relevant risk assessments and COSHH requirements for this"
                                                           " experiment have been completed...",
                                      font="Helvetica 21", justify=CENTER, wraplength=WIDTH, fg="red")
            confirm_splash_l3.place(x=0, y=420)  # lol
            # for KL /u1F49A
            confirm_splash_l3 = Label(confirm_splash, text="ʕ•ᴥ•ʔ",
                                      font="Helvetica 24", justify=CENTER, wraplength=1366, fg="Green")
            confirm_splash_l3.place(x=500, y=650)

            # proceed button and next layer of the onion --> warmup screen --. to be followed by hand back to base app
            # ngl, this is because my coding sucks (5 weeks into the pain...)
            def proc_2_warmup():
                if t_ri != e_ri and t_rb1 != e_rb1:
                    sleep(1)
                    confirm_splash.destroy()
                    sleep(0.5)
                    warmup_scr = Toplevel()
                    canvas_wus = Canvas(warmup_scr, width=WIDTH, height=HEIGHT, bg='green')
                    warmup_scr.geometry("1366x768+0+0")
                    warmup_scr.title(
                        "Precondition status viewer")  # possibly/ hopefully make this re-viewable from the app
                    warmup_scr.attributes("-topmost", True)

                    canvas_wus.pack()

                    # proceed button
                    # command possibly to run precon_iheater_func.py
                    button_proc2 = Button(canvas_wus, text="Proceed...", font="Helvetica 14 bold",
                                          pady=20, padx=50, activebackground="black", activeforeground="green",
                                          cursor="tcross",
                                          relief="ridge", bg="grey")
                    button_proc2.place(x=1100, y=650)

                    # quit button in top corner
                    def kill_scr1():
                        sleep(1)
                        warmup_scr.destroy()

                    button_gen_quit = Button(canvas_wus, text="Quit...", font="Helvetica 14 bold",
                                             activebackground="black", activeforeground="red",
                                             cursor="circle", bitmap="error", relief="raised", bg="grey",
                                             command=kill_scr1)
                    button_gen_quit.place(x=1326, y=10)
                    sleep(1)
                    precon_inp_win.destroy()

                else:
                    top.destroy()

            button_proc1 = Button(confirm_splash, text="Proceed...", font="Helvetica 14 bold",
                                  pady=20, padx=50, activebackground="black", activeforeground="green", cursor="tcross",
                                  relief="ridge", bg="grey", command=proc_2_warmup)
            button_proc1.place(x=1100, y=650)

            # chicken out button... what's unicode for *cluck cluck*??
            def kill_scr():
                sleep(1)
                confirm_splash.destroy()

            button_chick_o = Button(confirm_splash, text="Quit...", font="Helvetica 14 bold",
                                    pady=20, padx=50, activebackground="black", activeforeground="red",
                                    cursor="circle", relief="ridge", bg="grey", command=kill_scr)
            button_chick_o.place(x=50, y=650)
            sleep(1)
            precon_inp_win.destroy()

        precon_inp_win = Toplevel()
        precon_inp_win.geometry("750x600+250+150")
        precon_inp_win.title("Preconditioning Setup")
        precon_inp_win.attributes("-topmost", True)
        precon_l1 = Label(precon_inp_win, text="Reactor Preconditioning",
                          font="Helvetica 20 bold underline")
        precon_l1.place(x=200, y=0)
        precon_l1a = Label(precon_inp_win, text="Please enter desired temperatures and estimated initial flow rate"
                           , font="Helvetica 16", justify=LEFT)
        precon_l1a.place(x=0, y=75)

        precon_l2 = Label(precon_inp_win, text="Internal reactor temperature (\u2070C):",
                          font="Helvetica 14", justify=CENTER)
        precon_l2.place(x=0, y=150)
        entry1 = Entry(precon_inp_win, font='Helvetica 16', justify=CENTER, relief="groove")
        entry1.place(x=275, y=200, width=200, height=50)

        precon_l3 = Label(precon_inp_win, text="Reagent bottle 1 (\u2070C):",
                          font="Helvetica 14", justify=CENTER)
        precon_l3.place(x=0, y=250)
        entry2 = Entry(precon_inp_win, font='Helvetica 16', justify=CENTER, relief="groove")
        entry2.place(x=275, y=300, width=200, height=50)

        precon_l4 = Label(precon_inp_win, text="Initial flow rate (m\u00B3s\u207B\u00B9):",
                          font="Helvetica 14", justify=CENTER)
        precon_l4.place(x=0, y=350)
        entry3 = Entry(precon_inp_win, font='Helvetica 16', justify=CENTER, relief="groove")
        entry3.place(x=275, y=400, width=200, height=50)

        button10 = Button(precon_inp_win, text="Confirm selections...", font="Helvetica 16 bold",
                          pady=20, padx=50, activebackground="blue", activeforeground="yellow", command=print_e1e2)
        button10.place(x=200, y=500)


    # precon_inp_win.create_window(200, 140, window=entry1)

    # creating function for all temp logger button #
    # def run_full_temp_logger():
    # tl1.myfunc()

    root.attributes("-topmost", True)  # sets as topmost screen --> hides the dodgy pop ups I can't get rid of... #

    # Main app canvases #
    canvas1 = tk.Canvas(root, height=HEIGHT, width=WIDTH,
                        bg="#E8FFFF")  # F2FEB3, FEF6B3, E4D9FF, D1BFFF, FFF4F4, E8FFFF, ebfff1
    canvas1.pack()

    # bottom credits bar
    canvas2 = tk.Canvas(root, height=20, width=WIDTH, bg="grey")
    canvas2.pack()
    canvas2.create_text(125, 12, fill="black", font="Times 10 italic bold",
                        text="Support: sghwest@student.liverpool.ac.uk")
    canvas2.create_text(1265, 10, fill="orange", font="Times 11 italic bold", text="A Sliding Koala Labs System")

    # canvas3a = tk.Canvas(root, height=20, width=1024, highlightthickness=0, bg="#ecd2fe")
    # canvas3a.place(relx=0, rely=0.04)
    # canvas3a.create_text(55, 10, fill="black", font="Times 11 italic", text="Main programs:")

    canvas3 = tk.Canvas(root, height=20, width=WIDTH, bg="white", highlightbackground="black")
    canvas3.place(relx=0, rely=0.25)
    canvas3.create_text(1260, 10, fill="black", font="Times 12 bold", text="Full System Halt!")
    canvas3.create_text(100, 10, fill="black", font="Times 12 bold", text="Fully autonomous")

    canvas4a = tk.Canvas(root, height=20, width=WIDTH, highlightthickness=0, bg="#E8FFFF")
    canvas4a.place(relx=0, rely=0.3)
    canvas4a.create_text(1215, 7, fill="black", font="Times 11 bold italic", text="Temperature loggers:")
    canvas4a.create_text(1215, 7, fill="black", font="Times 11 bold italic", text="Temperature loggers:")
    canvas4a.create_text(150, 7, fill="black", font="Times 11 bold italic", text="Light loggers:")

    # canvas4b = tk.Canvas(root, height=20, width=WIDTH, highlightthickness=0, bg="#E8FFFF")
    # canvas4b.place(relx=0, rely=0.6)

    # utility bar banner
    canvas4 = tk.Canvas(root, height=20, width=WIDTH, bg="white")
    canvas4.place(relx=0, rely=0.85)
    canvas4.create_text(32, 12, fill="black", font="Times 11", text="Utilities:")

    # central graph
    graph1 = PhotoImage(file="graph_small.png")  # to be replaced with matplotlib live plot eventually
    canvas6 = tk.Canvas(root, height=400, width=700, bg="green")
    canvas6.place(relx=0.24, rely=0.32)
    canvas6.create_image(4, 4, image=graph1, anchor=NW)

    # top image / pseudo progress bar
    canvas7 = tk.Canvas(root, height=75, width=970, bg="green")
    canvas7.place(relx=0.138, rely=0.09)
    canvas7.create_text(500, 40, fill="orange", font="Times 16 italic bold",
                        text="Cutesy animated koala gif/progress bar"
                             " coming when/if I cba...")

    # top bar/frame params #
    frame = tk.Frame(root, bg="gray")
    frame.place(relwidth=1, relheight=0.04)
    # frame2= tk.Frame(root, bg="gray")
    # frame2.place(relwidth=1, relheight=0.03, rely=0.97)

    # HALT button
    photo = PhotoImage(file="stopsign140x140.png")
    B1 = tk.Button(canvas1, text="Full System HALT", relief="raised", bg="white", fg="red", image=photo,
                   activebackground="black", activeforeground="black", width=167, height=140)
    B1.place(x=1175, y=600)

    # RUN button
    BigShinyButton = tk.Button(root, text="GO!", font="Times 25 bold", padx=35, pady=40, fg="black", bg="red",
                               relief="raised", activebackground="Blue", activeforeground="green",
                               command=open_precon_window)
    BigShinyButton.place(x=20, y=42)

    # Manual mode button
    man_mode_button = tk.Button(root, text="Manual reactor control", font="Times 18 bold", padx=35, pady=20,
                                fg="black", bg="green", relief="raised", activebackground="Blue",
                                activeforeground="green", wraplength=100, command=manual_mode)
    man_mode_button.place(x=1175, y=42)

    # custom code button
    openFile = tk.Button(canvas1, text="Import custom code...", padx=10, pady=5, fg="black", bg="yellow",
                         relief="sunken",
                         command=addCode)
    openFile.place(x=615, y=720)

    # launch Thonny IDE button --> facilitate code edit
    openFile = tk.Button(canvas1, text="Launch Thonny IDE...", padx=10, pady=5, fg="black", bg="yellow",
                         relief="sunken")
    openFile.place(x=50, y=720)

    # test  --> DEL LINK IN OPEN TERMINAL BUTTON BELOW/
    def print_precon_entr():
        print(e_ri, e_rb1, e_ifr)


    # open terminal button --> facilitate code edit
    openFile = tk.Button(canvas1, text="Launch Terminal...", padx=15, pady=5, fg="black", bg="yellow", relief="sunken",
                         command=print_precon_entr)
    openFile.place(x=240, y=720)

    # run sensor test button
    st_button = tk.Button(root, text="Run sensor test...", padx=20, pady=5, fg="black", bg="yellow", relief="sunken",
                          activebackground="white", activeforeground="black", command=lambda: runscript(9))
    st_button.place(x=425, y=720)

    # show README.txt button
    readme_button = tk.Button(root, text="Show README...", padx=25, pady=5, fg="black", bg="yellow", relief="sunken",
                              activebackground="white", activeforeground="black")
    readme_button.place(x=810, y=720)


    # About system button
    def open_Rme():
        top1 = Toplevel()
        top1.geometry("300x500")
        top1.title("About")
        top1.attributes("-topmost", True)
        l2 = Label(top1, text="System information", font="Helvetica 16 bold underline")
        l2.pack()
        l3 = Label(top1, text="\nThis system was designed and brought to fruition by Harvey West during his 2021"
                              " summer internship. Dr Konstantin Luzyanin acting as project supervisor, was a "
                              "continuous source of inspiration, advice, and passionate encouragement, who was never"
                              " afraid to throw his creative spanner into the works. Stephen Moss's door was always open"
                              " for stimulating and productive conversation, facilitating many changes to 'the plan',"
                              " without which, this project would not have succeeded! \n\nWith special thanks to"
                              " Professor Berry and the University of Liverpool's Department of Chemistry for"
                              " generously providing the funding for this project \n\nI wish the best of luck to "
                              "whomever is brave enough to develop this system further... \n\n\nʕ•ᴥ•ʔ",
                   font="Helvetica 10", wraplength=280)
        l3.pack()


    about_sys_button = tk.Button(root, relief="raised", activebackground="black", activeforeground="white",
                                 bitmap="info", command=open_Rme)
    about_sys_button.place(x=1000, y=720)

    # temp loggers

    # run all_temp_logger.py button
    atl_button = tk.Button(root, text="Full system...", font="Times 13 bold", padx=75, pady=28, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(1))
    atl_button.place(x=1085, y=260)

    # run internal_reactor.py button
    ril_button = tk.Button(root, text="Reactor internal...", font="Times 13 bold", padx=57, pady=28, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(2))
    ril_button.place(x=1085, y=365)

    # run lamp_temp.py button
    ltl_button = tk.Button(root, text="Lamp...", font="Times 13 bold", padx=98, pady=28, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(3))
    ltl_button.place(x=1085, y=470)

    # run bottle_temp.py button
    btl_button = tk.Button(root, text="Reagent bottles...", font="Times 13 bold", padx=62, pady=28, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="blue",
                           command=lambda: runscript(4))
    btl_button.place(x=1085, y=575)

    # light loggers

    # run all_light_logger.py button
    all_button = tk.Button(root, text="All sensors...", font="Times 13 bold", padx=77, pady=28, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                           command=lambda: runscript(5))
    all_button.place(x=20, y=260)

    # run VEML6070.py button
    v6070_button = tk.Button(root, text="VEML6070...", font="Times 13 bold", padx=75, pady=28, fg="black",
                             bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                             command=lambda: runscript(6))
    v6070_button.place(x=20, y=365)

    # run VEML7700.py button
    v7700_button = tk.Button(root, text="VEML7700...", font="Times 13 bold", padx=75, pady=28, fg="black",
                             bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                             command=lambda: runscript(7))
    v7700_button.place(x=20, y=470)

    # run TSL2591.py button
    tsl_button = tk.Button(root, text="TSL2591...", font="Times 13 bold", padx=85, pady=28, fg="black",
                           bg="grey", relief="ridge", activebackground="white", activeforeground="green",
                           command=lambda: runscript(8))
    tsl_button.place(x=20, y=575)

    window.destroy()
    root.mainloop()
