# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora.

import sqlite3
conn = sqlite3.connect("biblioteka.db")
cur = conn.cursor()
# Pobieram od użytkownika imię i nazwisko autora
autor = input("Podaj imię i nazwisko autora szukanej pozycji książkowej: ")
# Zapytanie SQL wyszukujące książki po autorze
cur.execute("SELECT * FROM ksiazki WHERE autor = ?", (autor,))
wyniki = cur.fetchall()    # Pobieramy wyniki
if not wyniki:
    print(f"Brak książek autora: {autor}")
else:
    print(f"\nKsiążki autora {autor}:")
    print("-" * 50)    # linia pod nagłówkiem
    for id, tytul, autor, rok in wyniki:
        print(f"{id}. {tytul} ({rok})")    # wyświetla książkę wpisanego autora
conn.close()