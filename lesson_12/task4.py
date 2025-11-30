# 4. ✏ Zadanie 4 – Bezpieczne dzielenie
# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
# try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
# zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!".

def bezpieczne_dzielenie(a, b):
    try:
        wynik = a / b
        return wynik
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")
        return None   # ....i nie wywala!
# Testuję warianty
print("17 / 2 =", bezpieczne_dzielenie(17, 2))
print("7 / 0 =", bezpieczne_dzielenie(7, 0))