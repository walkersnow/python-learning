# hari_ke_93.py
teks = input("Masukkan kalimat: ")
kata = teks.split()
jumlah_kata = len(kata)
jumlah_karakter = len(teks.replace(" ", ""))
print(f"Kata: {jumlah_kata}, Karakter (tanpa spasi): {jumlah_karakter}")
