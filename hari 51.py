# hari_ke_51.py
import tkinter as tk

def hitung():
    try:
        hasil = eval(entry.get())
        label_hasil.config(text="Hasil: " + str(hasil))
    except:
        label_hasil.config(text="Error")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Hitung", command=hitung)
btn.pack()

label_hasil = tk.Label(root, text="Hasil:")
label_hasil.pack()

root.mainloop()
