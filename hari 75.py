# hari_ke_75.py
kontak = {}

while True:
    print("\n1. Tambah\n2. Cari\n3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama: ")
        no = input("Nomor: ")
        kontak[nama] = no
    elif pilih == "2":
        cari = input("Nama yang dicari: ")
        print("Nomor:", kontak.get(cari, "Tidak ditemukan"))
    elif pilih == "3":
        break
