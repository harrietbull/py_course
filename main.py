from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/signUp")
# def signUp():
#     return render_template("signUp.html")

@app.route("/signUp", methods=["POST"])
def signUp():
    # read the posted values from the UI
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    # validate the received values
    if name and email and password:
        return "You are signed up"

if  __name__ == "__main__":
    app.run(debug=True)
