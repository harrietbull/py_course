from flask import Flask, render_template, url_for, redirect, request
import requests

app = Flask("__name__")

def send_simple_message(email, name):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc42735b98d7b464587d8a7396a7e7741.mailgun.org/messages",
        auth=("api", "5bb876706f10a10b2f2e5a3d12804f39-7caa9475-a3d1e7df"),
        data={"from": "Excited User <mailgun@sandboxc42735b98d7b464587d8a7396a7e7741.mailgun.org>",
              "to": [email],
              "subject": "Thanks for signing up "+name,
              "text": "You've signed up to receive more healthy updates - well done you!"})

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
        send_simple_message(email, name)
        return render_template("thanks.html")


if  __name__ == "__main__":
    app.run(debug=True)
