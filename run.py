import os
from flask import (
    Flask, render_template, redirect,
    url_for, request, session, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
import bcrypt


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    recipe = mongo.db.recipes.find().sort("<recipe_id>", 1).limit(3)
    return render_template(
        "index.html", page_title="Recently Added Recipes", recipes=recipe)


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("register.html")


# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


# Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipe = mongo.db.recipes.find()

    if session:
        return render_template(
            "profile.html", username=username, recipes=recipe)

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# All Recipes
@app.route("/recipes")
def recipes():
    recipe = mongo.db.recipes.find()
    return render_template(
        "recipes.html", page_title="All Recipes", recipes=recipe)


# Recipe CRUD Funtionality
# Add/Create a new recipe
@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    if request.method == "POST":
        # Key value pairs 
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_preptime": request.form.get("recipe_preptime"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_step1": request.form.get("recipe_step1"),
            "recipe_step2": request.form.get("recipe_step2"),
            "recipe_step3": request.form.get("recipe_step3"),
            "created_by": session["user"],
            "recipe_url": request.form.get("recipe_name")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))
    return render_template("addrecipe.html", page_title="Add A Recipe")


# Individual recipe page
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("method.html", recipe=recipe)


# Edit recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # update the form with new values
    if request.method == "POST":
        # Key value pairs 
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_preptime": request.form.get("recipe_preptime"),
            "recipe_servings": request.form.get("recipe_servings"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_step1": request.form.get("recipe_step1"),
            "recipe_step2": request.form.get("recipe_step2"),
            "recipe_step3": request.form.get("recipe_step3"),
            "created_by": session["user"],
            "recipe_url": request.form.get("recipe_name")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipes"))

    # retrieve recipe from db to edit
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


# Delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Remove recipe from db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
