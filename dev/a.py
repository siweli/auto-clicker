from tkinter import *
import random
import string
import pyperclip

root = Tk()
# BackEnd

def copy_to_clipbrd():
    pyperclip.copy(entry1.get())

def password():
    entry1.config(state="normal")
    random_password = random.sample(string.ascii_letters, 15)
    entry1.delete(0, END)
    entry1.insert(0, random_password)
    entry1.config(state="disable")


# FrontEnd
entry1 = Entry(root,width = 40, borderwidth = 20 )
entry1.place(x = 50, y = 35)
btn1 = Button(root, text = "Generate", command = password)
btn1.place(x = 70, y = 85)
btn2 = Button(root, text = "Copy", command = copy_to_clipbrd)
btn2.place(x = 145, y = 85)
root.mainloop()
