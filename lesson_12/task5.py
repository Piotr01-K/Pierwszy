# 5. ✏ Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikowi

try:
    with open("nieistniejacy.txt", "r", encoding="utf-8") as plik:
        odczytana_tresc = plik.read()
        print("Zawartość pliku:")
        print(odczytana_tresc)
except FileNotFoundError:
    print("Błąd: Plik 'nieistniejacy.txt' nie został znaleziony.")
