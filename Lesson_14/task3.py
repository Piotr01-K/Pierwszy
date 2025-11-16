# Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.

import sqlite3
conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()
#  suma cen produktów w kategorii "Elektronika"  
query = """
SELECT SUM(p.cena) AS laczna_wartosc
FROM Produkty AS p
JOIN Kategorie AS k ON p.id_kategorii = k.id_kategorii   
WHERE k.nazwa_kategorii = ?
"""
#  Wykonuje zapytanie "z parametrem"
cursor.execute(query, ("Elektronika",))
#    Pobiera wynik - fetchone(), zwraca krotkę, pierwszy element to suma
wynik = cursor.fetchone()
laczna_wartosc = wynik[0]  
if laczna_wartosc is None:    # może być None, jeśli brak produktów w tej kategorii
    print("Brak produktów w kategorii 'Elektronika'.")
else:
    print(f"Łączna wartość produktów w kategorii 'Elektronika wynosi': {laczna_wartosc:.2f} PLN")
conn.close()

