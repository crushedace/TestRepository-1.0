from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("KPI Calculator")
root.geometry("1000x400")
buttonCounter = 0
# definitions
def open_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/TestRepository/", title="Open Text File", filetypes=(("Text Files", "*.txt"),))

    text_file = open('KPI Results.txt', 'r')
    variable = text_file.read()

    my_text.insert(END, variable)
    text_file.close()
def save_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/TestRepository/", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open('KPI Results.txt', 'w+')
    text_file.write(my_text.get(1.0, END))
def calculate_button():
    myLabel2["text"] = "Cases Assigned :" + myEntry1.get()
    myLabel3["text"] = "Cases Closed :" + myEntry2.get()
    myLabel4["text"] = "Current KPI :" + myEntry3.get()
    myLabel5["text"] = "Employee Name" + myEntry4.get()

    calculate = (float(myEntry2.get()) / float(myEntry1.get()) * 100)
    text_file = open("KPI Results.txt", "w+")
    text_file.write("Cases Assigned: " + myEntry1.get() + "\n")
    text_file.write("Cases Closed: " + myEntry2.get() + "\n")
    text_file.write("Current KPI: " + myEntry3.get() + "\n")
    text_file.write("Employee Name: " + myEntry4.get() + "\n")
    text_file.close()

    if calculate < float(myEntry3.get()):
        myLabel6["text"] = \
            ("Greetings " + (myEntry4.get()) + ", Unfortunately, you have not met our KPI requirements with "
             + str(calculate) + " % out of " + (myEntry3.get()) + " %")

    elif calculate >= float(myEntry3.get()):
        myLabel6["text"] = \
            ("Greetings " + (myEntry4.get()) + ", Fantastic! You have met our KPI requirements with "
             + str(calculate) + " % out of " + (myEntry3.get()) + " %")
# define widgets
myLabel1 = Label(root, text="Please Input Data")
myLabel2 = Label(root, text="Cases Assigned :")
myLabel3 = Label(root, text="Cases Closed :")
myLabel4 = Label(root, text="Current KPI :")
myLabel5 = Label(root, text="Employee Name: ")
myLabel6 = Label(root, text="KPI Calculated % :")
# my entries
myEntry1 = Entry(root)
myEntry2 = Entry(root)
myEntry3 = Entry(root)
myEntry4 = Entry(root)
# my entries insert
myEntry1.insert(0, " ")
myEntry2.insert(0, " ")
myEntry3.insert(0, " ")
myEntry4.insert(0, " ")
# Button Name Variable // Button // Text = Name on button // command = def button
calc_button = Button(root, text="Calculate!", command=calculate_button)
open_button = Button(root, text="Load File", command=open_txt)
save_button = Button(root, text="Save File", command=save_txt)
# place widgets on screen
# LabelWidgets
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)
myLabel4.grid(row=3, column=0)
myLabel5.grid(row=4, column=0)
myLabel6.grid(row=5, column=0)
# LabelEntries
myEntry1.grid(row=1, column=1, padx=0, pady=0)
myEntry2.grid(row=2, column=1, padx=0, pady=0)
myEntry3.grid(row=3, column=1, padx=0, pady=0)
myEntry4.grid(row=4, column=1, padx=0, pady=0)
# LabelButton
calc_button.grid(row=1, column=2)
open_button.grid(row=2, column=2)
save_button.grid(row=3, column=2)
my_text = Text()
#my_text.grid(row=9, column=0)

root.mainloop()