# hari_ke_24.py
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(5))
