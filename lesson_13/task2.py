# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem.

import sqlite3
connection = sqlite3.connect("biblioteka1.db")   # łączy się z bazą Biblioteka.db
cursor = connection.cursor()
ksiazki = [
    ("Przygody Tomka Sawyera", "Mark Twain", 1876),
    ("Don Kichot", "Miguel de Cervantes", 1605),
    ("Mechaniczna pomarańcza", "Anthony Burgess", 1962),
]
# Dodaje książki do tabeli
cursor.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)", ksiazki)
connection.commit()
connection.close()
print("Książki zostały dodane do bazy danych")
