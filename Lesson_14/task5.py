# Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.

import sqlite3
conn = sqlite3.connect("sklep.db")
cur = conn.cursor()
cur.execute("SELECT imie, email FROM Klienci")    # wybierz kolumnę "imię" i "Klienci"
klienci = cur.fetchall()     # fetchall pobierze wszystkie wyniki
print("Lista klientów:")
for imie, email in klienci:
   print(f"- {imie}: {email}")
conn.close()