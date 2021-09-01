from flask import redirect, render_template, request, session, abort
from app import app
import auth
import users
import rooms
import threads
import messages

@app.route("/")
def index():
    return render_template("index.html", rooms = rooms.get_public_rooms())

@app.route("/error")
def error():
    return render_template("error.html", message = "Tuntematon virhe!")


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
            return redirect("/error")
        if len(username) < 3:
            return render_template(
                "error.html",
                message="Käyttäjänimen tulee olla vähintään 3 merkkiä pitkä"
            )
        if len(password) < 8:
            return render_template(
                "error.html",
                message="Salasanan tulee olla vähintään 8 merkkiä pitkä"
            )
        success = auth.register(username, password)
        if not success:
            return redirect("/error")
    return redirect("/")

@app.route("/rooms/<room_id>", methods=["GET"])
def one_room(room_id):
    user_id = session["user_id"]
    room = rooms.get_room(room_id)
    thread_list = threads.get_threads(room_id)
    admin = user_id == room.user_id or users.check_admin_status(user_id, room_id)
    return render_template(
        "forum/room.html",
        room = room,
        admin = admin,
        threads = thread_list
    )

@app.route("/rooms/<room_id>/delete", methods=["POST"])
def delete_room(room_id):
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    user_id = session["user_id"]
    room = rooms.get_room(room_id)
    if room.user_id != user_id:
        return render_template("error.html", message="Et omista huonetta")
    success = rooms.delete_room(room_id)
    if not success:
        return render_template("error.html", message="Virhe poistaessa huonetta")
    return redirect("/")



@app.route("/rooms/<room_id>/settings", methods=["GET"])
def one_room_settings(room_id):
    user_id = session["user_id"]
    room = rooms.get_room(room_id)
    admin = user_id == room.user_id or users.check_admin_status(user_id, room_id)
    if not admin:
        return redirect("/error")
    search = request.args.get("search") or ""
    user_results = users.get_users_like(search)
    room_admins = users.get_admins_by_room(room_id)
    return render_template(
        "forum/room_settings.html",
        room = room,
        admin = session["user_id"] == room.user_id,
        user_results = user_results,
        search = search,
        room_admins = room_admins
    )

@app.route("/rooms/<room_id>/admins", methods=["POST"])
def admins(room_id):
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    user_id = session["user_id"]
    user_to_add_id = request.form["user_to_add_id"]
    room = rooms.get_room(room_id)
    if room is None:
        return redirect("/error")
    if room.user_id != user_id:
        return redirect("/error")
    success = rooms.add_admin(user_to_add_id, room_id)
    if not success:
        return render_template("error.html", message="Tarkistathan onko käyttäjä jo admin")
    return redirect("/rooms/" + room_id + "/settings")

@app.route("/rooms", methods=["POST"])
def post_room():
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    name = request.form["name"]
    if len(name) > 50:
        return render_template(
            "error.html",
            message="Nimi saa olla korkeintaan 50 merkkiä pitkä"
        )
    if len(name) < 3:
        return render_template(
            "error.html",
            message="Nimen tulee olla vähintään 3 merkkiä pitkä"
        )

    description = request.form["description"]
    if len(description) > 200:
        return render_template(
            "error.html",
            message="Kuvaus saa olla korkeintaan 200 merkkiä pitkä"
        )
    success = rooms.create_room(name, description, session["user_id"])
    if not success:
        return redirect("/error?type=none")
    return redirect("/")

@app.route("/threads", methods=["POST"])
def post_thread():
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    name = request.form["name"]
    if len(name) > 50:
        return render_template(
            "error.html",
            message="Nimi saa olla korkeintaan 50 merkkiä pitkä"
        )
    if len(name) < 3:
        return render_template(
            "error.html",
            message="Nimen tulee olla vähintään 3 merkkiä pitkä"
        )
    room_id = request.form["room_id"]
    user_id = session["user_id"]
    room = rooms.get_room(room_id)
    admin = user_id == room.user_id or users.check_admin_status(user_id, room_id)
    if room is None:
        return redirect("/error")
    if not admin:
        return render_template("error.html", message = "Ei oikeuksia")
    success = threads.create_thread(name, room_id)
    if not success:
        return redirect("/error")
    return redirect("/rooms/" + str(room.id))

@app.route("/messages", methods=["POST"])
def post_message():
    if session["csrf_token"] != request.form["csrf_token"]:
        return abort(403)
    room_id = request.form["room_id"]
    content = request.form["content"]
    if len(content) > 200:
        return render_template(
            "error.html",
            message="Viesti saa olla enintään 200 merkkiä pitkä"
        )
    if len(content) < 1:
        return render_template(
            "error.html",
            message="Viesti ei saa olla tyhjä"
        )
    thread_id = request.form["thread_id"]
    user_id = session["user_id"]
    success = messages.create_message(content, thread_id, user_id)
    if not success:
        return redirect("/error")
    return redirect("/rooms/" + room_id)

@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    user = users.get_user_by_username(username)
    if user is None:
        return redirect("/error")
    return render_template("profile.html", user = user)
