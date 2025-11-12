# Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń."


print("Kalkulator (wpisz q aby zakończyć)")

while True:
    try:
        # Pobieramy dane od użytkownika
        a = input("Wpisz pierwszą liczbę: ")
        if a.lower() == "q":  
            break
        a = float(a)    # tekst na liczbę, żeby liczył
        b = input("Wpisz drugą liczbę: ")
        if b.lower() == "q":
            break
        b = float(b)    
        operacja = input("Podaj operację (+, -, *, /): ")
        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            wynik = a / b
        else:
            print("Nieznana operacja!")  # obsługa na wypadek inninych czy omyłkowych wpisów)
            continue
    except ValueError:
        print("Błąd: Wprowadzona wartość nie jest liczbą!")
    except ZeroDivisionError:
        print("Błąd: Nie można dzielić przez zero!")
    else:    # Wyświetli wynik jeśli nie było błędu
        print(f"Wynik: {wynik}")
    finally:
        print("Koniec obliczeń.\n")   # Wyświetla się po każdej operacji