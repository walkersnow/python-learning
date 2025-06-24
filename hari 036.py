# hari_ke_36.py
import re

kalimat = "Nomor HP: 0812-3456-7890 atau 0857-8888-7777"
hasil = re.findall(r'08\d{2}-\d{4}-\d{4}', kalimat)
print("Nomor ditemukan:", hasil)
