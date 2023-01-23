#!/usr/bin/python3
"""
Flask route that return json status response
and stats
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = [Amenity, City, Place, Review, State, User]


@app_views.route('/status', strict_slashes=False)
def index_status():
    """Return am api status OK"""
    return jsonify(status="OK")


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """Returns counts of all objects in storage"""
    return jsonify(
        amenities=storage.count(Amenity),
        cities=storage.count(City),
        places=storage.count(Place),
        reviews=storage.count(Review),
        states=storage.count(State),
        users=storage.count(User)
    )
