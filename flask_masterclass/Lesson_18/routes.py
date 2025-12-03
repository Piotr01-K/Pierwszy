from models import Booking   #  dodałem w ramach zaania 4
from flask import Blueprint, render_template, request, jsonify
from app import db, sql_stats    #   dodałem w ramach task3
#   from app import db, query_counter    # dodałem w ramach task2
from models import Message
from models import Notification
from flask import jsonify
from app import sql_stats

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            new_msg = Message(text=msg)
            db.session.add(new_msg)
            db.session.commit()
            return render_template("form.html", message=msg)

@main.route("/query-count")
def query_count():
    return {"queries_executed": sql_stats["count"]}

@main.route("/stats")
def stats():
    return jsonify(sql_stats)

#   dodałem w ramach zadania 4
@main.route("/api/notifications", methods=["GET"])
def api_get_notifications():
    user_id = 1  # tymczasowo
    notifs = Notification.query.filter_by(user_id=user_id, is_read=False).order_by(Notification.created_at.desc()).all()
    return jsonify([n.to_dict() for n in notifs])

#   dodałem w ramach zadania 4
@main.route("/api/notifications/<int:notification_id>/read", methods=["POST"])
def api_mark_notification_read(notification_id):
    n = Notification.query.get(notification_id)
    if not n:
        return jsonify({"error": "not found"}), 404
    n.is_read = True
    db.session.commit()
    return jsonify({"status": "ok"})

#   dodałem w ramach zadania 4
main = Blueprint("main", __name__)
@main.route("/test-queries")
def test_queries():
    from app import sql_stats
    # wykonujemy kilka zapytań SQL
    bookings = Booking.query.all()
    notifications = Notification.query.all()

    return jsonify(sql_stats)