#!/usr/bin/python3
"""New view for Cities objects that handles all default RestFul API actions."""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort, request
from models import storage
from models.city import City
from models.state import State


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def getCity(city_id=None):
    """Defines get method 1."""
    objName = storage.get(City, city_id)
    if objName is not None:
        return jsonify(objName.to_dict())
    abort(404)


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def getCity2(state_id):
    """defines get method 2."""
    if (("State." + state_id) in storage.all()):
        cities = []
        for city in storage.all("City").values():
            if (city.state_id == state_id):
                print(city)
                cities.append(city.to_dict())
            return jsonify(cities)
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteCity(city_id):
    """Defines delete method."""

    objName = "City." + city_id
    if objName in storage.all():
        storage.get(City, city_id).delete()
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def postCity(state_id=None):
    """Defines post method."""
    state = storage.get(State, state_id)
    if state is not None:
        if not request.get_json():
            abort(400, 'Not a JSON')
        if 'name' not in request.get_json():
            abort(400, 'Missing name')
        request.get_json()['state_id'] = state_id
        newCity = City(**request.get_json())
        newCity.save()
        return jsonify(newCity.to_dict()), 201
    abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def putCity(city_id=None):
    """Defines put method."""

    city = storage.get(City, city_id)
    if city is not None:
        testing = request.get_json()
        if testing is None:
            abort(400, 'Not a JSON')
        for key, value in testing.items():
            setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict()), 200
    else:
        abort(404)
