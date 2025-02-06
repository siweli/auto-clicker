import tkinter as tk


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.count = 0
        self.button = tk.Button(self, text="Click me!", command=self.click)
        self.label = tk.Label(self, text="", width=20)

        self.label.pack(side="top", fill="both", expand=True)
        self.button.pack(side="bottom", padx=4, pady=4)

        self.refresh_clicks()

    def click(self):
        self.count += 1
        self.refresh_clicks()

    def refresh_clicks(self):
        self.label.configure(text=f"Clicks: {self.count}")

apps = []
n = 2
for i in range(n):
    window = tk.Tk() if i == 0 else tk.Toplevel()

    app = App(window)
    app.pack(fill="both", expand=True)
    apps.append(app)

tk.mainloop()
