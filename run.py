import os
import json
from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
import env
import bcrypt


app = Flask(__name__)


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index(): 
    if "username" in session:
        return "You are logged in as " + session["username"]
        return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({"name": request.form["username"]})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form["password"].encode("utf-8"), bcrypt.gensalt())
            users.insert({"name": request.form["username"], "password": hashpass})
            session["username"] = request.form["username"]
            return redirect(url_for("login"))

        return "That username already exists!"

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("index"))


@app.route("/profile")
def profile():
    return render_template("profile.html", page_title="Welcome User")


@app.route("/recipes")
def recipes():
    data = []
    with open("data/recipes.json", "r") as json_data:
        data= json.load(json_data)
    return render_template("recipes.html", page_title="All Recipes", recipes=data)


@app.route('/recipes/<recipe_name>')
def recipes_method(recipe_name):
    method = {}

    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == recipe_name:
                method = obj

    return render_template("method.html", method=method)


@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html", page_title="Add a Recipe")


@app.route("/saved")
def saved():
    return render_template("saved.html", page_title="Saved Recipes")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
