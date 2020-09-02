#!/usr/bin/python3
""" script that starts a Flask web application """


from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ close session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def state_and_state(id=None):
    """ reaturn template """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
