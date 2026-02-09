import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="moja_baza",
        user="postgres",
        password="Bylejakiehaslo"
    )
    return conn

@app.route('/users')
def list_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)