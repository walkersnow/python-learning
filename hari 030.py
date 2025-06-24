# hari_ke_30.py
class Persegi:
    def __init__(self, sisi):
        self._sisi = sisi

    @property
    def luas(self):
        return self._sisi ** 2

    @luas.setter
    def luas(self, nilai):
        self._sisi = nilai ** 0.5

p = Persegi(4)
print("Luas:", p.luas)
p.luas = 100
print("Sisi baru:", p._sisi)
