# hari_ke_44.py
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b if b != 0 else "Error"

print("1.Tambah 2.Kurang 3.Kali 4.Bagi")
pilih = input("Pilih operasi (1-4): ")
a = int(input("Angka 1: "))
b = int(input("Angka 2: "))

ops = {"1": tambah, "2": kurang, "3": kali, "4": bagi}
hasil = ops[pilih](a, b)
print("Hasil:", hasil)
