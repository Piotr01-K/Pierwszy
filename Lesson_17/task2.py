#  Zadanie 2 – Prosty kalkulator
#  Utwórz ścieżkę /add/<int:num1>/<int:num2>. Funkcja przypisana do tej ścieżki powinna
#  przyjąć dwie liczby jako argumenty, zsumować je i zwrócić wynik w formacie "Wynik to:
#  [suma]".

#    Dopisuję Endpoint w ramach Task2 Lesson_17
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    suma = num1 + num2    # ten wpis da potem to, że w przeglądarce wpisuję http://127.0.0.1:5000/add/4/19  i otrzymuję sumę liczby 4 i 19 
    return f"Wynik to: {suma}"   #  W przeglądarce wyświetla: Wynik to: 23