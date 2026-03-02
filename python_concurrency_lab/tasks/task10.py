import threading
import os

# Globalny licznik
total_count = 0
lock = threading.Lock()


def policz_slowo_w_pliku(nazwa_pliku, slowo):
    global total_count

    with open(nazwa_pliku, "r", encoding="utf-8") as f:
        tresc = f.read()
        liczba = tresc.count(slowo)

    # Bezpieczna aktualizacja licznika
    with lock:
        total_count += liczba

    print(f"{nazwa_pliku}: {liczba}")


if __name__ == "__main__":
    slowo = input("Podaj słowo do wyszukania: ")

    watki = []

    for plik in os.listdir("."):
        if plik.endswith(".txt"):
            watek = threading.Thread(
                target=policz_slowo_w_pliku,
                args=(plik, slowo)
            )
            watki.append(watek)
            watek.start()

    for watek in watki:
        watek.join()

    print(f"\nŁączna liczba wystąpień słowa '{slowo}': {total_count}")
