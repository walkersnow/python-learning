# hari_ke_28.py
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print(f"Halo, saya {self.nama}, umur saya {self.umur} tahun.")

mhs1 = Mahasiswa("Ical", 21)
mhs1.sapa()
