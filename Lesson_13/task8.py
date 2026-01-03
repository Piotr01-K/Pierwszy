# Zadanie 8 – Połącz tabele (Relacja)
# To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
# audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
# samej bazie uczelnia.db. Tabela powinna mieć strukturę:
# - id_przypisania (INTEGER, klucz główny)
# - id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
# tabeli studenci .
# - id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
# audytoria 

import sqlite3
import os
conn = sqlite3.connect("uczelnia.db")
conn.execute("PRAGMA foreign_keys = ON")   # Trzeba ręcznie włączyć obsługę kluczy obcych (w SQL)
cursor = conn.cursor()
# Tworzy tabelę przypisania
cursor.execute("""
CREATE TABLE IF NOT EXISTS przypisania (
    id_przypisania INTEGER PRIMARY KEY AUTOINCREMENT,
    id_studenta INTEGER NOT NULL,
    id_audytorium INTEGER NOT NULL,
    FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
    FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
);
""")
conn.commit()
conn.close()
print("Tabela 'przypisania' została utworzona.")
