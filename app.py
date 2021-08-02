from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///lkajakko"
db = SQLAlchemy(app)

@app.route("/")
def index(): 
    return render_template("index.html") 

@app.route("/login")
def getLogin():
    return render_template("auth/login.html") 

@app.route("/login",methods=["POST"])
def postLogin():
    username = request.form["username"]
    result = db.session.execute(
        "SELECT id, password_hash FROM users WHERE username=:username",
        {"username": username}
    )
    user = result.fetchone()    
    if not user:
        return redirect("/")
    if check_password_hash(user.password_hash, request.form["password"]):
        session["username"] = username
    return redirect("/")


@app.route("/reqister")
def getReqister():
    return render_template("auth/reqister.html")

@app.route("/reqistration_failed")
def getReqisterFail():
    return render_template("auth/reqister_fail.html")

@app.route("/reqister",methods=["POST"])
def postReqister():
    
    username = request.form["username"]
    password = request.form["password"]
    passwordConfim = request.form["password-confirm"]
    if (password != passwordConfim): return redirect("/reqistration_failed")
    db.session.execute(
        "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)", 
        {
            "username": username,
            "password_hash": generate_password_hash(password)
        }
    )
    db.session.commit()
    return redirect("/login")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")