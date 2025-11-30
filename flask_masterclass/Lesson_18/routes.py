from flask import Blueprint, render_template, request
from app import db
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

    return render_template("form.html", message=None)
