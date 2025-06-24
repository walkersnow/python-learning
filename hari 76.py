# hari_ke_76.py
from datetime import datetime

tanggal_input = input("Masukkan tanggal (DD-MM-YYYY): ")
tanggal_obj = datetime.strptime(tanggal_input, "%d-%m-%Y")
print("Format baru:", tanggal_obj.strftime("%Y/%m/%d"))
