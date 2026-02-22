import multiprocessing
import math


def oblicz_silnie():
    """Funkcja uruchamiana w osobnym procesie"""
    wynik = math.factorial(10)
    print(f"Silnia 10 wynosi: {wynik}")


if __name__ == "__main__":
    # Tworzymy proces
    proces = multiprocessing.Process(target=oblicz_silnie)

    # Uruchamiamy proces
    proces.start()

    # Czekamy aż proces się zakończy
    proces.join()

    print("Proces zakończył działanie.")
