"""
Package: genericservice.src.v1
Filename: routes.py
Author(s): Grant W

The routes for genericservice.
"""

# Python Imports

# 3rd Party Imports
from flask import Blueprint
from flask.views import MethodView

 # Local Imports
from src.v1.endpoints.genericendpoint import GenericEndpoint


genericservice_v1 = Blueprint('genericservice_v1', __name__, url_prefix="/v1")

###########################
##### GenericEndpoint #####
###########################

genericservice_v1.add_url_rule(GenericEndpoint.uri,
        view_func=GenericEndpoint.as_view(GenericEndpoint.__name__))
