# hari_ke_92.py
daftar = input("Masukkan daftar angka (pisahkan dengan koma): ").split(",")
duplikat = [x for x in set(daftar) if daftar.count(x) > 1]
print("Duplikat:", duplikat)
