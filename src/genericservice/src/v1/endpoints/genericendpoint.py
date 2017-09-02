"""
Package: genericservice.src.v1.endpoints
Filename: genericendpoint.py
Author(s): Grant W

Api endpoints for genericservice suggestions.
"""

# Python Imports
import os

# 3rd Party Imports
from flask import current_app as app, jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import BadRequest

# BT Imports


class GenericEndpoint(MethodView):

    uri = '/generic_route'

    def get(self):
        """Returns a generic response
        """

        return jsonify(1, 2, 3)
