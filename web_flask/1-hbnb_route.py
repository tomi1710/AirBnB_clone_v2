#!/usr/bin/python3
""" Made by Tomas de Castro for Holberton School 2021 """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns a specific string """
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_world():
    """ Returns a specific string """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
