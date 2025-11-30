print('Zadanie 4 – Lekcja 11')

# Zadanie 4 – Czytelny Punkt
# Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
# metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y).

class Punkt:
    def __init__(self, nazwa, x, y):
        self.nazwa = nazwa
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.nazwa}: ({self.x}, {self.y})"
A = Punkt("Punkt A", 4, 7)
print(A)