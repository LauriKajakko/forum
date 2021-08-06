from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash
from app import app
from db import db
import auth

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    if request.method == "POST":
        user = auth.login(request.form["username"], request.form["password"])
        if not user:
            return redirect("/")
        return redirect("/")

@app.route("/error")
def error():
    error_type = request.args.get("type")
    if error_type == "password_match":
        message = "Salasana ja vahvistus eivät täsmää."
    elif error_type == "auth_sql":
        message = "Käyttäjänimi tai salasana ei kelvollinen."
    else:
        message = "Virhe."
    return render_template("error.html", message = message)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_confim = request.form["password-confirm"]
        if password != password_confim:
            return redirect("/registration_failed?type=no_match")
        success = auth.register(username, password)
        if not success:
            return redirect("/error?type=auth_sql")
        return redirect("/login")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
