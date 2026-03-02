import threading
import time

def witaj(numer_watku):
    print(f"Wątek numer {numer_watku} mówi: Cześć!")
    time.sleep(1)

watki = []

for i in range(5):
    thread = threading.Thread(target=witaj, args=(i,))
    watki.append(thread)
    thread.start()

print("Wszystkie wątki zostały uruchomione.")

for thread in watki:
    thread.join()

print("Wszystkie wątki zakończyły pracę.")
