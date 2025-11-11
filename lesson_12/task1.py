# 1. ✏ Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.

from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int
    def __str__(self):
        # ustalam odpowiedni format wyświetlenia wyników:
        return f"Film(tytul: '{self.tytul}', rezyser: '{self.rezyser}', rok_produkcji: {self.rok_produkcji})"
film1 = Film("Pianista", "CRoman Polański", 2002)
film2 = Film("Pulp Ficion", "Quentin Tarantino", 1994)
print(film1)
print(film2)