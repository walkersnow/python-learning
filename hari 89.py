# hari_ke_89.py
teks = input("Masukkan kalimat: ").lower()
vokal = "aiueo"
jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)
jumlah_konsonan = sum(1 for huruf in teks if huruf.isalpha() and huruf not in vokal)
print("Vokal:", jumlah_vokal, "| Konsonan:", jumlah_konsonan)
