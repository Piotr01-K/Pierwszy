# Zadanie 4 – Dynamiczny tytuł strony
# Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html również
# zmienną page_title z wartością "Moje ulubione filmy". Użyj tej zmiennej w znaczniku

#   W pliku app.py zamieniam bok /movies na następujący:
#   blok dodany w ramach zadania 4
# @app.route('/movies')
# def movies_page():
#     movies = ['Matrix', 'Pewnego razu na dzikim Zachodzie', 'Obcy']
#     page_title = "Moje ulubione filmy"
#     return render_template('movies.html', movies=movies, page_title=page_title)


# W pliku movies dotychczasowy kod z zadania 3 zastępuję nowym w ramach zadania 4:

# <!DOCTYPE html>
# <html lang="pl">
# <head>
#     <meta charset="UTF-8">
#     <title>{{ page_title }}</title>
# </head>
# <body>
#     <h1>{{ page_title }}</h1>

#     <ul>
#         {% for film in movies %}
#             <li>{{ film }}</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>

