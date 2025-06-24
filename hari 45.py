# hari_ke_45.py
import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.start_time = None
        self.label = tk.Label(root, text="0.00", font=("Arial", 30))
        self.label.pack()
        self.btn = tk.Button(root, text="Start", command=self.toggle)
        self.btn.pack()
        self.running = False
        self.update()

    def toggle(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
        else:
            self.running = False

    def update(self):
        if self.running:
            elapsed = time.time() - self.start_time
            self.label.config(text=f"{elapsed:.2f}")
        root.after(100, self.update)

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
