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
from src.v1.endpoints.stackoptions import StackOptions


stack_options_v1 = Blueprint('stack_options_v1', __name__, url_prefix="/v1")

###########################
##### GenericEndpoint #####
###########################

stack_options_v1.add_url_rule(StackOptions.uri,
        view_func=StackOptions.as_view(StackOptions.__name__))
