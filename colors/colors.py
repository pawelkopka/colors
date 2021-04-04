import json
import os

from flask import Flask, jsonify, abort, request


app = Flask(__name__)
app.config.update(
    ENVIRONMENT=os.getenv("ENVIRONMENT", "Production"),
    FILE_NAME=os.getenv("FILE_NAME", "colors.json"),
)


def load_colors(file):
    with open(file, "r") as f:
        pre_colors = json.loads(f.read())
        return {color["color"]: color["value"] for color in pre_colors}


def save(file):
    with open(file, "w", encoding="utf-8") as f:
        post_colors = [
            {"color": color, "value": value} for color, value in colors_cache.items()
        ]
        json.dump(post_colors, f, indent=4)


@app.route("/")
@app.route("/colors")
def list_colors():
    return jsonify([key for key in colors_cache.keys()])


@app.route("/<name>", methods=["POST", "GET"])
def color(name):
    if request.method == "POST":
        value = request.get_data()
        colors_cache[name] = str(value, encoding="UTF-8")
        if app.config["ENVIRONMENT"] == "Production":
            save(app.config["FILE_NAME"])
        return jsonify({"color": name, "value": colors_cache[name]})
    else:
        try:
            return jsonify({"color": name, "value": colors_cache[name]})
        except KeyError:
            abort(404, description="Color not found")


if app.config["ENVIRONMENT"] == "Production":
    colors_cache = load_colors(app.config["FILE_NAME"])
