# hari_ke_85.py
import re

email = input("Masukkan email: ")
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Email valid")
else:
    print("Email tidak valid")
