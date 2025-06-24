# hari_ke_95.py
import random

opsi = ['batu', 'gunting', 'kertas']
komputer = random.choice(opsi)
player = input("Pilih (batu/gunting/kertas): ").lower()

if player == komputer:
    hasil = "Seri"
elif (player == 'batu' and komputer == 'gunting') or \
     (player == 'gunting' and komputer == 'kertas') or \
     (player == 'kertas' and komputer == 'batu'):
    hasil = "Menang!"
else:
    hasil = "Kalah!"

print(f"Kamu: {player}, Komputer: {komputer} -> {hasil}")
