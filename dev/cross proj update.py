import tkinter as tk
from win32gui import SetWindowLong, GetWindowLong, SetLayeredWindowAttributes
from win32con import WS_EX_LAYERED, WS_EX_TRANSPARENT, GWL_EXSTYLE

def set_clickthrough(hwnd):
    try:
        styles = GetWindowLong(hwnd, GWL_EXSTYLE)
        styles = WS_EX_LAYERED | WS_EX_TRANSPARENT
        SetWindowLong(hwnd, GWL_EXSTYLE, styles)
        SetLayeredWindowAttributes(hwnd, 0, 255, 0x00000001)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('1920x1080')
    root.overrideredirect(True)
    root.config(bg='#000000')
    root.attributes("-alpha", 1)
    root.wm_attributes("-topmost", 1)
    root.attributes('-transparentcolor', '#000000', '-topmost', 1)
    root.resizable(False, False)
    set_clickthrough(root.winfo_id())

    label = tk.Label(root, text="+", bg="black", fg="red", font=("Arial", 10), bd=0)
    label.place(x=1920 / 2, y=1080 / 2)

    root.mainloop()

