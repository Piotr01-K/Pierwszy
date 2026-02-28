import threading
import time
import random

def witaj(numer):
    time.sleep(random.uniform(0, 0.5))
    print(f"Wątek {numer} mówi: Cześć!")

watki = []

for i in range(5):
    thread = threading.Thread(target=witaj, args=(i,))
    watki.append(thread)
    thread.start()

for thread in watki:
    thread.join()

print("Koniec programu.")
