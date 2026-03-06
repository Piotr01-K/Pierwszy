import multiprocessing
import random
import math


def czy_pierwsza(n):
    """Sprawdza, czy liczba jest pierwsza"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    # Lista 100 losowych liczb
    liczby = [random.randint(1, 1000) for _ in range(100)]

    # Tworzymy pulę procesów
    with multiprocessing.Pool() as pool:
        wyniki = pool.map(czy_pierwsza, liczby)

    # Liczymy True
    ile_pierwszych = sum(wyniki)

    print(f"Znaleziono {ile_pierwszych} liczb pierwszych.")
