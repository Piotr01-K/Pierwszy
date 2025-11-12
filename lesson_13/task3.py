# Zadanie 3 – Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
# tabeli ksiazki.

import sqlite3
conn = sqlite3.connect("biblioteka.db")
cur = conn.cursor()
print("Lista książek w bibliotece:")
print("-" * 50)    # pozioma linia pod tytułem w tabelce
for id, tytul, autor, rok in cur.execute("SELECT * FROM ksiazki"):     # Wykonujemy SELECT i w pętli od razu drukujemy wyniki
    print(f"{id:>2} | {tytul:<25} | {autor:<20} | {rok}")     # wyrownanie do prawej i lewej, wcięcia, "|" tworzą kolumny
# Zamykamy połączenie
conn.close()