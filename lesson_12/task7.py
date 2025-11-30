# Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
# nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
# tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
    @classmethod
    def ze_stringa(cls, tekst):
        dzien, miesiac, rok = tekst.split("-")  # tutaj rozbijam datę na składowe (tekstowe)
        return cls(int(dzien), int(miesiac), int(rok))    # konwersja na int; tutaj jest cls a nie self gdyż metoda dopiero tworzy obiekt
data1 = Data.ze_stringa("25-12-2023")     # Testuję, (data1 to jest nowy objekt klasy Data) 
print(data1.dzien, data1.miesiac, data1.rok)
