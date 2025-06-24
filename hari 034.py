# hari_ke_34.py
import time

def generator():
    for i in range(1000000):
        yield i

def list_biasa():
    return [i for i in range(1000000)]

start = time.time()
g = generator()
for _ in g:
    pass
print("Generator:", time.time() - start)

start = time.time()
l = list_biasa()
for _ in l:
    pass
print("List:", time.time() - start)
