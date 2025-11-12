# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3
conn = sqlite3.connect("uczelnia.db")    # łączy się z bazą uczelnia.db (lub ją tworzy)
cur = conn.cursor()
# Tworzy tabelę Studenci
cur.execute("""
CREATE TABLE IF NOT EXISTS studenci (
    id_studenta INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL
);
""")
# Tworzy tabelę Audytoria
cur.execute("""
CREATE TABLE IF NOT EXISTS audytoria (
    id_audytorium INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_budynku TEXT NOT NULL,
    numer_sali INTEGER NOT NULL
);
""")
conn.commit()
conn.close()
print("Tabele zostały zapisane!")