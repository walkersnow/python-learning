# hari_ke_32.py
def hitung():
    for i in range(5):
        yield i * 2

for angka in hitung():
    print(angka)
