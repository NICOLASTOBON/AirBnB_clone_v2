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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_and_state(id=None):
    """ reaturn template """
    state = None
    states = storage.all(State)
    if id:
        val_id = "State." + id
        if val_id in states.keys():
            state = states[val_id]
    return render_template('9-states.html', id=id, state=state, states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
