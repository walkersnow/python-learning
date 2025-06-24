# hari_ke_61.py
import random

opsi = ["gunting", "batu", "kertas"]
komputer = random.choice(opsi)
user = input("Pilih (gunting/batu/kertas): ")

if user == komputer:
    print("Seri!")
elif (user == "gunting" and komputer == "kertas") or \
     (user == "batu" and komputer == "gunting") or \
     (user == "kertas" and komputer == "batu"):
    print("Kamu menang!")
else:
    print("Kamu kalah!")
