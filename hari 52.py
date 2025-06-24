# hari_ke_52.py
import time

start = input("Tekan Enter untuk mulai stopwatch...")
mulai = time.time()
input("Tekan Enter untuk stop...")
selesai = time.time()
print(f"Total waktu: {round(selesai - mulai, 2)} detik")
