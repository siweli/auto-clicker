import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
import ctypes
# screensize so it can be centered on any screen size
user32 = ctypes.windll.user32
screenx, screeny = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
x,y = screenx//2, screeny//2

#update to pyautogui method


# MAIN PROGRAM
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # standard stuff
        self.title("Custom Crosshair Menu")
        self.geometry("300x320+0+0")
        self.resizable(False,False)
        Label(self, text="Choose your settings", font=("Moderne Sans","15")).pack()
        
        # default settings
        self.colour = "#00ff00"
        self.size = 15
        #self.crosshair = Crosshair(self.colour, self.size)

        # change settings
        Button(self, text="Change colour", command=self.change_colour).pack()
        scale = Scale(
                                self, from_=5, to=90, orient=HORIZONTAL, activebackground="#FFFFFF",
                                command=self.change_size, sliderlength=15, length=175, cursor="arrow")
        scale.pack()
        scale.set(self.size)
               
        # preview the crosshair
        preview_frame = Frame(self, height=175,width=175, bg="#777")
        preview_frame.pack()
        preview_frame.pack_propagate(False)

        # to center the preview crosshair
        for i in ["left","right","top","bottom"]: Label(preview_frame, bg="#777").pack(side=i, fill=BOTH,expand=True)

        # the crosshair preview
        self.preview = Label(preview_frame, text="⭕", font=("Moderne Sans",self.size), fg=self.colour, bg="#777")
        self.preview.pack()

        # apply the changes
        apply_button = Button(self, text="Apply", command=lambda: self.update(self.colour, self.size))
        apply_button.pack()

        # hide or show the crosshair
        self.state_button = Button(self, text="Hide", command=self.change_state)
        self.state_button.pack()

    def change_size(self, amount):
        self.size = amount
        self.preview.config(font=("Moderne Sans",amount))

    def change_colour(self):
        colour = askcolor(title="Colour Chooser")
        self.colour = colour[1]
        self.preview.config(fg=colour[1])
    
    # update/create the crosshair
    def update(self, colour, size):
        try:
            self.crosshair.destroy() # destroys old crosshair
        except AttributeError:
            pass
        self.crosshair = Crosshair(colour, size)
        self.crosshair.mainloop()

    def change_state(self):
        if self.crosshair.state: self.state_button.config(text="Show")
        else: self.state_button.config(text="Hide")
        self.crosshair.change_state()

# THE CROSSHAIR
class Crosshair(tk.Tk):
    def __init__(self, colour, size):
        super().__init__()

        self.state = True

        # change chroma to black (will leave a black outline due to python being bad)
        # will also change to different black if colour happens to be the same as default chroma
        chroma = "#010101"
        if colour == chroma: chroma = "#112"

        # the crosshair
        # https://jrgraphix.net/r/Unicode/0020-007F
        # ⚞⚟
        # ⭕ ⚬
        # ♢ ☐ ⌷ ⍞
        # ⛭ ☼
        # ⛬ ⛚
        # ⛶
        # ♡
        # ☝ # if this one then y needs to go down an amount

        # ☩
        # ⚋ # try find this but rotated
        # ╳ ┽┽╁╂╃╄╅╋
        
        self.cross = Label(self, text="⭕", font=("Moderne Sans",size), fg=colour)#, bg=chroma)
        self.cross.pack()
        w, h = self.cross.winfo_reqwidth(), self.cross.winfo_reqheight()

        # makes the crosshair appear in center and transparent
        self.overrideredirect(True)
        self.geometry(f"+{x-w//2}+{y-h//2}")
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", chroma)

        # make event handler to toggle on keypress like left click or smth (default insert)

    def change_state(self):
        if self.state: self.cross.config(text="")
        else: self.cross.config(text="⭕")
        self.state = not self.state

# START
if __name__ == "__main__":
    app = App()
    app.mainloop()
