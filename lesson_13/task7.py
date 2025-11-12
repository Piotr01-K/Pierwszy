# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.

import sqlite3
try:
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()
    # dane do wstawienia
    studenci = [
        ("Piotr", "Iksiński"),
        ("Ewa", "Kłos"),
        ("Paweł", "Politechniczny"),
        ("Anna", "Gołąbek")
    ]
    audytoria = [
        ("Bud A", 37),
        ("Bud B", 76),
        ("Bud C", 101)
    ]
    #   wstawianie danych do tabeli
    c.executemany(     # wstawia wiele rekordów jednocześnie
        "INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", studenci)
    c.executemany(
        "INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", audytoria)
    conn.commit()
    print("Dane zostały dodane do bazy uczelnia.db!")
except sqlite3.Error as i:
    print("Błąd bazy danych:", i)
finally:
    if 'conn' in locals():    # zamknij tylko jeśli jest połączenie! (Po co? Bo jest try...except)
        conn.close()