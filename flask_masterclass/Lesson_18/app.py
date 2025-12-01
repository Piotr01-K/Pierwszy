from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
from config import config

from sqlalchemy import event
from sqlalchemy.engine import Engine
import time

# Rozszerzone statystyki
sql_stats = {
    "count": 0,
    "queries": [],
    "total_time_ms": 0
}

@event.listens_for(Engine, "before_cursor_execute")
def before_execute(conn, cursor, statement, parameters, context, executemany):
    context._query_start_time = time.time()

@event.listens_for(Engine, "after_cursor_execute")
def after_execute(conn, cursor, statement, parameters, context, executemany):
    duration = (time.time() - context._query_start_time) * 1000  # ms
    sql_stats["count"] += 1
    sql_stats["total_time_ms"] += duration
    sql_stats["queries"].append({
        "query": statement,
        "duration_ms": round(duration, 3)
    })

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    # rejestrujemy blueprint routes.py
    from routes import main
    app.register_blueprint(main)

    # TEST POŁĄCZENIA Z BAZĄ
    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute(text("SELECT 1"))
            return "Połączenie z PostgreSQL OK!"
        except Exception as e:
            return f"Błąd połączenia z bazą: {str(e)}"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


