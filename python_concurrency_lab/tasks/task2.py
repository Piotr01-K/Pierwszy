import threading
import time


def worker(thread_number):
    """
    Funkcja wykonywana przez każdy wątek.
    """
    print(f"Jestem wątkiem numer {thread_number}")
    time.sleep(1)


threads = []

# Tworzymy i uruchamiamy 5 wątków
for i in range(1, 6):
    thread = threading.Thread(
        target=worker,
        args=(i,)
    )
    threads.append(thread)
    thread.start()

print("Główny program czeka na zakończenie wszystkich wątków...")

# Czekamy na zakończenie wszystkich wątków
for thread in threads:
    thread.join()

print("Wszystkie wątki zakończyły pracę.")
