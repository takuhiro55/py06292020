#!/usr/bin/env python3

from flask import Flask

# Flask constructor takes the name of current module(__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a decorator
# teslls the application which URL should call the associated function
@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application

