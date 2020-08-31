#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
