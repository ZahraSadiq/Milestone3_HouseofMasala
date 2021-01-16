import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html", page_title="Add a Recipe")


@app.route("/recipes")
def recipes():
    data = []
    with open("data/recipes.json", "r") as json_data:
        data= json.load(json_data)
    return render_template("recipes.html", page_title="All Recipes", recipes=data)


@app.route("/saved")
def saved():
    return render_template("saved.html", page_title="Saved Recipes")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)