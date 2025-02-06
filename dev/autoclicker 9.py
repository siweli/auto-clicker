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
    
    pos_key = Key.f7
    clear_key = Key.f8
    
    start_key = Key.f10
    stop_key = Key.f11
    exit_key = Key.f12

    mode_key = Key.f9
    mode = True

    default_keys = ["F7", "F8", "F10", "F11", "F9", "F12"]
    def __init__(self, parent):
        super().__init__(parent)

        self.p = parent

        # standard menu setup
        parent.title("EasyClicker")
        parent.geometry("300x300+1+6")
        parent.resizable(False,False)
        parent.wm_attributes("-topmost", True)
        
        # setting the menu content
        tk.Label(parent, text="Settings for autoclicker", font=("Moderne Sans","15")).grid(row = 0, column = 1, pady = 3, columnspan=3)

        tk.Label(parent).grid(row = 1, column = 0)
        tk.Label(parent, text="Pos key:").grid(row = 2, column = 1, pady = 1)
        tk.Label(parent, text="Clear key:").grid(row = 3, column = 1, pady = 1)
        tk.Label(parent, text="Start key:").grid(row = 4, column = 1, pady = 1)
        tk.Label(parent, text="Stop key:").grid(row = 5, column = 1, pady = 1)
        tk.Label(parent, text="Mode key:").grid(row = 6, column = 1, pady = 1)
        tk.Label(parent, text="Exit key:").grid(row = 7, column = 1, pady = 1)

        # entries for custom toggle keys
        for i in range(len(self.default_keys)):
            entry = tk.Entry(parent, width=6)
            entry.grid(row = i+2, column = 2, pady = 1)
            entry.bind("<KeyPress>", self.onKeyPress)
            entry.insert(0, self.default_keys[i])

        tk.Label(parent).grid(row = 9, column = 0)
        # start the program button
        self.start_button = tk.Button(parent, text="Start", width=7, command=self.startClicker)
        self.start_button.grid(row = 10, column = 4)

    def onKeyPress(self, event):
        def clear():
            event.widget.delete(0,"end")
            event.widget.insert(0,event.keysym)
        self.p.after(1, clear)
        entry = str(event.widget).split("entry")[1]

        # surround if statements is fine but wtf is the if elif spam in between
        if event.keysym in string.ascii_letters + string.digits:
            if entry == "": self.pos_key = KeyCode(char=event.keysym)
            elif entry == "2": self.clear_key = KeyCode(char=event.keysym)
            elif entry == "3": self.start_key = KeyCode(char=event.keysym)
            elif entry == "4": self.stop_key = KeyCode(char=event.keysym)
            elif entry == "5": self.mode_key = KeyCode(char=event.keysym)
            elif entry == "6": self.exit_key = KeyCode(char=event.keysym)
        else:
            for i in Key:
                if event.keysym.upper() == str(i).split(".")[1].upper():
                    if entry == "": self.pos_key = i
                    elif entry == "2": self.clear_key = i
                    elif entry == "3": self.start_key = i
                    elif entry == "4": self.stop_key = i
                    elif entry == "5": self.mode_key = i
                    elif entry == "6": self.exit_key = i

    # start
    def startClicker(self):
        self.p.focus()
        self.started = True
        self.start_button.config(text="Running")

    # click loop for at current mouse pos
    def click_loop(self):
        if self.started:
            if self.running:
                mouse.press(self.button)
                mouse.release(self.button)
                self.p.after(self.delay, self.click_loop)

    # mode switch
    def mode_switch(self):
        self.mode = not self.mode
        
# THE POINTER
class Point(tk.Frame):
    coords = []
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
        self.coords.append(pos)
        circle = tk.Label(self.p, text="⭕", bg="#012345", fg="red", font=("Arial", 15), bd=0)
        #n = tk.Label(self.p, text=len(self.coords), bg="#012345", fg="red", font=("Arial", 15), bd=0)
        n = tk.Label(self.p, text=str(len(self.coords))+str(pos), bg="#012345", fg="red", font=("Arial", 15), bd=0)
        w, h = circle.winfo_reqwidth(), circle.winfo_reqheight()
        n.place(x=pos[0], y=pos[1]-35)
        circle.place(x=pos[0]-w//2, y=pos[1]-h//2)

    def coords_loop(self):
        def click(pos):
            mouse.position = pos
            mouse.press(app.button)
            mouse.release(app.button)
            
        if app.started:
            if app.running:
                for i in self.coords:
                    self.p.after(100, click(i))
                self.p.after(1, self.coords_loop)



# DETECTION
# detects key presses and if they match any toggle keys
def on_press(key):
    if app.started:
        if key == app.start_key and not app.running:
            print("STARTED")
            app.running = True

            if app.mode:
                print("MODE: autoclicker")
                app.click_loop()
            else:
                print("MODE: coord loop")
                point.coords_loop()

        elif key == app.stop_key and app.running:
            print("STOPPED: stop key press")
            app.running = False

        elif key == app.pos_key:
            point.create(mouse.position)

        elif key == app.clear_key:
            for widget in sub.winfo_children():
                widget.destroy()
            point.coords = []

        elif key == app.mode_key:
            app.mode_switch()
            if app.mode:
                print("MODE SWITCH: autoclicker")
            else:
                print("MODE SWITCH: coord loop")

        elif key == app.exit_key:
            print("EXIT")
            main.destroy()
            keyboard_listener.stop()

# detects mouse movement and if it is not in the saved coords then stop the program
def on_move(x,y):
    if app.started:
        if app.running:
            if app.mode == False:
                if mouse.position not in point.coords:
                    print("STOPPED: mouse movement")
                    app.running = False
                    

# START
if __name__ == "__main__":
    # mouse control
    mouse = Controller()
    # setup the listener
    keyboard_listener = KBListener(on_press=on_press)
    mouse_listener = MListener(on_move=on_move)
    keyboard_listener.start()
    mouse_listener.start()

    # window set up
    main = tk.Tk()
    sub = tk.Toplevel()

    app = App(main)
    point = Point(sub)

    # mainloop
    tk.mainloop()
    






