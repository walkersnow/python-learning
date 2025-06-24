# hari_ke_73.py
kalimat = input("Masukkan kalimat: ")
kata = kalimat.lower().split()
frekuensi = {}

for k in kata:
    frekuensi[k] = frekuensi.get(k, 0) + 1

print(frekuensi)
