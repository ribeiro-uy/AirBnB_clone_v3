#!/usr/bin/python3
"""index file"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify

@app_views.route("/status")
def status_url ():
    """ method that returns a status JSON """
    return jsonify({"status": "OK"})
