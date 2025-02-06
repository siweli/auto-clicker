import time, threading
import tkinter as tk


class App(tk.Tk, threading.Thread):
    def __init__(self):
        #super(App, self).__init__()
        threading.Thread.__init__(self)
        tk.Tk.__init__(self)

        # standard stuff
        self.title("EasyClicker")
        self.geometry("300x320+0+0")
        self.resizable(False,False)
        tk.Label(self, text="Title", font=("Moderne Sans","15")).pack()

        tk.Button(self, text="test button", command=self.hi).pack()

    def hi(self):
        print("hi")

app = App()
