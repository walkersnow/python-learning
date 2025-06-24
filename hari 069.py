# hari_ke_69.py
import random
import string

panjang = 8
karakter = string.ascii_letters + string.digits
password = "".join(random.choices(karakter, k=panjang))
print("Password:", password)
