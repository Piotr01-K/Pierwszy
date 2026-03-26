# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.

import sqlite3

try:
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    # Pobieramy ID studentów
    c.execute("SELECT id_studenta FROM studenci")
    studenci = [row[0] for row in c.fetchall()]

    # Pobieramy ID audytoriów
    c.execute("SELECT id_audytorium FROM audytoria")
    audytoria = [row[0] for row in c.fetchall()]

    # Jeśli nie ma danych, informujemy
    if not studenci or not audytoria:
        print("❗ Brak studentów lub audytoriów — dodaj dane najpierw.")
    else:
        i = 0  # indeks audytorium
        for student_id in studenci:
            audytorium_id = audytoria[i]
            c.execute(
                "INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)",
                (student_id, audytorium_id)
            )
            i = (i + 1) % len(audytoria)  # przechodzimy w kółko przez listę sal

        conn.commit()
        print("✅ Przypisania studentów do audytoriów zostały dodane!")

except sqlite3.Error as e:
    print("❌ Błąd bazy danych:", e)

finally:
    if 'conn' in locals():
        conn.close()
        print("🔒 Połączenie zamknięte.")
