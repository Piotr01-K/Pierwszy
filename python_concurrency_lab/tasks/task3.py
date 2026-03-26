import threading
import time


def pobierz_dane(id_danych):
    """
    Symuluje pobieranie danych.
    """
    print(f"Pobieram dane o id: {id_danych}")
    time.sleep(2)
    print(f"Zakończono pobieranie danych o id: {id_danych}")


# =========================
# WERSJA 1: SEKWENCYJNA
# =========================

print("\n--- Wersja sekwencyjna ---")

start_time = time.time()

for i in range(1, 4):
    pobierz_dane(i)

end_time = time.time()

czas_sekwencyjny = end_time - start_time
print(f"Czas sekwencyjny: {czas_sekwencyjny:.2f} sekund")


# =========================
# WERSJA 2: WĄTKI
# =========================

print("\n--- Wersja wielowątkowa ---")

threads = []
start_time = time.time()

for i in range(1, 4):
    thread = threading.Thread(
        target=pobierz_dane,
        args=(i,)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

czas_watki = end_time - start_time
print(f"Czas z wątkami: {czas_watki:.2f} sekund")
