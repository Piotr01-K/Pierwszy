import threading
import time

def ciezka_praca():
    suma = 0
    for i in range(20_000_000):
        suma += i * i
    return suma


# 1️⃣ Wersja sekwencyjna
start = time.time()
ciezka_praca()
ciezka_praca()
print(f"Sekwencyjnie: {time.time() - start:.2f} s")


# 2️⃣ Wersja wielowątkowa
start = time.time()

t1 = threading.Thread(target=ciezka_praca)
t2 = threading.Thread(target=ciezka_praca)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Wątki: {time.time() - start:.2f} s")
