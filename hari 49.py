# hari_ke_49.py
mahasiswa = [
    {"nama": "Ibnu", "nilai": 99},
    {"nama": "Dika", "nilai": 100},
    {"nama": "Ical", "nilai": 95},
]

mahasiswa.sort(key=lambda x: x["nilai"], reverse=True)
print(mahasiswa)
