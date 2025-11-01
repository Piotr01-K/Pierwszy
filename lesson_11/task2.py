print('Zadanie 2 – Lekcja 11')

# Zadanie 2 – Atrybuty Produkt
# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
# obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.

class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        # zapisuję atrybuty produktu
        self.nazwa = nazwa         
        self.cena = cena           
        self.kategoria = kategoria 

# Tworzę obiekt klasy Produkt
Zabawki = Produkt("Gry", 65.20, "Strategiczne")

# Wyświetlam każdy atrybut osobno
print("Nazwa produktu:", Zabawki.nazwa)
print("Cena produktu:", Zabawki.cena)
print("Kategoria produktu:", Zabawki.kategoria)



