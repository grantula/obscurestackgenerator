"""
Package: stackoptions-python.src.v1.endpoints
Filename: stackoptions.py
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


class StackOptions(MethodView):

    uri = '/stack_options'

    def get(self):
        """Returns a generic response
        """

        return jsonify({
            'operatingSystem':[
                'ubuntu',
                'centos',
                'debian',
                'freebsd',
                'openbsd',
                'suse',
                'fedora'
            ],
            'backEnd': [
                'python',
                'node',
                'java',
                'c#',
                'ruby',
                'go',
                'erlang',
                '.net'
            ],
            'frontEnd': [
                'react',
                'angular1',
                'angular2',
                'angular4',
                'vanilla javascript',
                'vuejs',
                'backbone'
            ],
            'server': [
                'apache',
                'nginx',
                'mongoose'
            ]
        })
