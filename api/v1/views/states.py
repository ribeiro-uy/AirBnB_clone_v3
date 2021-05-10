#!/usr/bin/python3
"""new view for State objects that handles all default RestFul API actions"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def getMethod(state_id=None):
    """get method def"""
    if (state_id):
        objName = "State." + state_id
        if (objName in storage.all()):
            return jsonify((storage.get(State, state_id))
                           .to_dict())
        else:
            abort(404)
    else:
        states = []
        for state in storage.all("State").values():
            states.append(state.to_dict())
        return jsonify(states)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteMethod(state_id):
    """delete method def"""

    objName = "State." + state_id
    if objName in storage.all():
        storage.get(State, state_id).delete()
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def postMethod():
    """Defines post method"""

    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    newState = State(**request.get_json())
    newState.save()
    return (jsonify(newState.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def putMethod(city_id=None):
    """Defines put method"""
	
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
