from flask import Blueprint, render_template, request, redirect, url_for, session
from . import mongo
from .authentication_db.mysql import register_user, login_user

main = Blueprint("main", __name__)

@main.route("/")
def home():
    capstones = mongo.db.capstones.find()
    return render_template("index.html", capstones=capstones)

@main.route("/mainpage")
def mainpage():
    return render_template("mainpage.html")


## ============= Authentication Routes =============

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    
        if register_user(username, password):
            return redirect(url_for("main.login"))

    return render_template("auth/register.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    
        user = login_user(username, password)

        if user:
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]

            if session["username"] == "admin":
                return redirect(url_for("main.admin_dashboard"))

            return redirect(url_for("main.mainpage"))

    return render_template("auth/login.html")

@main.route("/logout")
def logout():
    print("Logging out user:", session.get("username"))
    session.clear()
    return redirect(url_for("main.home"))


## ============= Admin Routes =============
@main.route("/admin")
def admin_dashboard():
    if session.get("username") != "admin":
        return redirect(url_for("main.login"))
    
    return render_template("admin/dashboard.html")