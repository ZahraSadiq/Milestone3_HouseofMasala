import os
import json
import env as config
from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo


app = Flask(__name__)


os.environ[“MONGO_URI”] = "mongodb+srv://zahrasadiq:<CodingMS32021>@myfirstcluster.vcalk.mongodb.net/<dbname>?retryWrites=true&w=majority"
app.secret_key = "my_secret_key"


mongo = PyMongo(app)


@app.route("/")
def index():
    if "username" in session:
        return "You are logged in as " + session["username"]
    
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid credentials, Please try again."
        else:
            session["loggin_in"] = True
            return redirect(url_for("profile"))
    return render_template("login.html", error=error)


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
