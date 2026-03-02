import threading
import queue
import time
import random


def producent(q, start_time):
    """Wątek producenta – dodaje dane do kolejki"""
    while time.time() - start_time < 10:
        liczba = random.randint(1, 100)
        q.put(liczba)
        print(f"Producent dodał: {liczba}")
        time.sleep(1)


def konsument(q, start_time):
    """Wątek konsumenta – pobiera dane z kolejki"""
    while time.time() - start_time < 10:
        try:
            element = q.get(timeout=2)
            print(f"Konsument pobrał: {element}")
        except queue.Empty:
            print("Kolejka pusta")
        time.sleep(1.5)


if __name__ == "__main__":
    q = queue.Queue()
    start_time = time.time()

    watek_producenta = threading.Thread(target=producent, args=(q, start_time))
    watek_konsumenta = threading.Thread(target=konsument, args=(q, start_time))

    watek_producenta.start()
    watek_konsumenta.start()

    watek_producenta.join()
    watek_konsumenta.join()

    print("Program producent–konsument zakończony.")
