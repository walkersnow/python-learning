# hari_ke_31.py
class Siswa:
    jumlah = 0

    def __init__(self, nama):
        self.nama = nama
        Siswa.jumlah += 1

    @classmethod
    def total_siswa(cls):
        print("Total siswa:", cls.jumlah)

    @staticmethod
    def info():
        print("Ini adalah class untuk data siswa.")

s1 = Siswa("Ical")
s2 = Siswa("Adit")
Siswa.total_siswa()
Siswa.info()
