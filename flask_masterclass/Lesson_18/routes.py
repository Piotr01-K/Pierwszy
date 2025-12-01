from flask import Blueprint, render_template, request, jsonify
from app import db, sql_stats    #   dodałem w ramach task3
#   from app import db, query_counter    # dodałem w ramach task2
from models import Message

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