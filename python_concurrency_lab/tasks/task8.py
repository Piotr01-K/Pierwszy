import multiprocessing


def wyslij_imie(kolejka, imie):
    """Proces potomny: wysyła dane do procesu głównego"""
    kolejka.put(imie)


if __name__ == "__main__":
    imie = input("Podaj swoje imię: ")

    kolejka = multiprocessing.Queue()

    proces = multiprocessing.Process(
        target=wyslij_imie,
        args=(kolejka, imie)
    )

    proces.start()

    odebrane_imie = kolejka.get()

    proces.join()

    print(f"Witaj, {odebrane_imie}!")
