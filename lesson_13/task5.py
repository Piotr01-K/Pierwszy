# Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.

import sqlite3
conn = sqlite3.connect("biblioteka.db")
cur = conn.cursor()
tytul = "Don Kichot"   # <-- tutaj wpisuję tytuł książki z aktualizowanym rokiem wydania
nowy_rok = 1602   # <-- a tu nowy rok wydania
cur.execute(
    "UPDATE ksiazki SET rok_wydania = ? WHERE tytul = ?",    # aktualizacja roku w bazie
    (nowy_rok, tytul)
)
conn.commit()  # zapisuje zmiany w bazie
cur.execute("SELECT * FROM ksiazki WHERE tytul = ?", (tytul,))    # pobiera zaktualizowaną pozycję książki
wynik = cur.fetchone()
print("\nZaktualizowana książka:")
print("---------------------------")
print(f"ID: {wynik[0]}")
print(f"Tytuł: {wynik[1]}")
print(f"Autor: {wynik[2]}")
print(f"Rok wydania: {wynik[3]}")
conn.close()