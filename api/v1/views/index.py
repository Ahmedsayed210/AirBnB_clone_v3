#!/usr/bin/python3xx
from flask import Flask
from api.v1.views import app_views
from models import storage
import models
from flask import jsonify


@app_views.route('/status', stirct_slashes=False)
def return_json_status():
    """ return a JSON from Dict """
    return jsonify(status='OK')
