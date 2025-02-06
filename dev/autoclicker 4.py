import time, threading
import tkinter as tk

from pynput.mouse import Listener, Button, Controller
MListener = Listener
from pynput.keyboard import Listener, KeyCode, Key
KBListener = Listener
 
 
delay = 0.1
button = Button.left
start_stop_key = Key.f11
exit_key = Key.f12


def hi():
    print("hi")

    
root = tk.Tk()
root.title("EasyClicker")
root.geometry("300x320+0+0")
root.resizable(False,False)
tk.Label(root, text="Title", font=("Moderne Sans","15")).pack()
tk.Button(root, text="test button", command=hi).pack()
        
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True
        self.mode = True
 
    def start_clicking(self):
        self.running = True
 
    def stop_clicking(self):
        self.running = False

    # True being an autoclicker at mouse pos
    # False being multiple coords to click at on loop
    def change_mode(self):
        self.mode = not self.mode
 
    def exit(self):
        self.stop_clicking()
        self.program_run = False
 
    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# START
mouse = Controller()
clicker = ClickMouse(delay, button)
clicker.start()


# DETECTION
# detecting toggle key press
def on_press(key):
    if key == start_stop_key:
        if clicker.running:
            print("stopped on stop key")
            clicker.stop_clicking()
        else:
            print("started")
            clicker.start_clicking()
    elif key == exit_key:
        print("exited on exit key")
        clicker.exit()
        mouse_listener.stop()
        keyboard_listener.stop()
        root.destroy()
        
# detect mouse movement
def on_move(x,y):
    if clicker.running:
        print("stopped on mouse movement")
        clicker.stop_clicking()

        

# Setup the listener threads
keyboard_listener = KBListener(on_press=on_press)
mouse_listener = MListener(on_move=on_move)


# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
#keyboard_listener.join()
#mouse_listener.join()



    
