# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.

import sqlite3

def znajdz_sale_studenta(nazwisko):
    try:
        conn = sqlite3.connect("uczelnia.db")
        c = conn.cursor()

        zapytanie = """
        SELECT s.imie, s.nazwisko, a.nazwa_budynku, a.numer_sali
        FROM przypisania p
        JOIN studenci s ON p.id_studenta = s.id_studenta
        JOIN audytoria a ON p.id_audytorium = a.id_audytorium
        WHERE s.nazwisko = ?
        """

        c.execute(zapytanie, (nazwisko,))
        wynik = c.fetchone()

        if wynik:
            imie, nazwisko, budynek, sala = wynik
            print(f"✅ Student: {imie} {nazwisko} → Budynek {budynek}, Sala {sala}")
        else:
            print("❓ Nie znaleziono studenta o takim nazwisku.")

    except sqlite3.Error as e:
        print("❌ Błąd bazy danych:", e)

    finally:
        if 'conn' in locals():
            conn.close()


# Test funkcji
znajdz_sale_studenta("Kowalski")