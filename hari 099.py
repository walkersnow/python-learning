# hari_ke_99.py
keys = input("Masukkan kunci (pisahkan koma): ").split(",")
values = input("Masukkan nilai (pisahkan koma): ").split(",")

hasil = dict(zip(keys, values))
print("Dictionary:", hasil)
