import tkinter as tk
import string

from pynput.mouse import Listener, Button, Controller
MListener = Listener
from pynput.keyboard import Listener, KeyCode, Key
KBListener = Listener

# MAIN PROGRAM
class App(tk.Frame):
    # default values
    started = False
    running = False
    delay = 10
    button = Button.left
    circle_key = Key.f7
    clear_key = Key.f8
    
    start_key = Key.f10
    stop_key = Key.f11
    exit_key = Key.f12

    pos_key = Key.f2
    default_keys = ["F10", "F11", "F12"]
    def __init__(self, parent):
        super().__init__(parent)

        # standard menu setup
        parent.title("EasyClicker")
        parent.geometry("300x200+1+6")
        parent.resizable(False,False)
        parent.wm_attributes("-topmost", True)
        
        # setting the menu content
        tk.Label(parent, text="Settings for autoclicker", font=("Moderne Sans","15")).grid(row = 0, column = 1, pady = 3, columnspan=3)

        tk.Label(parent).grid(row = 1, column = 0)
        tk.Label(parent, text="Start key:").grid(row = 2, column = 1, pady = 1)
        tk.Label(parent, text="Stop key:").grid(row = 3, column = 1, pady = 1)
        tk.Label(parent, text="Exit key:").grid(row = 4, column = 1, pady = 1)

        # entries for custom toggle keys
        for i in range(3):
            entry = tk.Entry(parent, width=6)
            entry.grid(row = i+2, column = 2, pady = 1)
            entry.bind("<KeyPress>", self.onKeyPress)
            entry.insert(0, self.default_keys[i])

        tk.Label(parent).grid(row = 9, column = 0)
        # start the program button
        self.start_button = tk.Button(parent, text="Start", width=7, command=self.start)
        self.start_button.grid(row = 10, column = 4)


    def onKeyPress(self, event, parent):
        def clear():
            event.widget.delete(0,"end")
            event.widget.insert(0,event.keysym)
        parent.after(1, clear)
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

    # start
    def start(self, parent):
        parent.focus()
        self.started = True
        self.start_button.config(text="Running")


    # click loop
    def click_loop(self):
        if self.started:
            if self.running:
                self.mouse.press(self.button)
                self.mouse.release(self.button)
                self.master.after(self.delay, self.click_loop)
        
# THE POINTER
class Point(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.p = parent

        parent.attributes('-fullscreen', True)
        parent.config(bg='#012345')
        parent.resizable(False, False)
        parent.overrideredirect(True)
        parent.wm_attributes("-topmost", True)
        parent.wm_attributes("-transparentcolor", "#012345")

    # create a circle at mouse pos
    def create(self,pos):
        print("h")
        label = tk.Label(self.p, text="⭕", bg="#012345", fg="red", font=("Arial", 15), bd=0)
        w, h = label.winfo_reqwidth(), label.winfo_reqheight()
        label.place(x=pos[0]-w//2, y=pos[1]-h//2)



# DETECTION
# detects key presses
def on_press(key):
    if key == app.start_key and not app.running:
        print("started")
        app.running = True
        app.click_loop()

    elif key == app.stop_key and app.running:
        print("stopped on stop key")
        app.running = False

    elif key == App.pos_key:
        point.create(mouse.position)

    elif key == app.clear_key:
        for widget in sub.winfo_children():
            widget.destroy()

    elif key == app.exit_key:
        main.destroy()



# START
if __name__ == "__main__":
    # mouse control
    mouse = Controller()
    # setup the listener
    keyboard_listener = KBListener(on_press=on_press)
    keyboard_listener.start()

    # window set up
    main = tk.Tk()
    sub = tk.Toplevel()

    app = App(main)
    point = Point(sub)

    # mainloop
    tk.mainloop()
    






