# hari_ke_81.py
from datetime import datetime

tahun_lahir = int(input("Masukkan tahun lahir: "))
tahun_sekarang = datetime.now().year
umur = tahun_sekarang - tahun_lahir
print("Umur kamu:", umur)
