# hari_ke_33.py
def dekorator(func):
    def bungkus():
        print("Sebelum fungsi dipanggil")
        func()
        print("Setelah fungsi dipanggil")
    return bungkus

@dekorator
def sapa():
    print("Halo, dunia!")

sapa()
