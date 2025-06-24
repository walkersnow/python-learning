# hari_ke_74.py
penghasilan = float(input("Masukkan penghasilan: "))
pajak = 0.1 if penghasilan > 5000000 else 0.05
print("Pajak:", penghasilan * pajak)
