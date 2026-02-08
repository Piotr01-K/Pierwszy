import threading
import time

def zadanie_watku():
    time.sleep(3)
    print("Wątek zakończył pracę!")

# Tworzymy wątek
thread = threading.Thread(target=zadanie_watku)

# Uruchamiamy wątek
thread.start()

print("Główny program czeka na wątek...")

# Czekamy, aż wątek się zakończy
thread.join()

print("Główny program zakończył działanie.")
