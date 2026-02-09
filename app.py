# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Witam serdecznie!'
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# blok dodany w ramach zadania 3 — lista ulubionych filmów
favorite_movies = [
    "Obcy",
    "Star Wars",
    "Matrix",
    "Avatar",
    "Pewnego razu na dzikim Zachodzie"
]

@app.route('/')
def index():
    users = ['Adam', 'Ewa', 'Karol']
    return render_template('index.html', title='Strona Główna', users=users)

@app.route('/user/<name>')
def user_page(name):
    return render_template('user.html', username=name)

#  # blok dodany w ramach zadania 3 — /movies
#  @app.route('/movies')
#  def movies():
#      return render_template('movies.html', movies=favorite_movies)

#   blok dodany w ramach zadania 4
@app.route('/movies')
def movies_page():
    movies = ['Matrix', 'Pewnego razu na dzikim Zachodzie', 'Obcy']
    page_title = "Moje ulubione filmy"
    return render_template('movies.html', movies=movies, page_title=page_title)

if __name__ == '__main__':
    app.run(debug=True)
