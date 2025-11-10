print('Zadanie 1 – Lekcja 11')

# Lekcja 11 - Zadanie 1 – Klasa Film
# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
# rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
# informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
# obiekty tej klasy i wydrukuj informacje o nich

class Film:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul    # atrybuty filmu
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji
    def informacje(self):    # metoda (udzielenie informacji) zwracająca informacje o filmie
        return f"tytuł: {self.tytul}, rok produkcji: {self.rok_produkcji}, reżyseria: {self.rezyser}."

# Tworzę dwa obiekty (filmy) tej samej klasy
film_1 = Film("Titanic", "James Cameron", 1997)
film_2 = Film("Ojciec Chrzesny", "Francis Ford Coppola", 1972)

print("Film 1:", film_1.informacje())
print("Film 2:", film_2.informacje())