# hari_ke_21.py
angka = [1, 2, 3, 4, 5, 6, 7, 8]
genap = list(filter(lambda x: x % 2 == 0, angka))
kuadrat = list(map(lambda x: x**2, angka))

print("Genap:", genap)
print("Kuadrat:", kuadrat)
