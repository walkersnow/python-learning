# hari_ke_91.py
import time

input("Tekan Enter untuk mulai...")
start = time.time()
input("Tekan Enter untuk berhenti...")
end = time.time()

elapsed = end - start
print(f"Waktu berlalu: {round(elapsed, 2)} detik")
