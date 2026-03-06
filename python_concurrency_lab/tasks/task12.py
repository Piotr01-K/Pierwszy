# Zadanie 12 – GIL w praktyce (CPU-bound)
# Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in
# range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie
# zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec
# zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i
# wyjaśnij wyniki w komentarzu w kodzie.

import threading
import multiprocessing
import time


def ciezkie_obliczenia():
    return sum(i * i for i in range(20_000_000))


def mierz_czas(opis, funkcja):
    start = time.time()
    funkcja()
    end = time.time()
    print(f"{opis}: {end - start:.2f} s")


if __name__ == "__main__":

    # ekwencyjnie
    print("\n--- Sekwencyjnie ---")
    mierz_czas("Pierwsze wywołanie", ciezkie_obliczenia)
    mierz_czas("Drugie wywołanie", ciezkie_obliczenia)

    # Wątki
    print("\n--- Wątki ---")
    start = time.time()

    t1 = threading.Thread(target=ciezkie_obliczenia)
    t2 = threading.Thread(target=ciezkie_obliczenia)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Wątki razem: {time.time() - start:.2f} s")

    # Procesy
    print("\n--- Procesy ---")
    start = time.time()

    p1 = multiprocessing.Process(target=ciezkie_obliczenia)
    p2 = multiprocessing.Process(target=ciezkie_obliczenia)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Procesy razem: {time.time() - start:.2f} s")

    """
    WNIOSKI:
    - Wątki NIE przyspieszają obliczeń CPU-bound z powodu GIL
    - Dwa wątki wykonują się praktycznie tak samo wolno jak sekwencyjnie
    - Procesy omijają GIL, więc działają szybciej na wielu rdzeniach
    """
