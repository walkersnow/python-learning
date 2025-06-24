# hari_ke_94.py
import re

nomor = input("Masukkan nomor HP (Indonesia): ")
if re.fullmatch(r"08\d{8,11}", nomor):
    print("Nomor valid")
else:
    print("Nomor tidak valid")
