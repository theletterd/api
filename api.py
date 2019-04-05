import time

from flask import Flask
from flask import jsonify
#from flask import render_template

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/", methods=["GET"])
def root():
    return "Hi there!"

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


