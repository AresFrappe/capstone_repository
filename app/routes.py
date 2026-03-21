from flask import Blueprint, render_template, request, redirect, url_for
from . import mongo

main = Blueprint("main", __name__)

@main.route("/")
def home():
    capstones = mongo.db.capstones.find()
    return render_template("index.html", capstones=capstones)

@main.route("/admin")
def admin_dashboard():
    return render_template("admin/dashboard.html")

@main.route("/login")
def login():
    return render_template("auth/login.html")

@main.route("/add", methods=["POST"])
def add_capstone():

    title = request.form.get("title")
    author = request.form.get("author")

    mongo.db.capstones.insert_one({
        "title": title,
        "author": author
    })

    return redirect(url_for("main.home"))