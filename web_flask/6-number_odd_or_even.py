#!/usr/bin/python3
""" Made by Tomas de Castro for Holberton School 2021 """
from flask import Flask, render_template


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


@app.route('/c/<text>')
def C_world(text):
    """ Returns all with C """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def Python_world(text='is cool'):
    """ Returns all with Python """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def integer_world(n):
    """ Returns all with number """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Returns number in a html pages """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def oddeven_template(n):
    """ Returns number in a html pages """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
