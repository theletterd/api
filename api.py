import time

from flask import Flask
from flask import jsonify
#from flask import render_template

app = Flask(__name__)


@app.route("/")
def root():
    return "Hi there!"

@app.route("/time")
def get_time():
    data = {
        "time": round(time.time())
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()


