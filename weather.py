from flask import Flask, render_template,redirect, url_for, request
from markupsafe import escape


app = Flask(__name__)
@app.route("/")
def home():
    text_input = request.args.get("city")
    return render_template("index.html")

@app.route("/search?city=<city_name>")
def test(city_name):
    return f"looks like the city name is {escape(city_name)}"