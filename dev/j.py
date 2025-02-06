import tkinter as tk

def onKeyPress(event):
    text.insert('end', f'You pressed {event.keysym}\n')



root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
#for i in range(1,13):
#   root.bind(f'<KeyPress-F{i}>', onFKeyPress)
root.bind('<KeyPress>', onKeyPress)
root.mainloop()


