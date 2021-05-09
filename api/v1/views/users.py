#!/usr/bin/python3
"""new view for State objects that handles all default RestFul API actions"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort, request
from models import storage
from models.state import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def getMethod(state_id=None):
    """get method def"""
    if (user_id):
        objName = "User." + user_id
        if (objName in storage.all()):
            return jsonify((storage.get(User, user_id))
                           .to_dict())
        else:
            abort(404)
    else:
        states = []
        for User in storage.all("User").values():
            Users.append(User.to_dict())
        return jsonify(Users)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleteMethod(state_id):
    """delete method def"""

    objName = "User." + user_id
    if objName in storage.all():
        storage.get(User, user_id).delete()
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def postMethod():
    """Defines post method"""

    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    newUser = User(**request.get_json())
    newUser.save()
    return (jsonify(newUser.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def putMethod(state_id):
    """Defines put method"""

    if not request.get_json():
        abort(400, 'Not a JSON')
    objName = "User." + user_id
    if (objName in storage.all()):
        newUser = storage.get(User, user_id)
        changeUser = request.get_json()
        for key, value in changeUser.items():
            if (key == 'name'):
                setattr(newUser, key, value)
        newUser.save()
        return (jsonify(newUser.to_dict()), 200)
    else:
        abort(404)
