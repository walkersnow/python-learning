# hari_ke_97.py
def enkripsi(teks, geser):
    hasil = ""
    for huruf in teks:
        if huruf.isalpha():
            ascii_offset = 65 if huruf.isupper() else 97
            hasil += chr((ord(huruf) - ascii_offset + geser) % 26 + ascii_offset)
        else:
            hasil += huruf
    return hasil

pesan = input("Masukkan pesan: ")
kunci = int(input("Geser berapa huruf? "))
print("Hasil enkripsi:", enkripsi(pesan, kunci))
