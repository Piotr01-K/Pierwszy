# 11. Napisz program dziennik od nowa tym razem wykorzystując paradygmaty obiektowe (możecie też rozwinąć dziennik. 
#    Nie usuwajcie "starego dziennika" możecie stworzyć dwa repo, lub dwa directory, które pokaża dwa rozwiązania. Oddawanie przez gita

import json
import os

class Dziennik:
    def __init__(self, plik="dziennik.json"):    # konstruktor klasy dziennik uruchomi się gdy powstanie obiekt Dziennik
        self.plik = plik   # przypisuje nazwę pliku do obiektu
        self.wpisy = []    # pusta lista na starcie
        self.wczytaj()    

    def wczytaj(self):    # jeśli jakieś dotychczasowe wpisy istnieją to je wczytaj
        if os.path.exists(self.plik):    # sprawdzam czy plik istnieje
            try:
                with open(self.plik, "r", encoding="utf-8") as f:
                    self.wpisy = json.load(f)    # odczytaną zawartość pliku konwestuje z JSON do obiektu Python
                print("Wczytano poprzednie wpisy.")
            except json.JSONDecodeError:    # gdy plik jest pusty lub niepoprawny....
                print("Plik pusty lub uszkodzony!") # ... informuje o błędzie i ....
                self.wpisy = []    # ....tworzy pustą listę (a nie wywala)
        else:
            print("Nie znalazłem pliku - tworzę nowy dziennik")
            self.wpisy = []  
    def zapisz(self):
        with open(self.plik, "w", encoding="utf-8") as f:    # otwiera dziennik do zapisu
            json.dump(self.wpisy, f, ensure_ascii=False, indent=4)    # zapisuje listę w JSON do dziennika
        print("Zapisano dziennik.")
    def dodaj_wpis(self):
        tekst = input("Wpisz treść: ").strip()    # pobiera dane od użytkownika usuwając puste spacje
        if tekst:
            self.wpisy.append(tekst)   # dodaje wpisany przez użytkownika tekst do listy
            print("Dodano wpis.")
        else:
            print("pis nie może być pusty.")   # informacja na wypadek braku wpisu
    def pokaz_wpisy(self):
        if not self.wpisy:
            print("Brak wpisów.")    # informuje, gdy brak wpisów
        else:
            print("\nTwoje wpisy:")    # informuje o wpisach...
            for i, w in enumerate(self.wpisy, 1):   #...przechodzi w pętli po każdej pozycji (listy) numerując je
                print(f"{i}. {w}")    # wyświetl numer pozycji (i) i jej treść (w)
            print()
    def uruchom(self):
        while True:   # pętla do do menu do wyboru (wielokrotnego) właściwej opcji przez użytkownika
            print("\n--- MENU ---")
            print("1. Dodaj wpis")
            print("2. Pokaż wpisy")
            print("3. Zakończ")
            wybor = input("Wybierz opcję: ")
            if wybor == "1":
                self.dodaj_wpis()
            elif wybor == "2":
                self.pokaz_wpisy()    # pokazuje dotychczasowe wpisy
            elif wybor == "3":
                self.zapisz()
                print("Dziękuję i do zobaczenia!")
                break
            else:
                print("Nieprawidłowa opcja.")
if __name__ == "__main__":
    Dziennik().uruchom()