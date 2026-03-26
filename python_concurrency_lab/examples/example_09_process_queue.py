from multiprocessing import Process, Queue

def pracownik(kolejka_zadan, kolejka_wynikow):
    for zadanie in iter(kolejka_zadan.get, "STOP"):
        wynik = zadanie * 2
        kolejka_wynikow.put(wynik)


if __name__ == "__main__":
    zadania = Queue()
    wyniki = Queue()

    for i in range(5):
        zadania.put(i)

    p = Process(target=pracownik, args=(zadania, wyniki))
    p.start()

    zadania.put("STOP")
    p.join()

    while not wyniki.empty():
        print("Wynik:", wyniki.get())
