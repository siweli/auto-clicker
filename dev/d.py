import tkinter as tk
from pynput.mouse import Controller
from pynput.keyboard import Listener, Key
KBListener = Listener

# MAIN PROGRAM
class App(tk.Frame):
    go_key = Key.f10
    exit_key = Key.f12
    def __init__(self, parent):
        super().__init__(parent)

        # standard menu setup
        parent.title("Menu")
        parent.geometry("300x320+0+0")
        parent.resizable(False,False)
        parent.wm_attributes("-topmost", True)
        
        # setting the menu content
        tk.Label(parent, text="title", font=("Moderne Sans","15")).pack()
        tk.Label(parent, text="pretend there are options here").pack()
        tk.Label(parent, text="press F10 to go").pack()

        

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
        label = tk.Label(self.p, text="⭕", bg="#012345", fg="red", font=("Arial", 15), bd=0)
        w, h = label.winfo_reqwidth(), label.winfo_reqheight()
        label.place(x=pos[0]-w//2, y=pos[1]-h//2)



# DETECTION
# detects key presses
def on_press(key):
    if key == Key.f10:
        point.create(mouse.position)
        
    elif key == App.exit_key:
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
    






