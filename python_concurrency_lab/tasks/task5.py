import threading

# Wspólna lista
wspolna_lista = []

# Tworzymy blokadę
lock = threading.Lock()


def dodaj_jedynki():
    """Dodaje liczbę 1 do listy 100 000 razy (BEZPIECZNIE)"""
    for _ in range(100_000):
        with lock:  # tylko jeden wątek naraz
            wspolna_lista.append(1)


def dodaj_dwojki():
    """Dodaje liczbę 2 do listy 100 000 razy (BEZPIECZNIE)"""
    for _ in range(100_000):
        with lock:
            wspolna_lista.append(2)


# Tworzymy wątki
watek_1 = threading.Thread(target=dodaj_jedynki)
watek_2 = threading.Thread(target=dodaj_dwojki)

# Start
watek_1.start()
watek_2.start()

# Czekamy na zakończenie
watek_1.join()
watek_2.join()

# Sprawdzamy wynik
print(f"Długość listy: {len(wspolna_lista)}")
