# hari_ke_83.py
n = int(input("Berapa banyak bilangan Fibonacci? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
