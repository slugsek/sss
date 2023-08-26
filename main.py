# Python code of the SSS

from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "<p>Congratulations, SSS web app!</p>"