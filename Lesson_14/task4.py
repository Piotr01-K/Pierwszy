# Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().

import sqlite3
conn = sqlite3.connect("sklep.db")
cur = conn.cursor()
# Zapytanie SQL – obliczenie średniej ceny książek
# AVG() – liczy średnią z kolumny
# Łączy tabelę Produkty z tabelą Kategorie, cel: wybór pozycji z kategorii "Książki".
cur.execute("""
    SELECT AVG(Produkty.cena)
    FROM Produkty
    JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
    WHERE Kategorie.nazwa_kategorii = 'Książki'
""")
wynik = cur.fetchone()  # pobiera jedną liczbę stanowiącą AVG
srednia_cena = wynik[0]  # krotka
print(f"Średnia cena książek: {srednia_cena:.2f} PLN")
conn.close()

