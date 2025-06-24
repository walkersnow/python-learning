# hari_ke_53.py
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

bmi = berat / (tinggi ** 2)

print(f"BMI Anda: {round(bmi, 2)}")
if bmi < 18.5:
    print("Kurus")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Gemuk")
