import threading

# WSPÓLNA lista dla obu wątków
wspolna_lista = []


def dodaj_jedynki():
    """Dodaje liczbę 1 do listy 100 000 razy"""
    for _ in range(100_000):
        wspolna_lista.append(1)


def dodaj_dwojki():
    """Dodaje liczbę 2 do listy 100 000 razy"""
    for _ in range(100_000):
        wspolna_lista.append(2)


# Tworzymy dwa wątki
watek_1 = threading.Thread(target=dodaj_jedynki)
watek_2 = threading.Thread(target=dodaj_dwojki)

# Uruchamiamy wątki
watek_1.start()
watek_2.start()

# Czekamy aż oba się zakończą
watek_1.join()
watek_2.join()

# Sprawdzamy wynik
print(f"Długość listy: {len(wspolna_lista)}")