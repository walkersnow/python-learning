# hari_ke_67.py
while True:
    print("\n1. Tambah\n2. Kurang\n3. Keluar")
    pilih = input("Pilih: ")
    if pilih == "3":
        break
    a = int(input("Angka 1: "))
    b = int(input("Angka 2: "))
    if pilih == "1":
        print("Hasil:", a + b)
    elif pilih == "2":
        print("Hasil:", a - b)
