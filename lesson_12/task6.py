# Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except.

class InvalidPasswordError(Exception):
    pass
def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Hasło musi mieć co najmniej 8 znaków!")
    else:
        print("Hasło zostało zapisane!")
#    Testuję warianty
try:
    ustaw_haslo("Pilot72")   # Próbuję hasło < 8
except InvalidPasswordError as x:
    print("Błąd:", x)
print("\nWeryfikuję dobre hasło:")
try:
    ustaw_haslo("Bardzodobrehaslo364")    # Próbuję hasło >= 8
except InvalidPasswordError as x:
    print("Błąd:", x)