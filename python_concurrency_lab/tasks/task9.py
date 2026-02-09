# Zadanie 9 – Sumowanie z wątkami i blokadą
# Napisz program, który sumuje liczby w dużej liście (np. 10 milionów elementów). Podziel
# listę na 4 części i każdą część zsumuj w osobnym wątku. Wyniki częściowe dodawaj do
# globalnej zmiennej suma_calkowita, zabezpieczając dostęp do niej za pomocą
# threading.Lock.

import threading

# Globalna suma
suma_calkowita = 0

# Blokada
lock = threading.Lock()


def sumuj_fragment(dane):
    """Sumuje fragment listy i dodaje do sumy globalnej (bezpiecznie)"""
    global suma_calkowita

    suma_czesciowa = sum(dane)

    # Sekcja krytyczna
    with lock:
        suma_calkowita += suma_czesciowa


if __name__ == "__main__":
    # Tworzymy dużą listę liczb
    dane = list(range(10_000_000))

    # Dzielimy na 4 części
    rozmiar = len(dane) // 4
    fragmenty = [
        dane[0:rozmiar],
        dane[rozmiar:2 * rozmiar],
        dane[2 * rozmiar:3 * rozmiar],
        dane[3 * rozmiar:]
    ]

    watki = []

    # Tworzymy i uruchamiamy wątki
    for fragment in fragmenty:
        watek = threading.Thread(target=sumuj_fragment, args=(fragment,))
        watki.append(watek)
        watek.start()

    # Czekamy na zakończenie wszystkich wątków
    for watek in watki:
        watek.join()

    print(f"Suma całkowita: {suma_calkowita}")
