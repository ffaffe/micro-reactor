from tkinter import *
import tkinter as tk

top = Toplevel()
top.geometry("200x768+0+0")
top.title("DEMO")


# reliefs and cursors
B1 = tk.Button(top, text ="arrow/flat", relief=FLAT,\
                         cursor="arrow")
B2 = tk.Button(top, text ="circle/raised", relief=RAISED,\
                         cursor="circle")
B3 = tk.Button(top, text ="clock/sunken", relief=SUNKEN,\
                         cursor="clock")
B4 = tk.Button(top, text ="cross/groove", relief=GROOVE,\
                         cursor="cross")
B5 = tk.Button(top, text ="dotbox/ridge", relief=RIDGE,\
                         cursor="dotbox")
B6 = tk.Button(top, text ="exchange", relief=RAISED,\
                         cursor="exchange")
B7 = tk.Button(top, text ="fleur", relief=RAISED,\
                         cursor="fleur")
B8 = tk.Button(top, text ="heart", relief=RAISED,\
                         cursor="heart")
B9 = tk.Button(top, text ="man", relief=RAISED,\
                         cursor="man")
B10 = tk.Button(top, text ="mouse", relief=RAISED,\
                         cursor="mouse")
B11 = tk.Button(top, text ="pirate", relief=RAISED,\
                         cursor="pirate")
B12 = tk.Button(top, text ="plus", relief=RAISED,\
                         cursor="plus")
B13 = tk.Button(top, text ="shuttle", relief=RAISED,\
                         cursor="shuttle")
B14 = tk.Button(top, text ="sizing", relief=RAISED,\
                         cursor="sizing")
B15 = tk.Button(top, text ="spider", relief=RAISED,\
                         cursor="spider")
B16 = tk.Button(top, text ="spraycan", relief=RAISED,\
                         cursor="spraycan")
B17 = tk.Button(top, text ="star", relief=RAISED,\
                         cursor="star")
B18 = tk.Button(top, text ="target", relief=RAISED,\
                         cursor="target")
B19 = tk.Button(top, text ="tcross", relief=RAISED,\
                         cursor="tcross")
B20 = tk.Button(top, text ="trek", relief=RAISED,\
                         cursor="trek")
B21 = tk.Button(top, text ="watch", relief=RAISED,\
                         cursor="watch")

# bitmaps
B22 = tk.Button(top, text ="error", relief=RAISED,\
                         bitmap="error")
B23 = tk.Button(top, text ="gray75", relief=RAISED,\
                         bitmap="gray75")
B24 = tk.Button(top, text ="gray50", relief=RAISED,\
                         bitmap="gray50")
B25 = tk.Button(top, text ="gray25", relief=RAISED,\
                         bitmap="gray25")
B26 = tk.Button(top, text ="gray12", relief=RAISED,\
                         bitmap="gray12")
B27 = tk.Button(top, text ="hourglass", relief=RAISED,\
                         bitmap="hourglass")
B28 = tk.Button(top, text ="info", relief=RAISED,\
                         bitmap="info")
B29 = tk.Button(top, text ="questhead", relief=RAISED,\
                         bitmap="questhead")
B30 = tk.Button(top, text ="question", relief=RAISED,\
                         bitmap="question")
B31 = tk.Button(top, text ="warning", relief=RAISED,\
                         bitmap="warning")

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()
B8.pack()
B9.pack()
B10.pack()
B11.pack()
B12.pack()
B13.pack()
B14.pack()
B15.pack()
B16.pack()
B17.pack()
B18.pack()
B19.pack()
B20.pack()
B21.pack()
B22.pack()
B23.pack()
B24.pack()
B25.pack()
B26.pack()
B27.pack()
B28.pack()
B29.pack()
B30.pack()
B31.pack()


top.mainloop()