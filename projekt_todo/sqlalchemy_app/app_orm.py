
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# sqlalchemy_app/app_orm.py
from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Zadanie

def pokaz_zadania(db: Session):
    """Wyświetla listę wszystkich zadań."""
    zadania = db.query(Zadanie).all()
    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")
    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}")
    print("------------------------\n")

def dodaj_zadanie(db: Session, opis: str):
    nowe_zadanie = Zadanie(opis=opis)
    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)

def oznacz_jako_zrobione(db: Session, id_zadania: int):
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania o podanym ID.")
#   dodaje cały blok usuń_zadanie w ramach zadania 2
def usun_zadanie(db: Session, id_zadania: int):
    """Usuwa zadanie o podanym ID."""
    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()
    if zadanie:
        db.delete(zadanie)
        db.commit()
        print("Zadanie zostało usunięte!")
    else:
        print("Nie znaleziono zadania o podanym ID.")

def main():
    db_gen = get_db()
    db = next(db_gen)

    while True:
        print("Menu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")     #    dodaję w ramach zadania 2
        print("5. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            pokaz_zadania(db)
        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db, opis)
            print("Zadanie dodane!")
        elif wybor == '3':
            try:
                id_zad = int(input("Podaj ID: "))
                oznacz_jako_zrobione(db, id_zad)
            except ValueError:
                print("Podaj poprawny numer!")
        #    dodaję poniższy blok w ramach zadania 2
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania do usunięcia: "))
                usun_zadanie(db, id_zadania)
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == '5':
            print("Do zobaczenia!")
            db.close()
            break
        else:
            print("Nieznana opcja — spróbuj ponownie.")

if __name__ == "__main__":
    main()
