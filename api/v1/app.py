#!/usr/bin/python3
""" Api app"""
from os import getenv
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def handle_context(code):
    """ method to handle context and call close"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ method to handle error 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":

    if getenv("HBNB_API_HOST"):
        new_host = getenv("HBNB_API_HOST")
    else:
        new_host = "0.0.0.0"
    if getenv("HBNB_API_PORT"):
        new_port = getenv("HBNB_API_PORT")
    else:
        new_host = "5000"

    app.run(port=new_port, host=new_host, threaded=True)
