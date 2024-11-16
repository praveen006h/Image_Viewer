from tkinter import *
from PIL import Image, ImageTk
from win32api import GetSystemMetrics
import sys
import os

global file
global directory
global file_list
global cur_file_num

def left_arrow(event=None):
    global cur_file_num
    cur_file_num -= 1
    print(file_list[cur_file_num])
    raw=Image.open(file_list[cur_file_num])
    w,h = raw.size
    if h > 600:
        x = 600/h
        raw= raw.resize((int(w*x),600), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(raw)
    img_label.config(image=img)
    img_label.image = img
    img_label.pack()

    print("left", cur_file_num)

def right_arrow(event=None):
    global cur_file_num
    cur_file_num += 1
    raw=Image.open(file_list[cur_file_num])
    w,h = raw.size
    if h > 600:
        x = 600/h
        raw= raw.resize((int(w*x),600), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(raw)
    img_label.config(image=img)
    img_label.image = img
    img_label.pack()

    print("right", cur_file_num)


scr_width, scr_height = GetSystemMetrics(0), GetSystemMetrics(1)
win = Tk()
win.title("Image Viewer")
win.geometry("%dx%d" % (scr_width, scr_height))
    

file = sys.argv[1]
directory = os.path.dirname(file)
file_list = [directory+"\\"+i for i in os.listdir(directory) if i.endswith(".jpg") or i.endswith(".png")]
cur_file_num = file_list.index(file)


frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


raw=Image.open(file)
w,h = raw.size
if h > 600:
    x = 600/h
    raw= raw.resize((int(w*x),600), Image.ANTIALIAS)
img = ImageTk.PhotoImage(raw)
img_label = Label(frame, image = img)
img_label.pack()

win.bind('<Left>', left_arrow)
win.bind('<Right>', right_arrow)

rt_btn = Button(win, text="Next", command=right_arrow)
rt_btn.place(x=350, y=550)
rt_btn.pack()
lt_btn = Button(win, text="Prev", command=left_arrow)
lt_btn.place(x=300, y=550)
lt_btn.pack()

print(file)
win.mainloop()