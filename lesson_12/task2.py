# 2. ✏ Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.

class Uzytkownik:
    def __init__(self, wiek):
        # zgodnie z przyjętą konwencją użyję podkreślnika do ustalenia prywatnej zmiennej dot. wieku
        self._wiek = wiek
    @property    # Getter
    def wiek(self):
        return self._wiek    # zwraca aktualny wiek użytkownika
    @wiek.setter    # Setter - ustawia nową wartość wieku
    def wiek(self, nowy_wiek):
        if 0 <= nowy_wiek <= 120:     # walidacja
            self._wiek = nowy_wiek     # ustawia nową wartość wieku gdy się mieści 0-120 lat
        else:
            print("Błędny wiek!")    # błędny wiek więc nie zmienia jego wartości
u = Uzytkownik(35)    # Tworzę użytkownika
print("Aktualny wiek:", u.wiek)  # tutaj wywołuje getter
# Próbuję zastosować nowy wiek
u.wiek = 57  # tutaj wywołuje setter
print("Zmieniony wiek:", u.wiek)
# Próbuję zastosować błędny wiek - nie zmienia jego wartości na błędny!
u.wiek = 200  # setter blokuje zmianę
print("Zmiana wieku na złą wartość nie ppowiodła się, pozstaje poprzednia:", u.wiek)
