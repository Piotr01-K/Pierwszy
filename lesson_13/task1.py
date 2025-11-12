# 1. ✏ Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

import sqlite3
conn = sqlite3.connect("biblioteka.db")     # Łączy z (lokalną) bazą danych i tworzy plik
c = conn.cursor()     # narzędzie do wykonywana komend w SQL
# Tworzy tabelę z "parametrami" ksiazki
c.execute("""      
CREATE TABLE IF NOT EXISTS ksiazki (
    id INTEGER PRIMARY KEY,
    tytul TEXT NOT NULL,
    autor TEXT NOT NULL,
    rok_wydania INTEGER
)
""")
conn.commit()   # Zapisuje zmiany
conn.close()    # Zamyka połączenie
print("Tabela ksiazki została utworzona w bazie biblioteka.db")