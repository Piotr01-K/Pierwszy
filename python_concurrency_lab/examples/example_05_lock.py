import threading

licznik = 0
lock = threading.Lock()

def bezpieczna_inkrementacja():
    global licznik
    for _ in range(100_000):
        with lock:
            licznik += 1

watki = []

for _ in range(10):
    thread = threading.Thread(target=bezpieczna_inkrementacja)
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

print(f"Ostateczna wartość licznika: {licznik}")
