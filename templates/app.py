from flask import Flask, render_template
imports requests

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POSTS"])
def weather():
    city = request.form["city"]
    unit = request.form["unit"]
    temp = getTemperature(city, unit)
    return "The user asked for {} temp in {}, and its {} in {}".format (city, unit, temp)    
