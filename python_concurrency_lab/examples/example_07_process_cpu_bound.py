import multiprocessing
import time

def ciezka_praca():
    suma = 0
    for i in range(20_000_000):
        suma += i * i
    return suma


if __name__ == "__main__":
    # 1️⃣ Sekwencyjnie
    start = time.time()
    ciezka_praca()
    ciezka_praca()
    print(f"Sekwencyjnie: {time.time() - start:.2f} s")

    # 2️⃣ Równolegle (2 procesy)
    start = time.time()

    p1 = multiprocessing.Process(target=ciezka_praca)
    p2 = multiprocessing.Process(target=ciezka_praca)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Procesy: {time.time() - start:.2f} s")
