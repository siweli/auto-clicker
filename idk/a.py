# IMPORTS
import tkinter as tk
import string
from pynput.mouse import Listener, Button, Controller
MListener = Listener
from pynput.keyboard import Listener, KeyCode, Key
KBListener = Listener

from random import randint as r



# MAIN PROGRAM
class App(tk.Frame):
    # default values
    on = "#b7fa87"
    off = "#f26161"
    started = False
    running = False
    delay = 10
    button = Button.left

    mode_key = Key.f6
    mode = True
    
    pos_key = Key.f7
    clear_key = Key.f8
    
    start_key = Key.f9
    stop_key = Key.f10
    exit_key = Key.f12

    default_keys = ["F6", "F7", "F8", "F9", "F10", "F12"]
    order = ["Mode key:", "Pos key:", "Clear key:", "Start key:", "Stop key:", "Exit key:"]
    def __init__(self, parent):
        super().__init__(parent)

        self.p = parent

        # standard menu setup
        parent.title("EasyClicker")
        parent.geometry("320x320+1+6")
        parent.resizable(False,False)
        parent.wm_attributes("-topmost", True)
        
        # setting the menu content
        tk.Label(parent, text="Settings for Autoclicker", font=("Moderne Sans","15")).grid(row = 0, column = 1, pady = 3, columnspan=3)
        tk.Label(parent).grid(row = 1, column = 0)
        for i in range(len(self.order)):
            tk.Label(parent, text=self.order[i]).grid(row = i+2, column = 1, pady = 1)

        # entries for custom toggle keys
        for i in range(len(self.default_keys)):
            entry = tk.Entry(parent, width=6)
            entry.grid(row = i+2, column = 2, pady = 1)
            entry.bind("<KeyPress>", self.onKeyPress)
            entry.insert(0, self.default_keys[i])

        # add entry for custom delay
        tk.Label(parent, text="Delay:").grid(row = 8, column = 1, pady = 1)
        self.delay_var = tk.IntVar()
        delay_entry = tk.Entry(parent, textvariable=self.delay_var, width=6)
        delay_entry.delete(0,"end")
        delay_entry.insert(0, self.delay)
        delay_entry.grid(row = 8, column = 2, pady = 1)
        delay_entry.bind("<Return>", self.get_delay)

        tk.Label(parent).grid(row = 9, column = 0)
        # status labels
        tk.Label(parent, text="Status:").grid(row = 10, column = 0)
        self.run_status = tk.Label(parent, text="Stopped", width=9, bg="#f26161")
        self.run_status.grid(row = 10, column = 1)

        tk.Label(parent, text="Mode:").grid(row = 10, column = 2)
        self.mode_status = tk.Label(parent, text="Autoclicker", width=9, bg="#fabf6b")
        self.mode_status.grid(row = 10, column = 3)

        tk.Label(parent).grid(row = 11, column = 0)
        # start the program button
        self.start_button = tk.Button(parent, text="Start", width=7, command=self.startClicker)
        self.start_button.grid(row = 12, column = 4)

    def get_delay(self, event=0):
        self.delay = self.delay_var.get()
        self.p.focus()

    def onKeyPress(self, event):
        def clear():
            event.widget.delete(0,"end")
            event.widget.insert(0,event.keysym)

        if event.keysym == "Return":
            self.p.focus()
        else:
            self.p.after(1, clear)
            entry = str(event.widget).split("entry")[1]

            # surround if statements is fine but wtf is the if elif spam in between
            # try change this to be cleaner
            if event.keysym in string.ascii_letters + string.digits:
                if entry == "": self.mode_key = KeyCode(char=event.keysym)
                elif entry == "2": self.pos_key = KeyCode(char=event.keysym)
                elif entry == "3": self.clear_key = KeyCode(char=event.keysym)
                elif entry == "4": self.start_key = KeyCode(char=event.keysym)
                elif entry == "5": self.stop_key = KeyCode(char=event.keysym)
                elif entry == "6": self.exit_key = KeyCode(char=event.keysym)
            else:
                for i in Key:
                    if event.keysym.upper() == str(i).split(".")[1].upper():
                        if entry == "": self.mode_key = i
                        elif entry == "2": self.pos_key = i
                        elif entry == "3": self.clear_key = i
                        elif entry == "4": self.start_key = i
                        elif entry == "5": self.stop_key = i
                        elif entry == "6": self.exit_key = i

    # start the clicker program
    def startClicker(self):
        self.p.focus()
        self.get_delay()
        self.started = True
        self.start_button.config(text="Running")

    # click loop for at current mouse pos
    def click_loop(self):
        if self.started:
            if self.running:
                pos = ( mouse.position[0]+r(-10,10),   mouse.position[1]-100+r(-5,5) )
                mouse.position = pos
                self.p.after(self.delay, self.click_loop)


# DETECTION
# detects key presses and if they match any toggle keys
def on_press(key):        
    if app.started:
        if key == app.start_key and not app.running:
            app.running = True
            app.run_status.config(text="Started", bg=app.on)
            app.click_loop()

        elif key == app.stop_key and app.running:
            app.run_status.config(text="Stopped", bg=app.off)
            app.running = False

        elif key == app.exit_key:
            main.destroy()
            keyboard_listener.stop()
            mouse_listener.stop()

# detects mouse movement and if it is not in the saved coords then stop the program
def on_move(x,y):
    if app.started:
        if app.running:
            if app.mode == False:
                if mouse.position not in point.coords:
                    app.run_status.config(text="Stopped", bg=app.off)
                    app.running = False
                    

# START
if __name__ == "__main__":
    # window set up
    main = tk.Tk()

    app = App(main)

    # mouse control
    mouse = Controller()
    # setup the listener
    keyboard_listener = KBListener(on_press=on_press)
    mouse_listener = MListener(on_move=on_move)
    keyboard_listener.start()
    mouse_listener.start()

    # mainloop
    tk.mainloop()
    






