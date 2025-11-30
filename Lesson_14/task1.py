# Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().

import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()
query = "SELECT COUNT(*) FROM Produkty"   # Zapytanie SQL — liczy rekordy z tabeli Produkty
cursor.execute(query)    # tutaj wysyła to zapytanie
liczba_produktow = cursor.fetchone()[0]    # Pobiera wynik (0 bo to pierwszy wynik z krotki)
print("Liczba produktów: ", liczba_produktow)
conn.close()