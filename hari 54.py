# hari_ke_54.py
import random

angka_rahasia = random.randint(1, 10)
tebakan = int(input("Tebak angka antara 1-10: "))

if tebakan == angka_rahasia:
    print("Benar!")
else:
    print("Salah, angka itu adalah:", angka_rahasia)
