#   from models import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import event, text
from sqlalchemy.engine import Engine
from config import config
import time

db = SQLAlchemy()
migrate = Migrate()

# --- STATYSTYKI SQL --------------------------------------------------

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
    duration = (time.time() - context._query_start_time) * 1000
    sql_stats["count"] += 1
    sql_stats["total_time_ms"] += duration
    sql_stats["queries"].append({
        "query": statement,
        "duration_ms": round(duration, 3)
    })


# --- FUNKCJA TWORZĄCA APLIKACJĘ --------------------------------------

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    # Import modeli dopiero tutaj!
    from models import Booking, Notification

    # LISTENER AFTER_INSERT — dopiero po imporcie modeli
    from datetime import datetime

    @event.listens_for(Booking, "after_insert")
    def create_notification(mapper, connection, target):
        """
        Automatyczne powiadomienie dla admina po utworzeniu rezerwacji.
        """
        connection.execute(
            Notification.__table__.insert().values(
                user_id=1,
                message=f"Nowa rezerwacja sali: {target.room_id}",
                is_read=False,
                created_at=datetime.utcnow()
            )
        )

    # rejestrujemy blueprint
    from routes import main
    app.register_blueprint(main)

    # Test DB
    @app.route("/test-db")
    def test_db():
        try:
            db.session.execute(text("SELECT 1"))
            return "Połączenie z PostgreSQL OK!"
        except Exception as e:
            return f"Błąd połączenia z bazą: {str(e)}"

    return app


# --- START APLIKACJI -------------------------------------------------

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


