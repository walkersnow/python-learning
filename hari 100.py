# hari_ke_100_quiz_game.py
import random

soal = [
    {
        "pertanyaan": "Apa output dari 2 ** 3?",
        "pilihan": ["5", "6", "8", "9"],
        "jawaban": "8"
    },
    {
        "pertanyaan": "Fungsi untuk input di Python?",
        "pilihan": ["get()", "input()", "scan()", "read()"],
        "jawaban": "input()"
    },
    {
        "pertanyaan": "Tipe data untuk nilai True/False?",
        "pilihan": ["str", "int", "bool", "float"],
        "jawaban": "bool"
    }
]

random.shuffle(soal)
skor = 0

for s in soal:
    print("\n❓", s["pertanyaan"])
    for i, opsi in enumerate(s["pilihan"]):
        print(f"{i+1}. {opsi}")
    jawab = input("Jawaban (1/2/3/4): ")
    if s["pilihan"][int(jawab)-1] == s["jawaban"]:
        print("✅ Benar!")
        skor += 1
    else:
        print(f"❌ Salah! Jawaban: {s['jawaban']}")

print(f"\nSkor akhir: {skor}/{len(soal)}")
