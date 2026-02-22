import threading

licznik = 0

def inkrementuj():
    global licznik
    for _ in range(100_000):
        licznik += 1

watki = []

for _ in range(10):
    thread = threading.Thread(target=inkrementuj)
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

print(f"Ostateczna wartość licznika: {licznik}")
