# hari_ke_50.py
tugas = []

while True:
    print("\n1. Tambah Tugas\n2. Lihat\n3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        tugas.append(input("Masukkan tugas: "))
    elif pilih == "2":
        for i, t in enumerate(tugas, 1):
            print(f"{i}. {t}")
    elif pilih == "3":
        break
    else:
        print("Pilihan salah.")
