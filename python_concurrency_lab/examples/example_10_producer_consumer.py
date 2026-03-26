import threading
import queue
import time
import random

q = queue.Queue()

def producent():
    for _ in range(5):
        time.sleep(1)
        liczba = random.randint(1, 100)
        print(f"Producent dodał: {liczba}")
        q.put(liczba)

def konsument():
    for _ in range(5):
        liczba = q.get()
        print(f"  Konsument pobrał: {liczba}")
        time.sleep(1.5)
        q.task_done()

t1 = threading.Thread(target=producent)
t2 = threading.Thread(target=konsument)

t1.start()
t2.start()

t1.join()
t2.join()

print("Koniec programu.")
