# hari_ke_62.py
harga = float(input("Masukkan harga: "))
diskon = float(input("Masukkan diskon (%): "))
total = harga - (harga * (diskon / 100))
print("Total bayar:", total)
