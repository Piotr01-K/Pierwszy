# Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().

import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()
# Zapytanie SQL - wybór nazwy i ceny najdroższego produktu
query = """
SELECT nazwa_produktu, cena
FROM Produkty
WHERE cena = (SELECT MAX(cena) FROM Produkty)
"""
cursor.execute(query)

produkt = cursor.fetchone()    # Pobieramy wynik (nazwa, cena)
if produkt:
    print(f"Najdroższy produkt to: {produkt[0]} (cena: {produkt[1]} PLN)")
else:
    print("Brak produktów w bazie.")
conn.close()
