#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Return message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def message_route():
    """ Return message route /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def get_message_route(text):
    """ Return message with text """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """ Return message with text """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ return number only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Return template a HTML page """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ Return template if n is an odd or even """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
