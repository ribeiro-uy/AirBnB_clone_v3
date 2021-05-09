#!/usr/bin/python3
"""index file"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status_url():
    """ method that returns a status JSON """
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats_url():
    """ method that returns a status JSON """
    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)})
