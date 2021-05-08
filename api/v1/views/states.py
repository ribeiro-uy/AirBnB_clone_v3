#!/usr/bin/python3
"""new view for State objects that handles all default RestFul API actions"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
def getmethod(state_id):
    """get method def"""
    if (state_id):
        name = "State." + state_id
        if (name in storage.all()):
            return jsonify((storage.get(State, state_id))
                           .to_dict())
        else:
            abort(404)
    else:
        states = []
        for state in storage.all("State").values():
            states.append(state.to_dict())
        return jsonify(states)
