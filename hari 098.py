# hari_ke_98.py
waktu_24 = input("Masukkan waktu (HH:MM): ")
jam, menit = map(int, waktu_24.split(":"))

periode = "AM" if jam < 12 else "PM"
jam_12 = jam % 12 or 12

print(f"{jam_12:02}:{menit:02} {periode}")
