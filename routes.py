from flask import redirect, render_template, request, session
from app import app
import auth
import rooms
import threads
import messages

@app.route("/")
def index():
    return render_template("index.html", rooms = rooms.get_rooms())

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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    if request.method == "POST":
        user = auth.login(request.form["username"], request.form["password"])
        if not user:
            return redirect("/")
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_confim = request.form["password-confirm"]
        if password != password_confim:
            return redirect("/error?type=password_match")
        success = auth.register(username, password)
        if not success:
            return redirect("/error?type=auth_sql")
    return redirect("/login")

@app.route("/rooms/<room_id>", methods=["GET"])
def one_room(room_id):
    room = rooms.get_room(room_id)
    thread_list = threads.get_threads(room_id)
    return render_template(
        "forum/room.html",
        room = room,
        admin = session["user_id"] == room.user_id,
        threads = thread_list
    )


@app.route("/rooms", methods=["POST"])
def post_room():
    name = request.form["name"]
    description = request.form["description"]
    status = request.form["status"]
    success = rooms.create_room(name, description, status, session["user_id"])
    if not success:
        return redirect("/error?type=none")
    return redirect("/")

@app.route("/threads", methods=["POST"])
def post_thread():
    name = request.form["name"]
    room_id = request.form["room_id"]
    user_id = session["user_id"]
    room = rooms.get_room(room_id)
    if room is None:
        return redirect("/error")
    if room.user_id != user_id:
        return redirect("/error")
    success = threads.create_thread(name, room_id)
    if not success:
        return redirect("/error")
    return redirect("/rooms/" + str(room.id))

@app.route("/messages", methods=["POST"])
def post_message():
    room_id = request.form["room_id"]
    content = request.form["content"]
    thread_id = request.form["thread_id"]
    user_id = session["user_id"]
    success = messages.create_message(content, thread_id, user_id)
    if not success:
        return redirect("/error")
    return redirect("/rooms/" + room_id)
    