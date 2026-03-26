import multiprocessing


def potega(liczba, pot):
    """Funkcja uruchamiana w osobnym procesie"""
    wynik = liczba ** pot
    print(f"{liczba} do potęgi {pot} = {wynik}")


if __name__ == "__main__":
    # Tworzymy proces z argumentami
    proces = multiprocessing.Process(
        target=potega,
        args=(5, 3)
    )

    # Uruchamiamy proces
    proces.start()

    # Czekamy na zakończenie procesu
    proces.join()

    print("Proces z argumentami zakończył działanie.")
