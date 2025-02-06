import tkinter as tk

from pynput.mouse import Listener, Button, Controller
MListener = Listener
from pynput.keyboard import Listener, KeyCode, Key
KBListener = Listener

# MAIN BUILD
class App:
    # default values
    running = False
    delay = 10
    button = Button.left
    getpos_key = Key.f9
    start_key = Key.f10
    stop_key = Key.f11
    exit_key = Key.f12
    def __init__(self, root):
        self.master = root

        # standard tkinter set up
        root.title("EasyClicker")
        root.geometry("300x320+0+0")
        root.resizable(False,False)

        # the tkinter menu
        tk.Label(root, text="Title", font=("Moderne Sans","15")).pack()
        tk.Label(root, text="press F9 to get mouse pos").pack()
        tk.Label(root, text="press F10 to start").pack()
        tk.Label(root, text="press F11 to stop").pack()
        tk.Label(root, text="press F12 to end").pack()

        _entry = tk.Entry(root)

        tk.Button(root, text="test", command=self.test).pack()


        # mouse control and listening set up
        self.mouse = Controller()
        # setup the listener threads
        keyboard_listener = KBListener(on_press=self.on_press)
        mouse_listener = MListener(on_move=self.on_move)
        keyboard_listener.start()
        mouse_listener.start()

    def test(self):
        t = str(self.start_key).split(".")[1]
        print(t)

    # detects key presses
    def on_press(self, key):
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
        if self.running: # change to check for mode
            print("stopped on mouse movement")
            self.running = False

    # click loop
    def click_loop(self):
        if self.running:
            self.mouse.press(self.button)
            self.mouse.release(self.button)
            self.master.after(self.delay, self.click_loop)
        
"""
    def change_mode(self):
        self.mode = not self.mode"""
 

# START
if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()







    
