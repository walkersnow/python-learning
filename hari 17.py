# hari_ke_17.py
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Tidak bisa dibagi nol.")
except ValueError:
    print("Input bukan angka.")
