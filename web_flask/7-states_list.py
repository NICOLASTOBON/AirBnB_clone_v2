#!/usr/bin/python3
""" script that starts a Flask web application """

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ close session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def get_list_state():
    """ display a HTML page """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
