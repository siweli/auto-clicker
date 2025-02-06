# imports
import tkinter as tk
import string

from pynput.mouse import Listener, Button, Controller
MListener = Listener
from pynput.keyboard import Listener, KeyCode, Key
KBListener = Listener

# MAIN BUILD
class App:
    # default values
    started = False
    running = False
    delay = 10
    button = Button.left
    getpos_key = Key.f9
    start_key = Key.f10
    stop_key = Key.f11
    exit_key = Key.f12
    default_keys = ["F10", "F11", "F12"]
    
    def __init__(self, root):
        self.master = root

        # standard tkinter set up
        root.title("EasyClicker")
        root.geometry("300x200+1+6")
        root.resizable(False,False)
        root.wm_attributes("-topmost", True)

        # the tkinter menu
        tk.Label(root, text="Settings for autoclicker", font=("Moderne Sans","15")).grid(row = 0, column = 1, pady = 3, columnspan=3)

        tk.Label(root).grid(row = 1, column = 0)
        #tk.Label(root, text="get mouse pos key:").grid()
        tk.Label(root, text="Start key:").grid(row = 2, column = 1, pady = 1)
        tk.Label(root, text="Stop key:").grid(row = 3, column = 1, pady = 1)
        tk.Label(root, text="Exit key:").grid(row = 4, column = 1, pady = 1)

        # entries for custom toggle keys
        for i in range(3):
            entry = tk.Entry(root, width=6)
            entry.grid(row = i+2, column = 2, pady = 1)
            entry.bind("<KeyPress>", self.onKeyPress)
            entry.insert(0, self.default_keys[i])

        tk.Label(root).grid(row = 9, column = 0)
        # start the program button
        self.start_button = tk.Button(root, text="Start", width=7, command=self.start)
        self.start_button.grid(row = 10, column = 4)


        # mouse control
        self.mouse = Controller()
        # setup the listeners
        keyboard_listener = KBListener(on_press=self.on_press)
        mouse_listener = MListener(on_move=self.on_move)
        keyboard_listener.start()
        mouse_listener.start()

    # detects key press in focused entry label (not to be confused with onPress)
    def onKeyPress(self, event):
        def clear():
            event.widget.delete(0,"end")
            event.widget.insert(0,event.keysym)
        self.master.after(1, clear)
        entry = str(event.widget).split("entry")[1]

        # surround if statements is fine but wtf is the if elif spam in between
        if event.keysym in string.ascii_letters + string.digits:
            if entry == "": self.start_key = KeyCode(char=event.keysym)
            elif entry == "2": self.stop_key = KeyCode(char=event.keysym)
            elif entry == "3": self.exit_key = KeyCode(char=event.keysym)
        else:
            for i in Key:
                if event.keysym.upper() == str(i).split(".")[1].upper():
                    if entry == "": self.start_key = i
                    elif entry == "2": self.stop_key = i
                    elif entry == "3": self.exit_key = i



# THE ACTUAL AUTOCLICKER
    def start(self):
        root.focus()
        self.started = True
        self.start_button.config(text="Running")

    """
    def change_mode(self):
        self.mode = not self.mode"""
        
        
    # detects key presses for autoclicker (not to be confused with onKeyPress)
    def on_press(self, key):
        if self.started:
            if key == self.stop_key and self.running:
                print("stopped on stop key")
                self.running = False
                
            elif key == self.start_key and not self.running:
                print("started")
                self.running = True
                self.click_loop()

            elif key == self.getpos_key:
                print("current mouse pos is:", self.mouse.position)
                    
            elif key == self.exit_key:
                print("exited on exit key")
                self.master.destroy()
        
    # detects mouse movement
    def on_move(self, x,y):
        if self.started:
            if self.running: # change to check for mode
                print("stopped on mouse movement")
                self.running = False

    # click loop
    def click_loop(self):
        if self.started:
            if self.running:
                self.mouse.press(self.button)
                self.mouse.release(self.button)
                self.master.after(self.delay, self.click_loop)
 

# START
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()







    
