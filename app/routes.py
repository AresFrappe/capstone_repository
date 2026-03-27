from flask import Blueprint, render_template, request, redirect, url_for, session
from .authentication_db.mysql import register_user, login_user
from .capstone_db.mongodb import get_all_capstones, insert_capstone, delete_capstone

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


## ============= Main Page =============

@main.route("/mainpage")
def mainpage():

    capstones = get_all_capstones()

    return render_template(
        "mainpage.html",
        capstones=capstones
    )

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
# admin dashboard
@main.route("/admin")
def admin_dashboard():
    if session.get("username") != "admin":
        return redirect(url_for("main.login"))

    return render_template("admin/dashboard.html")

# adding capstone
@main.route("/admin/add_capstone", methods=["GET", "POST"])
def add_capstone():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]

        if insert_capstone(title, author, year):
            print("Capstone added successfully", title, author)
            return redirect(url_for("main.admin_dashboard"))

# redirect to manage capstones page
@main.route("/admin/manage_capstones")
def manage_capstones():
    capstones = get_all_capstones()
    return render_template("admin/manage.html", capstones=capstones)

# delete capstone
@main.route("/admin/delete_capstone/<capstone_id>")
def delete(capstone_id):
    if delete_capstone(capstone_id):
        print("Capstone deleted successfully", capstone_id)
        return redirect(url_for("main.manage_capstones"))
    
