# hari_ke_35.py
import re

teks = "Email saya adalah contoh@gmail.com dan juga contoh2@yahoo.com"
hasil = re.findall(r'\S+@\S+', teks)
print("Email ditemukan:", hasil)
