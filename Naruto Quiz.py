from tkinter import *

def create_window():
    new_window = Toplevel()

window = Tk()

Button(window,text="New Window",command=create_window).pack()

window.mainloop()