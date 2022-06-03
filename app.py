from flask import Flask
import time

app = Flask(__name__)


def validate_input(number):
    return number != 0


@app.route("/team/<int:post_id>")
def hello_world(post_id):
    if validate_input(post_id):
        print(1 / post_id)
    return "<p>Hello, team or maybe not</p>"


@app.route("/")
def hello_world2():
    return "<p>Hello</p>"
