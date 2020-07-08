#!/usr/bin/env python3

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"]
        )

@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return "Enjoy this message. It will only display once per day!"

@app.route("/fast")
def fast():
    return "I inherit the default limits of 200 per day and 50 per hour."

@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG FOEVER!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
