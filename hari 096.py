# hari_ke_96.py
akun = {"admin": "1234", "user": "abcd"}

username = input("Username: ")
password = input("Password: ")

if akun.get(username) == password:
    print("Login berhasil!")
else:
    print("Username/password salah!")
