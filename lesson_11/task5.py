print('Zadanie 5 – Lekcja 11')

# Zadanie 5 – Polimorficzna Figura
# Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
# stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
# klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
# przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
# pętli wydrukuj pole każdej figury.

# Klasa bazowa (rodzic)
class Figura:
    def oblicz_pole(self):
        pass
# Klasa potomna – Kwadrat
class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok  # zapamiętuję długość boku
    def oblicz_pole(self):
        return self.bok ** 2     # bo pole kwadratu wynosi a²
# Klasa potomna – Koło
class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien  # zapamiętuję promień
    def oblicz_pole(self):
        PI = 3.14159
        return PI * (self.promien ** 2)    # bo pole koła wynosi πr²
# Tworzę dwa konkretne obieky klasy figura tj. kwadrat (o boku 5) i koło (o promieniu 4)
kwadrat = Kwadrat(5)
kolo = Kolo(4)
figury = [kwadrat, kolo]
for figura in figury:
    if isinstance(figura, Kwadrat):
        print(f"Pole kwadratu: {figura.oblicz_pole():.2f}")
    elif isinstance(figura, Kolo):
        print(f"Pole koła: {figura.oblicz_pole():.2f}")
