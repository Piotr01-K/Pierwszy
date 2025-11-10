print('Zadanie 3 – Lekcja 11')
# Zadanie 3 – Dziedziczenie Pracownik -> Programista
# Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
# oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
# dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
# stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje.

class Pracownik:     # Klasa bazowa
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa

    def oblicz_pensje(self, liczba_godzin):
        return self.stawka_godzinowa * liczba_godzin

class Programista(Pracownik):     # Klasa potomna
    def __init__(self, imie, stawka_godzinowa, jezyki_programowania):
        super().__init__(imie, stawka_godzinowa)    # konstruktor z klasy nadrzędnej (Pracownik)
        self.jezyki_programowania = jezyki_programowania     # Dodaję własny atrybut dla programisty

# Tworzę obiekt klasy Programista pracujący ze stawką 60 zł/h ze znajomością 2 języków opr.
programista_konkretny = Programista("Piotr Informatyczny", 60, ["Visual Basic", "Python", "C++"])

# Metoda odziedziczona po klasie Pracownik
pensja = programista_konkretny.oblicz_pensje(140)  # np. Pan Piotr pracuje 140 godzin/mc

print("Imię:", programista_konkretny.imie)
print("Stawka godzinowa:", programista_konkretny.stawka_godzinowa, "zł")
print("Języki programowania:", ", ".join(programista_konkretny.jezyki_programowania))
print("Miesięczna pensja:", pensja, "zł")