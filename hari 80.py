# hari_ke_80.py
import random

kata_list = ["python", "program", "belajar", "kuat", "logika"]
kata = random.choice(kata_list)
tebakan = input("Tebak kata (hint: bahasa pemrograman): ")

if tebakan == kata:
    print("Benar!")
else:
    print("Salah! Jawabannya:", kata)
