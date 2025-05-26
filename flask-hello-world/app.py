from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/photos")
def photos():
    return render_template("photos.html", title="Photos")


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
