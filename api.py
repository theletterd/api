import time

from flask_cors import cross_origin

from flask import Flask
from flask import jsonify


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Hi there!"})

@app.route("/time", methods=["GET"])
def get_time():
    data = {
        "time": round(time.time())
    }
    return jsonify(data)

@app.route("/about", methods=["GET"])
def about():
    data = {
        "about": ""
        "This API mostly exists so that I can add a bunch of different stuff without "
        "having to go through the laborious process of spinning up a new app every "
        "time I want to add an API endpoint",
        "endpoints": ""

    }
    return jsonify(data)

@app.route("/links", methods=["GET"])
@cross_origin(origins=r"https://*theletterd.co.uk")
def links():
    name_and_link = (
        ("Resume", "https://resume.theletterd.co.uk"),
        ("API", "https://api.theletterd.co.uk"),
        ("Stats", "https://stats.theletterd.co.uk"),
        ("Goals", "https://goals.theletterd.co.uk"),
        ("Blog", "https://blog.theletterd.co.uk"),
        ("Github", "https://github.com/theletterd")
    )
    data = [dict(name=name, link=link) for name, link in name_and_link]
    return jsonify(data)

@app.route("/who", methods=["GET"])
def who():
    data = {
        "name": "Duncan Cook",
        "email": "duncan.cook@theletterd.co.uk",
        "resume": "https://resume.theletterd.co.uk",
        "bio": "Some guy who likes coding"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
