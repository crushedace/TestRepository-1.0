from tkinter import *

root = Tk()
root.title("Hokage Quiz (Naruto) ")
root.geometry("300x200")

# definitions
def yes1():
    print("You are correct!")
def yes2():
    print("You are correct!")
def yes3():
    print("You are incorrect!")
def yes4():
    print("You are incorrect!")
def yes5():
    print("Have a seat, baby faced skywalkah")
def no1():
    print("You are incorrect!")
def no2():
    print("You are incorrect!")
def no3():
    print("You are correct!")
def no4():
    print("You are correct!")
def no5():
    print("Have a seat, baby faced skywalkah")
    print("test")
# define widgets
myLabel1 = Label(root, text=" Is Naruto ?")
myLabel2 = Label(root, text=" tom is tom")
myLabel3 = Label(root, text=" bobobobobobo ")
myLabel4 = Label(root, text=" boruto can solo all of dbz ")
myLabel5 = Label(root, text=" Boruto is the greatest anime/manga of all time  ")
# Button Name Variable // Button // Text = Name on button // command = def button
yes_button1 = Button(root, text="YES", command=yes1)
yes_button2 = Button(root, text="YES", command=yes2)
yes_button3 = Button(root, text="YES", command=yes3)
yes_button4 = Button(root, text="YES", command=yes4)
yes_button5 = Button(root, text="YES", command=yes5)
no_button1 = Button(root, text="NO", command=yes1)
no_button2 = Button(root, text="NO", command=yes2)
no_button3 = Button(root, text="NO", command=yes3)
no_button4 = Button(root, text="NO", command=yes4)
no_button5 = Button(root, text="NO", command=yes5)
# place widgets on screen
# LabelWidgets
myLabel1.grid(row=1, column=0, padx=1, pady=0)
myLabel2.grid(row=2, column=0, padx=1, pady=0)
myLabel3.grid(row=3, column=0, padx=1, pady=0)
myLabel4.grid(row=4, column=0, padx=1, pady=0)
myLabel5.grid(row=5, column=0, padx=1, pady=0)
# LabelButton
yes_button1.grid(row=1, column=2, padx=2, pady=0)
yes_button2.grid(row=2, column=2, padx=2, pady=0)
yes_button3.grid(row=3, column=2, padx=2, pady=0)
yes_button4.grid(row=4, column=2, padx=2, pady=0)
yes_button5.grid(row=5, column=2, padx=2, pady=0)
no_button1.grid(row=1, column=3, padx=2, pady=0)
no_button2.grid(row=2, column=3, padx=2, pady=0)
no_button3.grid(row=3, column=3, padx=2, pady=0)
no_button4.grid(row=4, column=3, padx=2, pady=0)
no_button5.grid(row=5, column=3, padx=2, pady=0)

root.mainloop()