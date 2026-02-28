import threading
import time

def zadanie_dla_watku():
    """Prosta funkcja, którą wykona nasz wątek."""
    print("Wątek startuje...")
    time.sleep(2)
    print("Wątek kończy pracę.")

thread = threading.Thread(target=zadanie_dla_watku)
thread.start()

print("Główny program czeka...")

thread.join()

print("Główny program zakończył działanie.")
