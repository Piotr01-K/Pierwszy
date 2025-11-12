# 3. ✏ Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
# usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
# stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.

class KalkulatorWalut:
    @staticmethod    # nie potrzebuje self ani danych klasy!
    def usd_na_pln(kwota_usd):
        staly_kurs = 4.0  # stały kurs: 1 USD = 4 PLN
        return kwota_usd * staly_kurs
kwota_w_usd = 37    # Wywołuję metodę bez utworzenia obiektu klasy!
kwota_w_pln = KalkulatorWalut.usd_na_pln(kwota_w_usd)
print(f"{kwota_w_usd} USD to {kwota_w_pln} PLN")
