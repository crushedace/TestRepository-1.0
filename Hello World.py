from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Hello World")
root.geometry("400x100")

# definitions
def open_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Hello World/", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open('HelloWorld Database.txt', 'r')
    variable = text_file.read()
    text_file.close()
def save_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Hello World/", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open('HelloWorld Database.txt', 'w+')
def sub_button():
    text_file = open("HelloWorld Database.txt", "w+")
    text_file.write("Username: " + myEntry1.get() + "\n")
    text_file.write("Password: " + myEntry2.get() + "\n")
    text_file.write("Name: " + myEntry3.get() + "\n")
    text_file.close()
# define widgets
myLabel1 = Label(root, text="Username:")
myLabel2 = Label(root, text="Password:")
myLabel3 = Label(root, text="Name:")
# my entries
myEntry1 = Entry(root)
myEntry2 = Entry(root)
myEntry3 = Entry(root)
# my entries insert
myEntry1.insert(0, " ")
myEntry2.insert(0, " ")
myEntry3.insert(0, " ")
# Button Name Variable // Button // Text = Name on button // command = def button
submit_button = Button(root, text="Submit!", command=sub_button)
open_button = Button(root, text="Load File", command=open_txt)
save_button = Button(root, text="Save File", command=save_txt)
# place widgets on screen
# LabelWidgets
myLabel1.grid(row=1, column=0, padx=1, pady=0)
myLabel2.grid(row=2, column=0, padx=1, pady=0)
myLabel3.grid(row=3, column=0, padx=1, pady=0)
# LabelEntries
myEntry1.grid(row=1, column=1, padx=1, pady=0)
myEntry2.grid(row=2, column=1, padx=1, pady=0)
myEntry3.grid(row=3, column=1, padx=1, pady=0)
# LabelButton
submit_button.grid(row=1, column=4, padx=2, pady=0)
open_button.grid(row=2, column=4, padx=2, pady=0)
save_button.grid(row=3, column=4, padx=2, pady=0)

root.mainloop()