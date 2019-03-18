from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ad")
def sign_up():
    return render_template("signUp.html")

# @app.route("/signUp")
# def signUp():
#     return render_template("signUp.html")

@app.route("/output", methods=["POST"])
def sUp():
    # read the posted values from the UI
    name = request.form['your_name']
    email = request.form['your_email']

    #
    # # validate the received values
    if name and email:
        return "Yes it works"


if  __name__ == "__main__":
    app.run(debug=True)
