# hari_ke_60.py
detik = int(input("Masukkan total detik: "))
jam = detik // 3600
menit = (detik % 3600) // 60
sisa = detik % 60
print(f"{jam} jam, {menit} menit, {sisa} detik")
