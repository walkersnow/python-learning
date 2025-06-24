# hari_ke_70.py
data = []

while True:
    print("\n1. Tambah\n2. Lihat\n3. Hapus\n4. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        item = input("Masukkan item: ")
        data.append(item)
    elif pilih == "2":
        for i, item in enumerate(data):
            print(f"{i+1}. {item}")
    elif pilih == "3":
        hapus = int(input("Nomor yang dihapus: ")) - 1
        if 0 <= hapus < len(data):
            data.pop(hapus)
    elif pilih == "4":
        break
