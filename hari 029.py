# hari_ke_29.py
class Orang:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        print(f"Halo, saya {self.nama}")

class Mahasiswa(Orang):
    def belajar(self):
        print(f"{self.nama} sedang belajar.")

mhs = Mahasiswa("Rani")
mhs.sapa()
mhs.belajar()
