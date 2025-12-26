from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguracja połączenia
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Bylejakiehaslo@localhost/moja_baza"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODEL = tabela w bazie
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
#     Endpoint
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

#    Dopisany Endpoint w ramach Task1 Lesson_17
@app.route('/me')
def me():
    return "Piotr Kaźmierczuk"

#    Dopisany Endpoint w ramach Task2 Lesson_17
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    suma = num1 + num2    # ten wpis da potem to, że w przeglądarce wpisuję http://127.0.0.1:5000/add/4/19  i otrzymuję sumę liczby 4 i 19 
    return f"Wynik to: {suma}"   #  W przeglądarce wyświetla: Wynik to: 23

if __name__ == '__main__':
    app.run(debug=True)