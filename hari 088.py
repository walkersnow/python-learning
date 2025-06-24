# hari_ke_88.py
n = int(input("Masukkan angka: "))
if (n & (n - 1)) == 0 and n != 0:
    print("Pangkat dua")
else:
    print("Bukan pangkat dua")
